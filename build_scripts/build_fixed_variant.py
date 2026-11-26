"""Build desktop, web, and Nerd Font files for a fixed Nordwand variant."""

import argparse
from contextlib import ExitStack
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from unittest.mock import patch

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables.otTables import Feature, FeatureRecord
import yaml

from nordwand_mono import generate_font
from nordwand_mono.config import DrawConfig, FontConfig, apply_config_overrides
from nerd_variant import build_nerd_fonts, find_fontforge


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = Path(__file__).with_name("fixed-variant.yml")
NO_REQUIRED_FEATURE = 0xFFFF
FORMATS = ("ttf", "otf", "woff", "woff2")

select_style_glyphs = generate_font.select_style_glyphs
draw_config_for_weight = DrawConfig.for_weight


def select_upright_glyphs(glyphs, italic):
    return select_style_glyphs(glyphs, italic=False)


def draw_upright(w=400, italic=False):
    return draw_config_for_weight(w=w, italic=False)


def is_character_variant(tag):
    return re.fullmatch(r"cv[0-9]{2}", tag) is not None


def load_build_config(path):
    with path.open(encoding="utf-8") as file:
        config = yaml.safe_load(file)
    if not isinstance(config, dict):
        raise ValueError("The build configuration must contain a YAML mapping")
    unknown = config.keys() - {"font", "italic_from_upright", "features", "hinting", "formats", "nerd_font"}
    if unknown:
        raise ValueError(f"Unknown build configuration keys: {sorted(unknown, key=str)}")
    font = config.get("font", {})
    if not isinstance(font, dict):
        raise ValueError("font must contain a mapping of Nordwand font parameters")
    upright = config.get("italic_from_upright", True)
    if type(upright) is not bool:
        raise ValueError("italic_from_upright must be true or false")
    hinting = config.get("hinting")
    if hinting is not None and type(hinting) is not bool:
        raise ValueError("hinting must be true, false, or null")
    formats = config.get("formats", ["ttf"])
    if not isinstance(formats, list) or not formats or any(value not in FORMATS for value in formats):
        raise ValueError("formats must be a nonempty list containing ttf, otf, woff, or woff2")
    nerd = config.get("nerd_font", False)
    if type(nerd) is not bool:
        raise ValueError("nerd_font must be true or false")
    features = config.get("features", {})
    if not isinstance(features, dict):
        raise ValueError("features must map OpenType tags to numeric values")
    for tag, value in features.items():
        if not isinstance(tag, str) or not re.fullmatch(r"[A-Za-z0-9]{4}", tag):
            raise ValueError(f"Invalid OpenType feature tag: {tag!r}")
        if type(value) is not int or value < 0 or (value > 1 and not is_character_variant(tag)):
            raise ValueError(f"{tag} must use 0 or 1, or a numbered cvXX variant")
    return font, upright, features, hinting, set(formats), nerd


def selected_glyphs(table, feature, index):
    substitutes = {}
    for lookup_index in feature.LookupListIndex:
        for subtable in table.LookupList.Lookup[lookup_index].SubTable:
            if hasattr(subtable, "alternates"):
                for glyph, alternates in subtable.alternates.items():
                    if index <= len(alternates):
                        substitutes[glyph] = alternates[index - 1]
            elif index == 1 and hasattr(subtable, "mapping"):
                substitutes.update(subtable.mapping)
    return substitutes


def apply_feature_defaults(table, preferences):
    records = table.FeatureList.FeatureRecord
    feature_indices = {record.FeatureTag: index for index, record in enumerate(records)}
    disabled = {
        feature_indices[tag] for tag, value in preferences.items()
        if value == 0 and tag in feature_indices
    }
    enabled = {
        feature_indices[tag] for tag, value in preferences.items()
        if value > 0 and not is_character_variant(tag)
    }
    kept = {
        index for index, record in enumerate(records)
        if index not in disabled and index not in enabled
    }
    exported = [record for index, record in enumerate(records) if index in kept]
    languages_to_update = []
    required_records = {}
    for record in table.ScriptList.ScriptRecord:
        script = record.Script
        languages = [script.DefaultLangSys, *(entry.LangSys for entry in script.LangSysRecord)]
        for language in languages:
            if language is None:
                continue
            active = list(language.FeatureIndex)
            required = language.ReqFeatureIndex
            force = enabled.intersection([*active, required])
            required_record = records[required] if required in kept else None
            if force:
                # Sequence substitutions must run at layout time even without app settings.
                if required_record is not None:
                    force.add(required)
                lookups = tuple(sorted({
                    lookup for index in force for lookup in records[index].Feature.LookupListIndex
                }))
                if lookups not in required_records:
                    feature = Feature()
                    feature.FeatureParams = None
                    feature.LookupListIndex = list(lookups)
                    feature.LookupCount = len(lookups)
                    entry = FeatureRecord()
                    entry.FeatureTag = "PERS"
                    entry.Feature = feature
                    required_records[lookups] = entry
                    exported.append(entry)
                required_record = required_records[lookups]
            optional = [records[index] for index in active if index in kept]
            languages_to_update.append((language, optional, required_record))
    exported.sort(key=lambda record: record.FeatureTag)
    table.FeatureList.FeatureRecord = exported
    table.FeatureList.FeatureCount = len(exported)
    index_by_record = {id(record): index for index, record in enumerate(exported)}
    for language, optional, required in languages_to_update:
        language.FeatureIndex = [index_by_record[id(record)] for record in optional]
        language.FeatureCount = len(optional)
        language.ReqFeatureIndex = (
            index_by_record[id(required)] if required is not None else NO_REQUIRED_FEATURE
        )


