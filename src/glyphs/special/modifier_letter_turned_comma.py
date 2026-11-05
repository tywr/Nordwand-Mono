from draw.polygon import draw_polygon
from glyphs.special.modifier_letter_apostrophe import ModifierLetterApostropheGlyph


class ModifierLetterTurnedCommaGlyph(ModifierLetterApostropheGlyph):
    """ʻokina: the modifier apostrophe turned by 180°."""

    name = "modifier_letter_turned_comma"
    unicode = "0x02BB"

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = self.height_ratio * b.height
        s, st = dc.stroke_x, dc.stroke_x * self.taper
        d = self.delta * b.width
        draw_polygon(
            pen,
            points=[
                (b.xmid - s / 2 + d, dc.ascent),
                (b.xmid + s / 2 + d, dc.ascent),
                (b.xmid + st / 2, dc.ascent - h),
                (b.xmid - st / 2, dc.ascent - h),
            ],
        )
