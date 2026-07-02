from glyphs import Glyph
from draw.arch import draw_arch


class LowercaseX2Glyph(Glyph):
    name = "lowercase_x_2"
    font_feature = {"cv06": 1}
    default_italic = True
    unicode = "0x78"
    offset = 0
    width_ratio = 1.26
    stroke_ratio = 1.1
    overlap = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        sx = dc.stroke_x
        ov = self.overlap * sx
        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1 - b.width / 2,
            b.y1,
            b.xmid + ov,
            b.y2,
            b.hx,
            b.hy,
            cut="left",
            side="right",
            taper=0.75,
        )
        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov,
            b.y1,
            b.x2 + b.width / 2,
            b.y2,
            b.hx,
            b.hy,
            cut="right",
            side="left",
            taper=0.75,
        )
