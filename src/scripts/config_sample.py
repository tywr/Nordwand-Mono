#!/usr/bin/env python3
"""Build the Regular OTF of a custom config and render a code sample with it.

Usage: python -m scripts.config_sample nordley
  reads configs/nordley/config.yml, writes configs/nordley/sample.png

Pass --weight to render another weight than Regular, e.g. --weight 425.
"""

import argparse
import os

from config import FontConfig as fc, load_config, weight_name
from generate_font import build_font
from scripts.samples import SAMPLE_1, _lexer, _target_image_width, render_sample
from pygments.lexers import PythonLexer


def main(name, weight=400):
    config_dir = os.path.join("configs", name)
    load_config(os.path.join(config_dir, "config.yml"))

    family = fc.family_name.replace(" ", "")
    out_root = f"custom-fonts/{family}"
    os.makedirs(f"{out_root}/otf", exist_ok=True)
    style = "Regular" if weight == 400 else weight_name(weight).replace(" ", "")
    font_path = f"{out_root}/otf/{family}-{style}.otf"
    build_font(output_path=font_path, weight=weight, ttf=False, out_root=out_root)

    render_sample(
        os.path.join(config_dir, "sample.png"),
        _lexer(PythonLexer),
        SAMPLE_1,
        font_path,
        _target_image_width(font_path),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("name", help="Folder name under configs/")
    parser.add_argument(
        "--weight", type=int, default=400, help="Weight to render (default: 400)"
    )
    args = parser.parse_args()
    main(args.name, args.weight)
