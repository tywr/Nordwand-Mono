from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.polygon import draw_polygon
from draw.corner import draw_corner


class CommercialAtGlyph(Glyph):
    name = "commercial_at"
    unicode = "0x40"
    offset = 0
    width_ratio = 1.22
    inner_ratio_x = 0.65
    inner_ratio_y = 0.45
    ending_thickness = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        wi, hi = self.inner_ratio_x * b.width, self.inner_ratio_y * b.height
        xi1, xi2 = b.x2 - wi, b.x2
        yi1, yi2 = b.ymid - hi / 2, b.ymid + hi / 2

        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_alt,
            xi1,
            yi1,
            xi2,
            yi2,
            b.hx * self.inner_ratio_x,
            b.hy * self.inner_ratio_y,
            side="right",
            taper=0.2,
        )

        draw_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            b.ymid,
            b.xmid,
            b.y2,
            b.hx,
            b.hy,
            orientation="top-left",
        )
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
            cut="right",
        )

        draw_rect(pen, b.x2 - dc.stroke_x, yi1, b.x2, b.ymid)
        draw_rect(pen, b.xmid, b.y1, b.x2 - dc.stroke_x, b.y1 + dc.stroke_y)
