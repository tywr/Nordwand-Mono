from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.polygon import draw_polygon


class CommaGlyph(Glyph):
    name = "comma"
    unicode = "0x2C"
    offset = 0
    width_ratio = 1
    height_ratio = 0.75
    vertical_offset = 0.2
    foot_offset = 0.15
    taper = 0.66
    stroke_ratio = 1.2

    def points(self, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sx, _ = self.get_strokes(dc)
        oy = self.vertical_offset * b.height
        fx = self.foot_offset * b.width

        return [
            (b.xmid - sx / 2, oy),
            (b.xmid + sx / 2, oy),
            (b.xmid + self.taper * sx / 2 - fx, dc.descent),
            (b.xmid - sx / 2 - fx, dc.descent),
        ]

    def draw(self, pen, dc):
        draw_polygon(pen, points=self.points(dc))
