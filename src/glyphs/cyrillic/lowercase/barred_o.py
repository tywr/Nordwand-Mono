from draw.rect import draw_rect
from glyphs.lowercase.round.o import LowercaseOGlyph


class CyrillicLowercaseBarredOGlyph(LowercaseOGlyph):
    """o with the bar of θ across its middle."""

    name = "cyrillic_lowercase_barred_o"
    unicode = "0x04E9"

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
        )
        draw_rect(
            pen,
            b.x1 + dc.stroke_x / 2,
            b.ymid - dc.stroke_alt / 2,
            b.x2 - dc.stroke_x / 2,
            b.ymid + dc.stroke_alt / 2,
        )
