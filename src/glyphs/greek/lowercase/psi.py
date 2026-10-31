from draw.rect import draw_rect
from draw.loop import draw_loop
from glyphs.lowercase.square import SquareLowercaseGlyph


class GreekLowercasePsiGlyph(SquareLowercaseGlyph):
    name = "greek_lowercase_psi"
    unicode = "0x3C8"
    offset = 0
    width_ratio = 1.1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx = max(0, 0.8 * (dc.stroke_x - dc.default_stroke)) + min(
            dc.default_stroke, dc.stroke_x
        )
        yl = b.y1 + self.loop_ratio * b.height
        ym = (yl + b.y1) / 2

        # Bottom arch, cut at top (only lower half drawn)
        draw_loop(
            pen,
            sx,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            yl,
            self.hx_ratio * b.hx,
            self.hy_ratio * b.hy,
            cut="top",
        )

        # Sides — start from arch midpoint
        draw_rect(pen, b.x1, ym, b.x1 + sx, dc.x_height)
        draw_rect(pen, b.x2 - sx, ym, b.x2, dc.x_height)
        # Middle stem
        draw_rect(
            pen,
            b.xmid - sx / 2,
            dc.descent,
            b.xmid + sx / 2,
            0,
        )
        draw_rect(
            pen,
            b.xmid - sx / 2,
            0,
            b.xmid + sx / 2,
            b.y2,
        )
