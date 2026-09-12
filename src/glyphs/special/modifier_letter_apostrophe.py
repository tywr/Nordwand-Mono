from glyphs import Glyph
from draw.polygon import draw_polygon


class ModifierLetterApostropheGlyph(Glyph):
    name = "modifier_letter_apostrophe"
    unicode = "0x02BC"
    offset = 0
    width_ratio = 1
    height_ratio = 0.55
    taper = 1.5
    delta = 0.22

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
                (b.xmid + s / 2 - d, dc.ascent - h),
                (b.xmid - s / 2 - d, dc.ascent - h),
                (b.xmid - st / 2, dc.ascent),
                (b.xmid + st / 2, dc.ascent),
            ],
        )
