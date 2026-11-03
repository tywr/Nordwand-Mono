"""Refresh docs/ from the latest font build: copy the web fonts, and rebuild
the glyph inspector's list from them, so the page follows every font change.

The list holds one [codepoint, name] per character of the font, then one
[codepoint, name, feature, value(, style)] per character variant
(cvXX / ssXX), read from the fonts' substitution tables. `style` is set to
"italic" or "upright" when the variant only exists in that style.
"""

import json
import re
import shutil
import unicodedata
from pathlib import Path

from fontTools.pens.recordingPen import RecordingPen
from fontTools.ttLib import TTFont

from scripts.topo import topo

FONTS = Path("fonts/woff2")
DOCS = Path("docs")
PAGE = DOCS / "index.html"
GLYPH_DATA = re.compile(
    r'(<script id="glyph-data" type="application/json">)(.*?)(</script>)', re.S
)
FONT_VERSION = re.compile(r'(<span class="font-version">)(.*?)(</span>)')
TOPO = re.compile(r'(<svg class="topo-drawing"[^>]*>\s*)(.*?)(\s*</svg>)', re.S)


def name(cp, font):
    # Private use characters (Powerline) have no Unicode name
    return unicodedata.name(chr(cp), None) or font.getBestCmap()[cp]


def visible(cp):
    # Spaces, control and format characters have nothing to inspect
    return unicodedata.category(chr(cp)) not in ("Zs", "Cc", "Cf")


def outline(font, glyph):
    pen = RecordingPen()
    font.getGlyphSet()[glyph].draw(pen)
    return tuple(pen.value)


def variants(font):
    """{(codepoint, feature, value): outline} for every cvXX / ssXX of the
    font."""
    by_glyph = {}
    for cp, glyph in font.getBestCmap().items():
        by_glyph.setdefault(glyph, []).append(cp)
    gsub = font["GSUB"].table
    found = {}
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
                        for value, alternate in enumerate(alternates, 1):
                            # Mapped to itself: the variant is missing from
                            # this style (e.g. a regular_only glyph)
                            if alternate != glyph:
                                found[cp, tag, value] = outline(font, alternate)
    return found


def glyph_data(upright, italic):
    data = [
        [cp, name(cp, upright)]
        for cp in sorted(upright.getBestCmap())
        if visible(cp)
    ]
    up, it = variants(upright), variants(italic)

    def covers(b, a):
        """Variant b draws a's character the same in every style a exists in."""
        return b != a and b[0] == a[0] and all(
            style.get(b) == style[a] for style in (up, it) if a in style
        )

    # Drop variants another one already shows (e.g. an upright-only cv04=1
    # drawn like cv04=2), keeping the first of two identical ones
    keys = up.keys() | it.keys()
    keys = [
        v for v in keys
        if not any(covers(w, v) and not (covers(v, w) and v < w) for w in keys)
    ]
    for cp, tag, value in sorted(keys, key=lambda v: (v[1], v[0], v[2])):
        label = f"{name(cp, upright)}, ALTERNATE" + (f" {value}" if value > 1 else "")
        only = []
        if (cp, tag, value) not in up:
            only = ["italic"]
        elif (cp, tag, value) not in it:
            only = ["upright"]
        data.append([cp, label, tag, value] + only)
    return data


def version(font):
    """Release version of a font, from its revision: 1.302 -> v1.3.2."""
    revision = round(font["head"].fontRevision * 1000)
    major, rest = divmod(revision, 1000)
    return f"v{major}.{rest // 100}.{rest % 100}"


def main():
    fonts = sorted(FONTS.glob("*.woff2"))
    if not fonts:
        raise SystemExit(f"No fonts in {FONTS}/, run `make build-font` first")
    (DOCS / "fonts").mkdir(parents=True, exist_ok=True)
    for f in fonts:
        shutil.copy2(f, DOCS / "fonts" / f.name)

    upright = TTFont(FONTS / "NordwandMono-Regular.woff2")
    data = glyph_data(upright, TTFont(FONTS / "NordwandMono-Italic.woff2"))
    page = PAGE.read_text()
    page = FONT_VERSION.sub(lambda m: m.group(1) + version(upright) + m.group(3), page)
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    page, n = GLYPH_DATA.subn(lambda m: m.group(1) + blob + m.group(3), page)
    if n != 1:
        raise SystemExit(f'Expected one <script id="glyph-data"> in {PAGE}')
    bold = TTFont(FONTS / "NordwandMono-Bold.woff2")
    page, n = TOPO.subn(lambda m: m.group(1) + topo(bold) + m.group(3), page)
    if n != 1:
        raise SystemExit(f'Expected one <svg class="topo-drawing"> in {PAGE}')
    PAGE.write_text(page)

    alternates = sum(len(e) > 2 for e in data)
    print(f"{len(fonts)} fonts copied, {len(data) - alternates} characters "
          f"and {alternates} alternates listed in {PAGE}")


if __name__ == "__main__":
    main()
