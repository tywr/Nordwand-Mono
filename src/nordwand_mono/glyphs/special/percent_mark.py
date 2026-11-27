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
    zero_ratio = 0.4
    stroke_ratio = 1
    stroke_x_dampening = 0.3
    zero_stroke_dampening = 0.0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        h = self.zero_ratio * b.height
        w = self.zero_ratio * b.width
        ox = self.offset_ratio_x * b.width
        oy = self.offset_ratio_y * b.height

        s, _ = self.get_strokes(dc)
        draw_parallelogramm(pen, s, b.x1, b.y1, b.x2, b.y2)

        sx = self.get_thinned_stroke(dc, coefficient=self.zero_stroke_dampening, stroke=s)
        draw_loop(
            pen,
            sx,
            sx,
            b.x1 + ox / 2 - w / 2,
            b.y2 - oy / 2 - h / 2,
            b.x1 + ox / 2 + w / 2,
            b.y2 - oy / 2 + h / 2,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )
        draw_loop(
            pen,
            sx,
            sx,
            b.x2 - ox / 2 - w / 2,
            b.y1 + oy / 2 - h / 2,
            b.x2 - ox / 2 + w / 2,
            b.y1 + oy / 2 + h / 2,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )
