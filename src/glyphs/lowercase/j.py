from glyph import Glyph
from shapes.corner import draw_corner
from shapes.rect import draw_rect


class LowercaseJGlyph(Glyph):
    name = "lowercase_j"
    unicode = "0x6A"
    offset = 160
    len_left = 320
    len_cap = 280
    corner_width = 160
    hx = 160
    hy = 160
    dot_width = 30
    tail_offset = 20  # Y-axis offset of the tail above the descender line

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)

        # Stem
        draw_rect(pen, b.xmid - dc.stroke / 2, 0, b.xmid + dc.stroke / 2, dc.x_height)
        # Left cap
        draw_rect(pen, b.xmid - self.len_cap - dc.stroke / 2, dc.x_height - dc.stroke, b.xmid, dc.x_height)
        # Corner curving down-left into the descender
        draw_corner(
            pen,
            dc.stroke,
            b.xmid + dc.stroke / 2,
            0,
            b.xmid - self.corner_width,
            dc.descent + self.tail_offset,
            self.hx,
            self.hy,
            orientation="bottom-left",
        )
        # Extension after the corner to the left
        if self.len_left > self.corner_width:
            draw_rect(
                pen,
                b.xmid - self.len_left - dc.stroke / 2,
                dc.descent + self.tail_offset,
                b.xmid - self.corner_width,
                dc.descent + self.tail_offset + dc.stroke,
            )
        # Accent dot
        draw_rect(
            pen,
            b.xmid - self.dot_width - dc.stroke / 2,
            dc.accent - self.dot_width / 2 - dc.stroke / 2,
            b.xmid + dc.stroke / 2,
            dc.accent + dc.stroke / 2 + self.dot_width / 2,
        )
