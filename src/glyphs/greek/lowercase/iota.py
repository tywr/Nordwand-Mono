from draw.rect import draw_rect
from draw.square_corner import draw_square_corner
from glyphs.lowercase.l import LowercaseLGlyph


class GreekLowercaseIotaGlyph(LowercaseLGlyph):
    """The l without its cap, its stem stopping at the x-height"""

    name = "greek_lowercase_iota"
    unicode = "0x3B9"

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        # Same footer as the l
        ym4 = b.y1 + b.height / 4
        xmid = self.stem_center(dc)

        # Stem
        draw_rect(
            pen, xmid - dc.stroke_x / 2, ym4, xmid + dc.stroke_x / 2, dc.x_height
        )

        # Footer
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xmid - dc.stroke_x / 2,
            ym4,
            b.x2,
            b.y1,
            orientation="bottom-right",
        )

        # Left cap
        draw_rect(
            pen,
            b.x1,
            dc.x_height - dc.stroke_y,
            xmid,
            dc.x_height,
        )
