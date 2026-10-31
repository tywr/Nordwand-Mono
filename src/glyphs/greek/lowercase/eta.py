from draw.rect import draw_rect
from glyphs.lowercase.square.n import LowercaseNGlyph


class GreekLowercaseEtaGlyph(LowercaseNGlyph):
    """The n with its right stem going down to the descender"""

    name = "greek_lowercase_eta"
    unicode = "0x3B7"

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, overshoot_top=True, width_ratio=self.width_ratio
        )
        draw_rect(pen, b.x2 - dc.stroke_x, dc.descent, b.x2, dc.stroke_y)
