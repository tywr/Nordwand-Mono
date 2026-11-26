"""Add Nerd Font icons to a finished Nordwand variant."""

import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
from unittest.mock import patch

from fontTools.misc.psCharStrings import T2CharString
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable

from nordwand_mono.scripts import nerd_font


def find_fontforge():
    executable = shutil.which("fontforge.exe") if os.name == "nt" else shutil.which("fontforge")
    if executable:
        return executable
    if os.name == "nt":
        for variable in ("ProgramFiles(x86)", "ProgramFiles"):
            directory = os.environ.get(variable)
            if directory:
                candidate = Path(directory) / "FontForgeBuilds" / "bin" / "fontforge.exe"
                if candidate.is_file():
                    return str(candidate)
        executable = shutil.which("fontforge")
        if executable:
            return executable
    raise RuntimeError("Nerd Font output requires FontForge. Add its executable to PATH.")


def load_icons(sample, patched, flavors):
    with TTFont(sample) as base, TTFont(patched) as font:
        new_codes = sorted(font.getBestCmap().keys() - base.getBestCmap().keys())
        if not new_codes:
            raise RuntimeError("The Nerd Fonts patcher produced no new Unicode glyphs")
        glyph_set = font.getGlyphSet()
        cmap = font.getBestCmap()
        icons, names, mappings = {}, {}, {}
        for code in new_codes:
            original = cmap[code]
            if original not in names:
                name = f"nerd.u{code:04X}"
                recording = DecomposingRecordingPen(glyph_set)
                glyph_set[original].draw(recording)
                ttf_glyph = cff_program = None
                if "ttf" in flavors:
                    pen = TTGlyphPen(None)
                    recording.replay(pen)
                    ttf_glyph = pen.glyph()
                    ttf_glyph.recalcBounds(None)
                if "otf" in flavors:
                    pen = T2CharStringPen(None, None)
                    recording.replay(pen)
                    cff_program = pen.getCharString().program
                icons[name] = (ttf_glyph, cff_program, font["hmtx"][original][1])
                names[original] = name
            mappings[code] = names[original]
    return mappings, icons


def add_icon_cmap(font, mappings):
    unicode_tables = [table for table in font["cmap"].tables if table.isUnicode()]
    combined = {**font.getBestCmap(), **mappings}
    for table in unicode_tables:
        if table.format == 4:
            table.cmap.update({code: name for code, name in mappings.items() if code < 0xFFFF})
        elif table.format == 12:
            table.cmap.update(mappings)
    if not any(table.platformID == 3 and table.platEncID == 10 for table in unicode_tables):
        table = CmapSubtable.newSubtable(12)
        table.platformID, table.platEncID, table.language = 3, 10, 0
        table.cmap = combined
        font["cmap"].tables.append(table)


def add_nerd_icons(source, target, base_family, nerd_family, mappings, icons):
    with TTFont(source) as font:
        base_cmap = font.getBestCmap()
        new_mappings = {code: name for code, name in mappings.items() if code not in base_cmap}
        names = list(dict.fromkeys(new_mappings.values()))
        order = font.getGlyphOrder() + names
        advance = font["hmtx"][base_cmap[32]][0]

        if "glyf" in font:
            for name in names:
                glyph = icons[name][0]
                font["glyf"][name] = glyph
                font["hmtx"][name] = (advance, glyph.xMin if glyph.numberOfContours else 0)
        else:
            cff = font["CFF "].cff
            top = cff.topDictIndex[0]
            strings = top.CharStrings
            private = top.Private
            index = strings.charStringsIndex
            width = [] if advance == private.defaultWidthX else [advance - private.nominalWidthX]
            for name in names:
                _, commands, bearing = icons[name]
                charstring = T2CharString(
                    program=width + commands, private=private, globalSubrs=cff.GlobalSubrs,
                )
                strings.charStrings[name] = len(index)
                index.append(charstring)
                font["hmtx"][name] = (advance, bearing)
            top.charset = order

        font.setGlyphOrder(order)
        font["maxp"].numGlyphs = len(order)
        add_icon_cmap(font, new_mappings)
        for name in font["name"].names:
            if name.nameID in (1, 3, 4, 6, 16, 18, 21):
                old, new = (base_family, nerd_family) if name.nameID != 6 else (
                    base_family.replace(" ", ""), nerd_family.replace(" ", ""),
                )
                value = name.toUnicode()
                if old not in value and name.nameID == 3:
                    old, new = base_family.replace(" ", ""), nerd_family.replace(" ", "")
                name.string = value.replace(old, new)
        if "CFF " in font:
            cff.fontNames[0] = font["name"].getDebugName(6)
            top.FullName = font["name"].getDebugName(4)
            top.FamilyName = nerd_family
        font.save(target)


def build_nerd_fonts(project, fontforge, sample, fonts, destination, family):
    cache = project / ".nerd-fonts" / nerd_font.PATCHER_VERSION
    with patch.object(nerd_font, "PATCHER_DIR", str(cache)):
        patcher = Path(nerd_font.fetch_patcher())
    flavors = {source.suffix.lstrip(".") for source in fonts}
    with TemporaryDirectory(prefix=".nerd-icons-", dir=destination.parent) as scratch:
        # FontForge has its own Python runtime on Windows.
        env = {key: value for key, value in os.environ.items() if key not in {"PYTHONHOME", "PYTHONPATH"}}
        print("Preparing Nerd Font icon outlines with FontForge", flush=True)
        result = subprocess.run(
            [
                fontforge, "-lang=py", "-script", str(patcher), "--complete", "--careful", "--mono",
                "--name", "Nordwand Icon Source", "--quiet", "--no-progressbars",
                "--outputdir", scratch, str(sample),
            ],
            env=env, capture_output=True, text=True, errors="replace",
        )
        if result.returncode:
            raise RuntimeError(f"Nerd Fonts patching failed:\n{(result.stdout + result.stderr)[-4000:]}")
        patched = list(Path(scratch).glob("*.ttf"))
        if len(patched) != 1:
            raise RuntimeError("Expected one TTF from the Nerd Fonts patcher")
        mappings, icons = load_icons(sample, patched[0], flavors)

    nerd_family = f"{family} NF"
    family_prefix = family.replace(" ", "")
    nerd_prefix = nerd_family.replace(" ", "")
    for source in fonts:
        out = destination / source.suffix.lstrip(".")
        out.mkdir(parents=True, exist_ok=True)
        filename = nerd_prefix + source.name[len(family_prefix):]
        add_nerd_icons(source, out / filename, family, nerd_family, mappings, icons)
        print(f"Nerd Font saved to {out / filename}", flush=True)

    shutil.copy2(project / "LICENSE-FONT.txt", destination)
    glyphs = patcher.parent / "src" / "glyphs"
    licenses = destination / "licenses"
    for source in glyphs.rglob("*"):
        if source.is_file() and (source.name.startswith("LICENSE") or source.name == "README.md"):
            out = licenses / source.relative_to(glyphs)
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, out)
