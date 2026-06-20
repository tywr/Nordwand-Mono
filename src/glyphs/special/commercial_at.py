from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.corner import draw_corner


class CommercialAtGlyph(Glyph):
    name = "commercial_at"
    unicode = "0x40"
    offset = 0
    width_ratio = 1.22
    mid_ratio = 0.4
    bottom_offset_ratio = 0.12
    bottom_reach = 0.66
    inner_ratio_x = 0.66
    inner_ratio_y = 0.55
    ending_thickness = 0.8
    hx_ratio = 1.15
    hy_ratio = 1.15
    taper = 0.3
    inner_hx_ratio = 0.6
    inner_hy_ratio = 0.65

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        xb = b.x1 + b.width * self.bottom_reach
        y1 = b.y1 - b.height * self.bottom_offset_ratio
        ymid = b.y1 + b.height * self.mid_ratio
        wi, hi = self.inner_ratio_x * b.width, self.inner_ratio_y * b.height
        xi1, xi2 = b.x2 - wi, b.x2
        yi1, yi2 = ymid - hi / 2, ymid + hi / 2
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        ihx, ihy = self.inner_hx_ratio * b.hx, self.inner_hy_ratio * b.hy

        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_alt,
            xi1,
            yi1,
            xi2,
            yi2,
            ihx,
            ihy,
            side="right",
            taper=self.taper*dc.taper,
        )

        draw_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            b.ymid,
            b.xmid,
            b.y2,
            hx,
            hy,
            orientation="top-left",
        )
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            y1,
            b.x2,
            b.y2,
            hx,
            hy,
            cut="right",
        )

        draw_rect(pen, b.x2 - dc.stroke_x, yi1, b.x2, b.ymid)
        draw_rect(pen, b.xmid, y1, xb, y1 + dc.stroke_y)
