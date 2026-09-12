from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class CyrillicUppercaseYuGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_yu"
    unicode = "0x042E"
    offset = 8
    width_ratio = 1.24
    mid_ratio = 0.33
    ymid_ratio = 0.518

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        lx1 = b.x1 + self.mid_ratio * b.width
        hx = (1 - self.mid_ratio) * b.hx
        ymid = b.y1 + self.ymid_ratio * b.height

        draw_loop(
            pen,
            sx,
            sy,
            lx1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            b.hy,
        )

        draw_rect(
            pen,
            b.x1,
            0,
            b.x1 + sx,
            dc.cap,
        )
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            lx1 + sx / 2,
            ymid + sy / 2,
        )
