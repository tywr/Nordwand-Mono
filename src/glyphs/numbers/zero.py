from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class ZeroGlyph(NumberGlyph):
    name = "zero"
    unicode = "0x30"
    offset = 0
    slash = 0.2
    width_ratio = 1.06
    dot_stroke_ratio = 1.4
    hx_ratio = 0.95
    hy_ratio = 1

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
        sd = min(dc.stroke_x * self.dot_stroke_ratio, 140)

        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            hy,
        )

        draw_rect(
            pen,
            b.xmid - sd / 2,
            b.ymid - sd / 2,
            b.xmid + sd / 2,
            b.ymid + sd / 2,
        )

        # draw_parallelogramm_vertical(
        #     pen,
        #     dc.stroke_alt,
        #     dc.stroke_alt,
        #     b.x1 + dc.stroke_x,
        #     b.y1 + dc.stroke_y,
        #     b.x2 - dc.stroke_x,
        #     b.y2 - dc.stroke_y,
        # )
