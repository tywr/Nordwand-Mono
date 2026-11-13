import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase.diagonal import DiagonalUppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseVGlyph(DiagonalUppercaseGlyph):
    name = "uppercase_v"
    unicode = "0x56"
    offset = 0

    def draw(self, pen, dc):
        b = self.body(dc)
        s = self.branch_stroke_ratio * dc.stroke_x
        ov = self.overlap * s
        lsh = self.section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        _, delta = draw_parallelogramm(
            gpen,
            s,
            b.xmid - ov,
            0,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            gpen,
            s,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + delta, b.y2), (b.x2 - delta, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
