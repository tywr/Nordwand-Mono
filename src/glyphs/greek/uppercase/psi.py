from glyphs.uppercase.u import UppercaseUGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class GreekUppercasePsiGlyph(UppercaseUGlyph):
    """Same as the U with a raised arch and a middle stem"""

    name = "greek_uppercase_psi"
    unicode = "0x3A8"
    arch_raise_ratio = 0.22
    width_ratio = 1.16
    inner_stroke_ratio = 1.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        y1 = b.y1 + self.arch_raise_ratio * b.height
        h = b.y2 - y1
        y2 = y1 + self.loop_ratio * h
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx = self.hx_ratio * b.hx
        hy = self.hy_ratio * b.hy * self.loop_ratio * h / b.height
        six = dc.stroke_alt * self.inner_stroke_ratio

        draw_loop(pen, sx, sy, b.x1, y1, b.x2, y2, hx, hy, cut="top")

        draw_rect(pen, b.x1, (y1 + y2) / 2, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, (y1 + y2) / 2, b.x2, b.y2)
        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, y1)
        draw_rect(pen, b.xmid - six / 2, y1, b.xmid + six / 2, b.y2)
