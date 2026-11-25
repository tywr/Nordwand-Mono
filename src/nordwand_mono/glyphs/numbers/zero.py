from nordwand_mono.glyphs.numbers import NumberGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.dot import draw_dot


class ZeroGlyph(NumberGlyph):
    name = "zero"
    unicode = "0x30"
    offset = 0
    slash = 0.2
    width_ratio = 1.06
    dot_ratio = 1.5
    hx_ratio = 0.9
    hy_ratio = 1
    hm_ratio = 0.05
    x_offset = 0.1
    y_offset = 0.4
    dot = True

    def draw_mark(self, pen, dc, b):
        draw_dot(pen, dc, b.xmid, b.ymid, self.dot_ratio)

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            number=True,
        )
        hx = self.hx_ratio * b.hx
        hy = self.hy_ratio * b.hy
        sx, sy = self.get_strokes(dc)

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            hy,
        )
        if self.dot:
            self.draw_mark(pen, dc, b)
