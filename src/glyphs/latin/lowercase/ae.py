from dataclasses import replace

from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph


class LowercaseAeGlyph(LowercaseAGlyph, LowercaseEGlyph):
    """An a and an e sharing the middle stroke, each drawn by its own glyph's
    code within its half of the body."""

    name = "lowercase_ae"
    unicode = "0xE6"
    offset = 0
    width_ratio = 1.3
    mid_height = 0.52
    cap_height = 0.7
    tail_height = 0.31
    stroke_ratio = 1
    stroke_smoothing = 0.6
    stroke_threshold = 60

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx = self.stroke_ratio * dc.stroke_x
        sx = max(0, self.stroke_smoothing * (sx - self.stroke_threshold)) + min(
            self.stroke_threshold, sx
        )
        sy = self.stroke_ratio * dc.stroke_y

        # Each half keeps the body's o shape once rescaled
        def half(x1, x2):
            return replace(b, x1=x1, x2=x2, hx=b.hx * (x2 - x1) / b.width)

        self.draw_a(
            pen, dc, half(b.x1, b.xmid + sx / 2), sx, sy, stem=False, right_taper=0.75
        )
        self.draw_e(pen, dc, half(b.xmid - sx / 2, b.x2), sx, sy, left_taper=0.75)
