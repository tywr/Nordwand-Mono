from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.square_corner import draw_square_corner


class LowercaseLGlyph(Glyph):
    name = "lowercase_l"
    unicode = "0x6C"
    offset = -12
    width_ratio = 1.16
    mid_ratio = 0.45
    expand_factor = 0.5

    def stem_center(self, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio, expand_factor=self.expand_factor
        )
        return b.x1 + self.mid_ratio * b.width

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        ym4 = b.y1 + b.height / 4
        xmid = self.stem_center(dc)

        # Stem
        draw_rect(pen, xmid - dc.stroke_x / 2, ym4, xmid + dc.stroke_x / 2, dc.ascent)

        # Footer
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xmid - dc.stroke_x / 2,
            ym4,
            b.x2,
            b.y1,
            gx=dc.square_corner_gx,
            gy=dc.square_corner_gy,
            orientation="bottom-right",
        )

        # Left cap
        draw_rect(
            pen,
            b.x1,
            dc.ascent - dc.stroke_y,
            xmid,
            dc.ascent,
        )
