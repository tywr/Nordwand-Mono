from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseMGlyph(SquareLowercaseGlyph):
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
    hx_ratio = 1
    stroke_x_ratio = 1
    stroke_y_ratio = 1
    stroke_x_dampening = 0.75
    mid_stroke_dampening = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        taper1 = min(1, self.taper1 * dc.taper)
        taper2 = min(0.75, self.taper2 * dc.taper)
        mid_y = (1 - self.mid_len) * (b.height - b.y1)
        hx = b.hx * self.hx_ratio
        hy = b.hy * self.loop_ratio
        sx, sy = self.get_strokes(dc)
        y1 = b.y1 + (1 - self.loop_ratio) * b.height
        smx = max(0, self.mid_stroke_dampening * (sx - dc.default_stroke)) + min(
            dc.default_stroke, sx
        )

        xl2 = b.xmid + smx / 2
        draw_arch(
            pen,
            smx,
            sy,
            b.x1 + sx - smx,
            y1,
            xl2,
            b.y2,
            hx * (xl2 - b.x1) / b.width,
            hy,
            handle_shift=self.handle_shift,
            taper=taper1,
            side="left",
            cut="bottom",
        )

        # Right arch (xmid to x2)
        xr1 = b.xmid - sx + smx / 2
        draw_arch(
            pen,
            sx,
            sy,
            xr1,
            y1,
            b.x2,
            b.y2,
            hx * (b.x2 - xr1) / b.width,
            hy,
            taper=taper2,
            handle_shift=self.handle_shift,
            side="left",
            cut="bottom",
        )

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.x_height)

        # Right stem
        draw_rect(pen, b.x2 - sx, 0, b.x2, (y1 + b.y2) / 2)

        draw_rect(
            pen,
            b.xmid - smx / 2,
            mid_y,
            b.xmid + smx / 2,
            (y1 + b.y2) / 2 + 1,
        )