def bake_features(path, preferences):
    with TTFont(path) as font:
        table = font["GSUB"].table
        features = {record.FeatureTag: record.Feature for record in table.FeatureList.FeatureRecord}
        substitutions = []
        for tag, value in sorted(preferences.items()):
            if value == 0:
                continue
            if tag not in features:
                raise ValueError(f"The font has no GSUB feature {tag}")
            if is_character_variant(tag):
                mapping = selected_glyphs(table, features[tag], value)
                if not mapping:
                    raise ValueError(f"The font has no alternate {tag}={value}")
                substitutions.append(mapping)
        for subtable in font["cmap"].tables:
            if subtable.isUnicode():
                for codepoint, glyph in subtable.cmap.items():
                    for mapping in substitutions:
                        glyph = mapping.get(glyph, glyph)
                    subtable.cmap[codepoint] = glyph
        apply_feature_defaults(table, preferences)
        font.save(path)


def build_desktop(target, weight, italic, upright, features, hinting, ttf, otf):
    hint = getattr(generate_font, "ttfautohint", None)
    with ExitStack() as stack:
        # Defer hinting when the generator requests it. Some checkouts omit it.
        hint_calls = (
            stack.enter_context(patch.object(generate_font, "ttfautohint")).call_args_list
            if ttf and callable(hint) else []
        )
        if italic and upright:
            # Use upright drawing data but leave italic=True for the shear and style metadata.
            stack.enter_context(patch.object(generate_font, "select_style_glyphs", select_upright_glyphs))
            stack.enter_context(patch.object(DrawConfig, "for_weight", staticmethod(draw_upright)))
        generate_font.build_font(
            output_path=str(target), weight=weight, italic=italic, ttf=ttf, otf=otf,
        )
    if otf:
        bake_features(target, features)
    if not ttf:
        return
    ttf_path = target.with_suffix(".ttf")
    bake_features(ttf_path, features)
    if hinting is False:
        return
    if hint_calls:
        for call in hint_calls:
            hint(*call.args, **call.kwargs)
    elif hinting is True:
        from ttfautohint import ttfautohint

        ttfautohint(in_file=str(ttf_path), out_file=str(ttf_path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Combined font and OpenType YAML")
    parser.add_argument(
        "--hint", action=argparse.BooleanOptionalAction,
        help="Force or disable ttfautohint, overriding the YAML setting",
    )
    args = parser.parse_args()
    try:
        font_options, upright, features, hinting, formats, nerd = load_build_config(args.config)
        apply_config_overrides(font_options)
    except (OSError, ValueError, yaml.YAMLError) as error:
        parser.error(f"{args.config}: {error}")
    if args.hint is not None:
        hinting = args.hint
    if not isinstance(FontConfig.family_name, str):
        parser.error("font.family_name must be text")
    family = FontConfig.family_name.replace(" ", "")
    if family in {".", ".."} or not re.fullmatch(r"[A-Za-z0-9_.-]+", family):
        parser.error("font.family_name must form a valid PostScript filename")
    fontforge = find_fontforge() if nerd else None
    need_ttf = nerd or bool(formats.intersection(("ttf", "woff", "woff2")))
    need_otf = "otf" in formats
    output_root = PROJECT / "custom-fonts"
    output_root.mkdir(exist_ok=True)
    output = output_root / family

    with TemporaryDirectory(prefix=".personal-build-", dir=output_root) as temporary:
        staging = Path(temporary)
        desktop = staging / "desktop"
        desktop.mkdir()
        sample = None
        for weight in FontConfig.weights:
            for italic in (False, True):
                style = generate_font._style_metadata(weight, italic)[1]
                target = desktop / f"{family}-{style}.otf"
                build_desktop(target, weight, italic, upright, features, hinting, need_ttf, need_otf)
                ttf_path = target.with_suffix(".ttf")
                if not italic and (sample is None or weight == 400):
                    sample = ttf_path
                if formats.intersection(("woff", "woff2")):
                    generate_font.write_web_fonts(
                        ttf_path, woff="woff" in formats, woff2="woff2" in formats, out_root=staging,
                    )
        if nerd:
            nerd_formats = formats.intersection(("ttf", "otf")) or {"ttf"}
            sources = sorted(path for path in desktop.iterdir() if path.suffix[1:] in nerd_formats)
            build_nerd_fonts(PROJECT, fontforge, sample, sources, staging / "nerd-font", FontConfig.family_name)
        for flavor in formats.intersection(("ttf", "otf")):
            directory = staging / flavor
            directory.mkdir()
            for font_path in desktop.glob(f"*.{flavor}"):
                font_path.replace(directory / font_path.name)
        for directory in staging.iterdir():
            if directory.name == "desktop":
                continue
            for path in directory.rglob("*"):
                if path.is_file():
                    target = output / path.relative_to(staging)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    path.replace(target)
    print(f"Personal fonts saved to {output}")


if __name__ == "__main__":
    main()
