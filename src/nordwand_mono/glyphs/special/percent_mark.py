from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.loop import draw_loop


class PercentMarkGlyph(Glyph):
    name = "percent_mark"
    unicode = "0x25"
    offset = 0
    width_ratio = 1.2
    offset_ratio_x = 0.45
    offset_ratio_y = 0.45
    zero_ratio = 0.475
    stroke_ratio = 1
    stroke_x_ratio = 0.8
    stroke_x_dampening = 0.5
    zero_stroke_dampening = 0.1

    def zero_stroke(self, dc):
        s, _ = self.get_strokes(dc)
        return self.get_thinned_stroke(
            dc, coefficient=self.zero_stroke_dampening, stroke=s
        )

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        h = self.zero_ratio * b.height
        w = self.zero_ratio * b.width
        ox = self.offset_ratio_x * b.width

        s, _ = self.get_strokes(dc)
        draw_parallelogramm(pen, s, b.x1, b.y1, b.x2, b.y2)

        sx = self.zero_stroke(dc)
        draw_loop(
            pen,
            sx,
            sx,
            b.x1 + ox / 2 - w / 2,
            b.y2 - h,
            b.x1 + ox / 2 + w / 2,
            b.y2 + dc.v_overshoot,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )
        draw_loop(
            pen,
            sx,
            sx,
            b.x2 - ox / 2 - w / 2,
            b.y1 - dc.v_overshoot,
            b.x2 - ox / 2 + w / 2,
            b.y1 - dc.v_overshoot + h,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )
