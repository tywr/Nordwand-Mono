from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.rect import draw_rect

from nordwand_mono.glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseHGlyph(SquareLowercaseGlyph):
    name = "lowercase_h"
    unicode = "0x68"
    offset = 0
    stroke_y_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            overshoot_top=True,
        )
        yl = b.y2 - self.loop_ratio * b.height

        # Top arch, cut at the bottom (only upper half drawn)
        draw_arch(
            pen,
            dc.stroke_x,
            self.stroke_y_ratio * dc.stroke_y,
            b.x1,
            yl,
            b.x2,
            b.y2,
            b.hx,
            self.loop_ratio * b.hy,
            taper=self.taper * dc.taper,
            handle_shift=self.handle_shift,
            side="left",
            cut="bottom",
        )
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        # Right stem — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, (b.y2 + yl) / 2)
