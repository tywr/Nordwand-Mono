import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase.diagonal import DiagonalUppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseXGlyph(DiagonalUppercaseGlyph):
    name = "uppercase_x"
    unicode = "0x58"
    offset = 0

    def draw(self, pen, dc):
        b = self.body(dc)
        s = self.branch_stroke_ratio * dc.stroke_x
        ish = self.section_height * dc.stroke_y

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
