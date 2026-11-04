from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner

from glyphs import Glyph
from glyphs.composed_glyphs import LowercaseHStrokeGlyph


class CyrillicLowercaseDjeGlyph(Glyph):
    name = "cyrillic_lowercase_dje"
    unicode = "0x0452"
    offset = 20
    height_ratio = 0.66
    hx_ratio = 1
    hy_ratio = 0.66
    taper = 0.65
    width_ratio = 0.99
    ending_thickness = 0.8
    loop_ratio = 0.9
    bottom_mid_ratio = 0.45

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            overshoot_top=True,
            height="cap",
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        y2 = b.y1 + self.height_ratio * b.height
        yl = b.y2 - self.loop_ratio * b.height
        xmid = b.x1 + self.bottom_mid_ratio * b.width

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
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.ascent)
        draw_rect(pen, b.x2 - sx, 0, b.x2, (y2 + yl) / 2)
        draw_square_corner(
            pen,
            sx,
            sy,
            b.x2,
            b.y1,
            xmid,
            dc.descent,
            orientation="bottom-left",
        )
        # Same bar as ħ
        h = LowercaseHStrokeGlyph
        y = (dc.x_height + dc.ascent) / 2
        draw_rect(
            pen,
            b.x1 - h.bar_left * b.width,
            y - dc.stroke_alt / 2,
            b.x1 + sx + h.bar_right * b.width,
            y + dc.stroke_alt / 2,
        )
