"""Refresh docs/ from the latest font build: copy the web fonts, and rebuild
the glyph inspector's list from them, so the page follows every font change.

The list holds one [codepoint, name] per character of the font, then one
[codepoint, name, feature, value(, italic_only)] per character variant
(cvXX / ssXX), read from the fonts' substitution tables.
"""

import json
import re
import shutil
import unicodedata
from pathlib import Path

from fontTools.ttLib import TTFont

FONTS = Path("fonts/woff2")
DOCS = Path("docs")
PAGE = DOCS / "index.html"
GLYPH_DATA = re.compile(
    r'(<script id="glyph-data" type="application/json">)(.*?)(</script>)', re.S
)


def name(cp, font):
    # Private use characters (Powerline) have no Unicode name
    return unicodedata.name(chr(cp), None) or font.getBestCmap()[cp]


def visible(cp):
    # Spaces, control and format characters have nothing to inspect
    return unicodedata.category(chr(cp)) not in ("Zs", "Cc", "Cf")


def variants(font):
    """{(codepoint, feature, value)} for every cvXX / ssXX of the font."""
    by_glyph = {}
    for cp, glyph in font.getBestCmap().items():
        by_glyph.setdefault(glyph, []).append(cp)
    gsub = font["GSUB"].table
    found = set()
    for record in gsub.FeatureList.FeatureRecord:
        tag = record.FeatureTag
        if not re.fullmatch(r"cv\d\d|ss\d\d", tag):
            continue
        for index in record.Feature.LookupListIndex:
            for sub in gsub.LookupList.Lookup[index].SubTable:
                sub = getattr(sub, "ExtSubTable", sub)
                if hasattr(sub, "alternates"):
                    choices = sub.alternates
                elif hasattr(sub, "mapping"):
                    choices = {g: [a] for g, a in sub.mapping.items()}
                else:
                    # Contextual lookups (e.g. ss03 on the -> => ligatures)
                    # don't map a character to a variant
                    continue
                for glyph, alternates in choices.items():
                    for cp in by_glyph.get(glyph, []):
                        for value in range(1, len(alternates) + 1):
                            found.add((cp, tag, value))
    return found


def glyph_data(upright, italic):
    data = [
        [cp, name(cp, upright)]
        for cp in sorted(upright.getBestCmap())
        if visible(cp)
    ]
    up, it = variants(upright), variants(italic)
    for cp, tag, value in sorted(up | it, key=lambda v: (v[1], v[0], v[2])):
        label = f"{name(cp, upright)}, ALTERNATE" + (f" {value}" if value > 1 else "")
        data.append([cp, label, tag, value] + ([1] if (cp, tag, value) not in up else []))
    return data


def main():
    fonts = sorted(FONTS.glob("*.woff2"))
    if not fonts:
        raise SystemExit(f"No fonts in {FONTS}/, run `make build-font` first")
    (DOCS / "fonts").mkdir(parents=True, exist_ok=True)
    for f in fonts:
        shutil.copy2(f, DOCS / "fonts" / f.name)

    data = glyph_data(
        TTFont(FONTS / "NordwandMono-Regular.woff2"),
        TTFont(FONTS / "NordwandMono-Italic.woff2"),
    )
    page = PAGE.read_text()
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    page, n = GLYPH_DATA.subn(lambda m: m.group(1) + blob + m.group(3), page)
    if n != 1:
        raise SystemExit(f'Expected one <script id="glyph-data"> in {PAGE}')
    PAGE.write_text(page)

    alternates = sum(len(e) > 2 for e in data)
    print(f"{len(fonts)} fonts copied, {len(data) - alternates} characters "
          f"and {alternates} alternates listed in {PAGE}")


if __name__ == "__main__":
    main()
