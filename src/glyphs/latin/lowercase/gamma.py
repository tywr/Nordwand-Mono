from draw.loop import draw_loop
from draw.parallelogramm import draw_parallelogramm
from glyphs import Glyph


def draw_gamma(pen, dc, b, s, sx, sy, loop_width, depth):
    """Two branches from the top corners of `b` crossing on their way down
    to the baseline, where they end `loop_width` of the body apart, closed
    by a round bottom down to `depth`: a teardrop hanging from the crossing."""
    w = loop_width * b.width
    xl, xr = b.xmid - w / 2, b.xmid + w / 2
    _, d = draw_parallelogramm(pen, s, xr, 0, b.x1, b.y2, direction="top-left")
    draw_parallelogramm(pen, s, xl, 0, b.x2, b.y2)
    hx = b.hx * w / b.width
    hy = b.hy * 2 * -depth / b.height
    draw_loop(pen, d, sy, xl, depth, xr, -depth, hx, hy, cut="top")


class LatinLowercaseGammaGlyph(Glyph):
    """v whose branches cross and close in a loop below the baseline (ɣ)."""

    name = "latin_lowercase_gamma"
    unicode = "0x263"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 1.0
    loop_width = 0.75
    loop_depth = 1  # Relative to the descent

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        draw_gamma(
            pen,
            dc,
            b,
            self.stroke_ratio * dc.stroke_x,
            dc.stroke_x,
            dc.stroke_y,
            self.loop_width,
            self.loop_depth * dc.descent - dc.v_overshoot,
        )
