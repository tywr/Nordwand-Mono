from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.glyphs.lowercase import TailedLowercaseGlyph
from nordwand_mono.glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseY2Glyph(TailedLowercaseGlyph, SquareLowercaseGlyph):
    name = "lowercase_y_2"
    unicode = "0x79"
    default_italic = True
    offset = 0
    stroke_y_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        y1 = b.y1 + self.y1_offset * b.height
        yl = y1 + self.loop_ratio * b.height

        # Bottom arch, cut at top (only lower half drawn)
        draw_arch(
            pen,
            dc.stroke_x,
            self.stroke_y_ratio * dc.stroke_y,
            b.x1,
            y1,
            b.x2,
            yl,
            b.hx,
            self.loop_ratio * b.hy,
            taper=self.taper * dc.taper,
            handle_shift=self.handle_shift,
            side="right",
            cut="top",
        )

        # Left stem — starts from arch midpoint
        draw_rect(pen, b.x1, (yl + y1) / 2, b.x1 + dc.stroke_x, dc.x_height)

        self.draw_tail(pen, dc, b)
