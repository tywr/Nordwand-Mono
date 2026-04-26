#!/usr/bin/env python3
"""Render syntax-highlighted code snippets as PNGs using Nordwand Mono.

Usage: python -m scripts.samples
"""

import argparse
import os

from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.filters import TokenMergeFilter
from pygments.formatters import ImageFormatter
from pygments.lexers import CppLexer, HaskellLexer, PythonLexer
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
)


# Pygments' ImageFormatter calls PIL's draw.text() without OpenType features,
# so ligatures/calt never fire. Inject them globally — Pillow needs libraqm,
# which we've checked is present.
_orig_pil_text = ImageDraw.ImageDraw.text


def _pil_text_with_features(self, *args, **kwargs):
    kwargs.setdefault("features", ["liga", "calt"])
    return _orig_pil_text(self, *args, **kwargs)


ImageDraw.ImageDraw.text = _pil_text_with_features


# Gravity palette (~/.config/colorthemes/monochrome/gravity.yaml)
BG = "#121212"
FG = "#cccccc"
FG_BRIGHT = "#eeeeee"
PRIMARY = "#91c7d9"
PRIMARY_BRIGHT = "#abeaff"
CONTRAST = "#af875f"
CONTRAST_BRIGHT = "#d7af87"

# 10-step monochrome gradient from foreground (noir_0) toward background (noir_9),
# mirroring the noir_N scale used in ~/.config/nvim/lua/noir.lua.
NOIR_0 = "#cccccc"
NOIR_1 = "#b3b3b3"
NOIR_2 = "#9a9a9a"
NOIR_3 = "#808080"
NOIR_4 = "#707070"
NOIR_5 = "#606060"
NOIR_6 = "#505050"
NOIR_7 = "#424242"
NOIR_8 = "#2c2c2c"
NOIR_9 = "#1f1f1f"


class GravityNoirStyle(Style):
    """Monochrome syntax style mirroring the noir.lua treesitter mapping."""

    background_color = BG
    highlight_color = NOIR_8

    styles = {
        Text:                       FG,

        Comment:                    f"italic {NOIR_7}",
        Comment.Preproc:            NOIR_2,

        Keyword:                    NOIR_5,
        Keyword.Constant:           PRIMARY,                   # True / False / None
        Keyword.Namespace:          NOIR_6,                    # import / from
        Keyword.Pseudo:             NOIR_5,
        Keyword.Reserved:           NOIR_5,
        Keyword.Type:               NOIR_6,

        Operator:                   NOIR_6,
        Operator.Word:              NOIR_5,                    # and / or / not

        Punctuation:                NOIR_2,

        Name:                       NOIR_2,
        Name.Function:              f"bold {FG}",
        Name.Function.Magic:        f"bold {NOIR_2}",
        Name.Class:                 NOIR_1,
        Name.Builtin:               NOIR_2,
        Name.Builtin.Pseudo:        NOIR_2,                    # self / cls
        Name.Decorator:             f"bold {PRIMARY}",
        Name.Namespace:             NOIR_2,
        Name.Variable:              NOIR_2,
        Name.Variable.Magic:        NOIR_2,                    # __name__ / __init__
        Name.Constant:              NOIR_2,
        Name.Attribute:             NOIR_2,
        Name.Tag:                   NOIR_6,
        Name.Exception:             NOIR_2,

        String:                     PRIMARY,
        String.Doc:                 f"italic {PRIMARY}",
        String.Escape:              NOIR_2,
        String.Interpol:            NOIR_2,
        String.Affix:               NOIR_5,                    # f / r / b prefix

        Number:                     PRIMARY,

        Error:                      PRIMARY,
    }


SAMPLE_1 = '''\
def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


if __name__ == "__main__":
    print(fibonacci(10))
'''


SAMPLE_2 = '''\
#include <vector>
#include <iostream>

template <typename T>
auto max_element(const std::vector<T>& xs) -> T {
    T best = xs[0];
    for (const auto& x : xs) {
        if (x >= best) best = x;
    }
    return best;
}

int main() {
    std::vector<int> v {3, 1, 4, 1, 5, 9, 2, 6};
    std::cout << "max = " << max_element(v) << "\\n";
    return 0;
}
'''


SAMPLE_3 = '''\
module Fib where

import Data.List (foldl\\')

-- | Infinite list of Fibonacci numbers.
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

fact :: Int -> Integer
fact n = foldl\\' (*) 1 [1..fromIntegral n]

main :: IO ()
main = do
  let xs = take 10 fibs
  mapM_ print xs
  putStrLn $ "10! = " ++ show (fact 10)
'''


def _lexer(cls):
    """Build a lexer with adjacent same-type tokens merged so `->`, `==`, etc.
    survive into a single draw.text() call where HarfBuzz can ligate them."""
    lex = cls()
    lex.add_filter(TokenMergeFilter())
    return lex


SAMPLES = [
    ("sample_1.png", _lexer(PythonLexer), SAMPLE_1),
    ("sample_2.png", _lexer(CppLexer), SAMPLE_2),
    ("sample_3.png", _lexer(HaskellLexer), SAMPLE_3),
]


FONT_SIZE = 40
IMAGE_PAD = 48
LINE_PAD = 12
TARGET_CHARS = 56


def _target_image_width(font_path):
    """Width of an image holding TARGET_CHARS monospace columns plus padding."""
    font = ImageFont.truetype(font_path, FONT_SIZE)
    char_w = font.getlength("M")
    return int(round(char_w * TARGET_CHARS)) + 2 * IMAGE_PAD


def render_sample(output, lexer, code, font_path, target_width):
    import io

    formatter = ImageFormatter(
        font_name=font_path,
        font_size=FONT_SIZE,
        line_numbers=False,
        style=GravityNoirStyle,
        image_pad=IMAGE_PAD,
        line_pad=LINE_PAD,
    )
    png_bytes = highlight(code, lexer, formatter)
    rendered = Image.open(io.BytesIO(png_bytes)).convert("RGB")

    if rendered.width > target_width:
        print(
            f"  warning: {output} is {rendered.width}px wide, exceeds target "
            f"{target_width}px — a line is longer than {TARGET_CHARS} chars"
        )
        canvas = rendered
    else:
        canvas = Image.new("RGB", (target_width, rendered.height), BG)
        canvas.paste(rendered, (0, 0))

    os.makedirs(os.path.dirname(output), exist_ok=True)
    canvas.save(output)
    print(f"Saved {output} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code-sample PNGs")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/ttf/NordwandMono-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output-dir", default="assets/samples", help="Output directory"
    )
    args = parser.parse_args()

    target_width = _target_image_width(args.font)
    for filename, lexer, code in SAMPLES:
        render_sample(
            os.path.join(args.output_dir, filename),
            lexer,
            code,
            args.font,
            target_width,
        )
