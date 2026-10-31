from draw.parallelogramm import draw_parallelogramm_legacy
from glyphs import Glyph
from glyphs.extra.ordinal_indicator import draw_scaled
from glyphs.numbers.one import OneGlyph
from glyphs.numbers.two import TwoGlyph
from glyphs.numbers.three import ThreeGlyph
from glyphs.numbers.four import FourGlyph


class FractionGlyph(Glyph):
    """Numerator digit top left, denominator digit bottom right, split by a slash."""

    offset = 0
    scale = 0.4
    stroke_ratio = 0.6
    spread = 0.25  # Horizontal shift of each digit from the centre, relative to the width
    numerator_top = 1  # Relative to the cap height
    denominator_top = 0.4  # Relative to the cap height
    slash_width = 0.4  # Relative to the width
    slash_stroke = 0.5

    def draw(self, pen, dc):
        cx = dc.window_width / 2
        dx = self.spread * dc.window_width
        for source, x, top in (
            (self.numerator, cx - dx, self.numerator_top),
            (self.denominator, cx + dx, self.denominator_top),
        ):
            draw_scaled(
                pen, dc, source, self.scale, self.stroke_ratio, x, top * dc.cap
            )

        hw = self.slash_width * dc.window_width / 2
        draw_parallelogramm_legacy(
            pen,
            dc.stroke_x * self.slash_stroke,
            dc.stroke_y * self.slash_stroke,
            cx - hw,
            0,
            cx + hw,
            dc.cap,
        )


class OneHalfGlyph(FractionGlyph):
    name = "onehalf"
    unicode = "0xBD"
    numerator = OneGlyph
    denominator = TwoGlyph


class OneQuarterGlyph(FractionGlyph):
    name = "onequarter"
    unicode = "0xBC"
    numerator = OneGlyph
    denominator = FourGlyph


class ThreeQuartersGlyph(FractionGlyph):
    name = "threequarters"
    unicode = "0xBE"
    numerator = ThreeGlyph
    denominator = FourGlyph
