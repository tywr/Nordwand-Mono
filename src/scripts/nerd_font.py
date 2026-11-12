#!/usr/bin/env python3
"""Generate Nerdwand Mono, the Nerd Font patched version of Nordwand Mono.

Patches every OTF and TTF in fonts/ with the complete Nerd Fonts icon set
using the official font-patcher (downloaded on first run). The no-ligatures
(NL) family is not patched. Icons are kept to a single cell, and the
original glyphs keep their source advances, so the results stay as
monospaced as the base fonts.

Requires fontforge on the PATH. Run `make build-font` first.

Output: fonts/nerd-font/{otf,ttf}/ plus the font license and the licenses of
every patched-in icon set.

Usage: python -m scripts.nerd_font
"""

import argparse
import glob
import hashlib
import io
import os
import re
import shutil
import subprocess
import tempfile
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

from fontTools.ttLib import TTFont


FAMILY_NAMES = (
    ("Nerdwand Mono", "NordwandMono"),
)
FLAVORS = ("otf", "ttf")
PATCHER_VERSION = "3.5.1"
PATCHER_URL = (
    "https://github.com/ryanoasis/nerd-fonts/releases/download/"
    f"v{PATCHER_VERSION}/FontPatcher.zip"
)
PATCHER_SHA256 = "42bcb32145499a35732274c7fc48deb434ad0d2e0e118f98527c1479c6fa251a"
PATCHER_DIR = f".nerd-fonts/{PATCHER_VERSION}"
INPUT_DIR = "fonts"
OUTPUT_DIR = "fonts/nerd-font"


def fetch_patcher():
    patcher = os.path.join(PATCHER_DIR, "font-patcher")
    if not os.path.exists(patcher):
        print(f"Downloading Nerd Fonts patcher v{PATCHER_VERSION}")
        with urllib.request.urlopen(PATCHER_URL) as response:
            archive = response.read()
        digest = hashlib.sha256(archive).hexdigest()
        if digest != PATCHER_SHA256:
            raise SystemExit(
                f"Patcher checksum mismatch: expected {PATCHER_SHA256}, got {digest}"
            )
        zipfile.ZipFile(io.BytesIO(archive)).extractall(PATCHER_DIR)
    return patcher


def style_name(path):
    """NordwandMono-SemiBoldItalic.ttf -> "SemiBold Italic"."""
    style = os.path.splitext(os.path.basename(path))[0].split("-", 1)[1]
    return re.sub(r"(?<=[a-z])(?=Italic)", " ", style)


def patch(patcher, path, output_dir, family_name):
    style = os.path.splitext(os.path.basename(path))[0].split("-", 1)[1]
    work_dir = tempfile.mkdtemp(prefix=f".{style}.", dir=output_dir)
    try:
        subprocess.run(
            [
                "fontforge",
                "-script",
                patcher,
                "--complete",
                "--careful",
                "--mono",
                "--name",
                f"{family_name} {style_name(path)}",
                "--quiet",
                "--no-progressbars",
                "--outputdir",
                work_dir,
                path,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        # The patcher keeps the input flavor (.otf in -> .otf out)
        written = glob.glob(os.path.join(work_dir, "*.ttf")) + glob.glob(
            os.path.join(work_dir, "*.otf")
        )
        if len(written) != 1:
            raise SystemExit(f"Expected exactly one font in {work_dir}, got: {written}")
        fix_style_names(written[0], family_name, style)
        restore_advances(path, written[0])
        ext = os.path.splitext(written[0])[1]
        out_name = f"{family_name.replace(' ', '')}-{style}{ext}"
        shutil.move(written[0], os.path.join(output_dir, out_name))
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)
    print(f"Patched {path} ({family_name})")


def fix_style_names(patched_path, family_name, style):
    """Restore the name tables for non-RIBBI weights.

    The Nerd Fonts name parser treats "Book" as an alias of "Regular" and
    drops the typographic family/subfamily names (IDs 16/17) that the base
    fonts carry for non-RIBBI weights. Both are rebuilt from the style;
    the values are exactly what the base fonts use, so overwriting is safe.
    """
    italic = style.endswith("Italic")
    weight = style[: -len("Italic")] if italic else style
    if weight in ("", "Regular", "Bold", "Italic"):
        return
    font = TTFont(patched_path)
    full = f"{family_name} {weight}"
    records = {
        1: full,
        2: "Italic" if italic else "Regular",
        3: f"{full} {PATCHER_VERSION}",
        4: f"{full} Italic" if italic else full,
        6: f"{family_name}-{style}".replace(" ", ""),
        16: family_name,
        17: f"{weight} Italic" if italic else weight,
    }
    for name_id, value in records.items():
        for platform, encoding, lang in ((1, 0, 0), (3, 1, 0x409)):
            font["name"].setName(value, name_id, platform, encoding, lang)
    font.save(patched_path)


def restore_advances(src_path, patched_path):
    """Restore the original (advance, lsb) of every base glyph.

    --mono forces all advances to a single cell, squeezing double-width
    ligatures, and fontforge rewrites lsb on save. Only the added icons
    should differ from the source font.
    """
    src_hmtx = TTFont(src_path)["hmtx"]
    font = TTFont(patched_path)
    for name, metrics in src_hmtx.metrics.items():
        if name in font["hmtx"].metrics:
            font["hmtx"][name] = metrics
    font.save(patched_path)


def copy_licenses(output_dir):
    """Ship the font license and the licenses of every patched-in icon set."""
    shutil.copy("LICENSE-FONT.txt", output_dir)
    glyphs_dir = os.path.join(PATCHER_DIR, "src", "glyphs")
    licenses_dir = os.path.join(output_dir, "licenses")
    os.makedirs(licenses_dir, exist_ok=True)
    shutil.copy(os.path.join(glyphs_dir, "README.md"), licenses_dir)
    for path in glob.glob(os.path.join(glyphs_dir, "*", "LICENSE*")):
        icon_set = os.path.basename(os.path.dirname(path))
        os.makedirs(os.path.join(licenses_dir, icon_set), exist_ok=True)
        shutil.copy(path, os.path.join(licenses_dir, icon_set))


def generate(output_dir=OUTPUT_DIR):
    patcher = fetch_patcher()
    os.makedirs(output_dir, exist_ok=True)

    tasks = []
    for family_name, prefix in FAMILY_NAMES:
        for flavor in FLAVORS:
            flavor_dir = os.path.join(output_dir, flavor)
            os.makedirs(flavor_dir, exist_ok=True)
            paths = sorted(glob.glob(f"{INPUT_DIR}/{flavor}/{prefix}-*.{flavor}"))
            if not paths:
                raise SystemExit(
                    f"No {flavor} fonts found for {prefix!r}, run "
                    "`make build-font` first"
                )
            tasks.extend((path, flavor_dir, family_name) for path in paths)

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as pool:
        list(pool.map(lambda task: patch(patcher, *task), tasks))
    copy_licenses(output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate the Nerdwand Mono Nerd Font")
    parser.add_argument(
        "-o",
        "--output",
        default=OUTPUT_DIR,
        help=f"Output directory (default: {OUTPUT_DIR})",
    )
    args = parser.parse_args()
    generate(args.output)
