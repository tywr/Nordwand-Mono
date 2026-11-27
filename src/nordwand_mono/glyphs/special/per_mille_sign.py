from fontTools.misc.transform import Transform
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from nordwand_mono.config import FontConfig as fc
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.glyphs.special.percent_mark import PercentMarkGlyph


class PerMilleSignGlyph(PercentMarkGlyph):
    """A narrower percent sign with a second zero beside the bottom one."""

    name = "per_mille_sign"
    unicode = "0x2030"
    width_ratio = 0.7
    # Smaller zeros than the percent sign, so three of them fit in the cell
    zero_ratio = 0.42
    gap = 0.03  # Between the two bottom zeros, relative to the body width
    # Thinner zeros, so three of them keep open counters in one cell
    zero_stroke_ratio = 0.7

    def zero_stroke(self, dc):
        return self.zero_stroke_ratio * super().zero_stroke(dc)

    def draw(self, pen, dc):
        rec = RecordingPen()
        super().draw(rec, dc)

        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        h = self.zero_ratio * b.height
        w = self.zero_ratio * b.width
        ox = self.offset_ratio_x * b.width
        sx = self.zero_stroke(dc)
        x1 = b.x2 - ox / 2 + w / 2 + self.gap * b.width
        draw_loop(
            rec,
            sx,
            sx,
            x1,
            b.y1 - dc.v_overshoot,
            x1 + w,
            b.y1 - dc.v_overshoot + h,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )

        # Center the whole sign in the cell
        left = min(b.x1, b.x1 + ox / 2 - w / 2)
        dx = fc.window_width / 2 - (left + x1 + w) / 2
        rec.replay(TransformPen(pen, Transform(1, 0, 0, 1, dx, 0)))
