from math import radians, tan

from glyphs import Glyph
from glyphs.special.quotation_mark import QuotationMarkGlyph
from draw.polygon import draw_polygon


class PrimeGlyph(Glyph):
    """Minutes and feet: a wedge hanging from the ascent, leaning right and
    thinning towards its foot. As tall as the apostrophe."""

    name = "prime"
    unicode = "0x2032"
    offset = 0
    width_ratio = 1
    height_ratio = QuotationMarkGlyph.height_ratio
    gap = 0.18
    angle = 18
    foot_ratio = 0.75
    count = 1
    stroke_ratio = 1.3

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = self.height_ratio * b.height
        s = self.stroke_ratio * dc.stroke_x
        sf = self.foot_ratio * s
        lean = h * tan(radians(self.angle))
        # Spaced like the bars of `"` when there are several
        step = self.gap * b.width + s
        first = b.xmid - (self.count - 1) * step / 2
        for i in range(self.count):
            x = first + i * step
            xt, xb = x + lean / 2, x - lean / 2
            draw_polygon(
                pen,
                [
                    (xb - sf / 2, dc.ascent - h),
                    (xb + sf / 2, dc.ascent - h),
                    (xt + s / 2, dc.ascent),
                    (xt - s / 2, dc.ascent),
                ],
            )


class DoublePrimeGlyph(PrimeGlyph):
    """Seconds and inches."""

    name = "double_prime"
    unicode = "0x2033"
    count = 2

class TriplePrimeGlyph(PrimeGlyph):
    """Seconds and inches."""

    name = "triple_prime"
    unicode = "0x2034"
    count = 3
