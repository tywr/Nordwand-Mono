from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.corner_double import draw_corner_double


class ZeroGlyph(NumberGlyph):
    name = "zero"
    unicode = "0x30"
    offset = 0
    slash = 0.2
    width_ratio = 1.06
    dot_stroke_ratio = 1.4
    hx_ratio = 0.9
    hy_ratio = 1
    # hy_ratio = 0.2
    # hm_ratio = 0.05
    # x_offset = 0.1
    # y_offset = 0.4

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
        # hm = self.hm_ratio * b.height
        # ox, oy = self.x_offset * b.width, self.y_offset * b.height
        # a = oy / ox
        #
        # draw_corner_double(
        #     pen,
        #     dc.stroke_x,
        #     dc.stroke_y,
        #     b.x1,
        #     b.ymid,
        #     b.xmid,
        #     b.y2,
        #     hx,
        #     hy,
        #     ox=self.x_offset,
        #     oy=self.y_offset,
        #     c=1,
        #     orientation="top-right"
        # )

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
