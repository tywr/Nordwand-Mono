from nordwand_mono.glyphs.uppercase import UppercaseGlyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.loop import draw_loop


class UppercaseJGlyph(UppercaseGlyph):
    name = "uppercase_j"
    unicode = "0x4A"
    offset = -15
    cap_ratio = 0.85
    hx_ratio = 1
    hy_ratio = 0.45
    loop_ratio = 0.66
    tail_len = 0.35
    width_ratio = 0.93

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ec = self.extra_cut(dc)
        xc = self.cap_ratio * b.width
        y2 = self.loop_ratio * b.height + ec

        # Vertical stem (centered)
        draw_rect(pen, b.x2 - sx, (b.y1 + y2) / 2, b.x2, b.y2)

        # Top bar
        draw_rect(pen, b.x2 - xc, b.y2 - sy, b.x2, b.y2)

        # Corner to bottom
        hy = b.hy * (y2 - b.y1) / b.height
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, y2, b.hx, hy, cut="top")
