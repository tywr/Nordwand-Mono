from glyphs.uppercase import UppercaseGlyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.rect import draw_rect


class UppercaseUGlyph(UppercaseGlyph):
    name = "uppercase_u"
    unicode = "0x55"
    offset = 0
    width_ratio = 1.10

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        draw_superellipse_loop(
            pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy, cut="top"
        )

        draw_rect(pen, b.x1, b.ymid, b.x1 + dc.stroke_x, b.y2)
        draw_rect(pen, b.x2 - dc.stroke_x, b.ymid, b.x2, b.y2)
