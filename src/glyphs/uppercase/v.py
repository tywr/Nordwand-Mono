import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseVGlyph(UppercaseGlyph):
    name = "uppercase_v"
    unicode = "0x56"
    offset = 0
    overlap = 0.5
    width_ratio = 1.28
    lower_section_height = 1.5
    branch_stroke_ratio = 0.988  # Perpendicular thickness of the branches

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        s = self.branch_stroke_ratio * dc.stroke_x
        ov = self.overlap * s
        lsh = self.lower_section_height * dc.stroke_y

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



