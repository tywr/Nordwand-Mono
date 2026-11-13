import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    offset = 0
    width_ratio = 1.1
    stroke_ratio = 1
    inner_section_height = 0.85

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        ish = self.inner_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        _, delta = draw_parallelogramm(gpen, s, b.x1, b.y1, b.x2, b.y2)
        draw_parallelogramm(gpen, s, b.x2, b.y1, b.x1, b.y2, direction="top-left")
        cut_glyph = ufoLib2.objects.Glyph()
        cpen = cut_glyph.getPen()
        draw_polygon(
            cpen,
            points=[(b.x1 + delta, b.y2), (b.x2 - delta, b.y2), (b.xmid, b.ymid + ish)],
        )
        draw_polygon(
            cpen,
            points=[(b.x2 - delta, b.y1), (b.x1 + delta, b.y1), (b.xmid, b.ymid - ish)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
