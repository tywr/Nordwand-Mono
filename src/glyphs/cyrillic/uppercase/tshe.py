from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner

from glyphs.uppercase import UppercaseGlyph


class CyrillicUppercaseTsheGlyph(UppercaseGlyph):
    name = "cyrillic_uppercase_tshe"
    unicode = "0x040B"
    offset = 20
    height_ratio = 0.66
    hx_ratio = 1
    hy_ratio = 0.66
    taper = 0.65
    width_ratio = 0.99
    ending_thickness = 0.8
    loop_ratio = 0.9
    bottom_mid_ratio = 0.45
    serif_width = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            overshoot_top=True,
            uppercase=True,
            height="cap",
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        y2 = b.y1 + self.height_ratio * b.height
        yl = b.y2 - self.loop_ratio * b.height
        sw = self.serif_width * b.width

        # Top arch, cut at the bottom (only upper half drawn)
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            yl,
            b.x2,
            y2,
            self.hx_ratio * b.hx,
            self.hy_ratio * b.hy,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)
        draw_rect(pen, b.x2 - sx, 0, b.x2, (y2 + yl) / 2)
        draw_rect(pen, b.x1 + sx / 2 - sw / 2, b.y2 - sy, b.x1 + sx / 2 + sw / 2, b.y2)
