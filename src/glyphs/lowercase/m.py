from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class LowercaseMGlyph(Glyph):
    name = "lowercase_m"
    unicode = "0x6D"
    offset = 0
    width_ratio = 1.18
    mid_len = 0.75
    taper1 = 0.5
    taper2 = 1.0
    min_taper = 0.1
    min_taper_2 = 0.15
    ending_thickness = 0.75
    min_width = 74
    hx_ratio = 1.15
    stroke_x_ratio = 1
    stroke_y_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        taper1 = min(1, self.taper1 * dc.taper)
        taper2 = min(1, self.taper2 * dc.taper)
        mid_y = (1 - self.mid_len) * (b.height - b.y1)
        hx = b.hx * self.hx_ratio
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        sx = max(0, 0.8 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)

        xl2 = b.xmid + sx / 2
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            xl2,
            b.y2,
            hx * (xl2 - b.x1) / b.width,
            b.hy,
            taper=taper1,
            side="left",
            cut="bottom",
        )

        # Right arch (xmid to x2)
        xr1 = b.xmid - sx / 2
        draw_arch(
            pen,
            sx,
            sy,
            xr1,
            b.y1,
            b.x2,
            b.y2,
            hx * (b.x2 - xr1) / b.width,
            b.hy,
            taper=taper2,
            side="left",
            cut="bottom",
        )

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.x_height)

        # Right foot — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - sx, 0, b.x2, b.ymid)

        draw_rect(
            pen,
            b.xmid - sx / 2,
            mid_y,
            b.xmid + sx / 2,
            b.ymid + 1,
        )
