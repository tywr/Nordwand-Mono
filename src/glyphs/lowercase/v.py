import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 0.96
    overlap = 0.33
    lower_section_height = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        ov = self.overlap * dc.stroke_x
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.0)
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        theta, delta = draw_parallelogramm(
            gpen, dc.stroke_x, dc.stroke_y, b.xmid - ov, 0, b.x2, b.y2, delta=sx
        )
        draw_parallelogramm(
            gpen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
            delta=sx,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + sx, b.y2), (b.x2 - sx, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
