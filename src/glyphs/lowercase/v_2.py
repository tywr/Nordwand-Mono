from glyphs import Glyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class LowercaseV2Glyph(Glyph):
    name = "lowercase_v_2"
    default_italic = True
    unicode = "0x76"
    offset = 14
    width_ratio = 0.98
    stroke_ratio = 0.96
    overlap = 0.33
    lower_section_height = 1.2
    tail_ratio = 0.15
    loop_ratio = 0.66
    hx_ratio = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        xt = b.x1 - self.tail_ratio * b.width
        w = b.x2 - b.x1 - dc.stroke_x

        draw_rect(pen, xt, b.y2 - dc.stroke_y, b.x1, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x1 + dc.stroke_x, b.y2)
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
            quarter="top-right",
        )
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1 + dc.stroke_x - w,
            b.y1,
            b.x2,
            b.y2,
            b.hx * 2 * w / b.width,
            b.hy,
            quarter="bottom-right",
        )
