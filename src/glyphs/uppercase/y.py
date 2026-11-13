import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm, parallelogramm_delta
from draw.polygon import draw_polygon
from draw.rect import draw_rect


class UppercaseYGlyph(UppercaseGlyph):
    name = "uppercase_y"
    unicode = "0x59"
    offset = 0
    width_ratio = 1.22
    junction_ratio = 0.4
    branch_stroke_ratio = 0.9
    inner_section_height = 1
    height = "cap"

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height=self.height
        )
        sx = dc.stroke_x * self.stroke_x_ratio

        yj = b.x1 + self.junction_ratio * b.height

        # Both feet centered on the stem, which they cover within a unit
        s = self.branch_stroke_ratio * sx
        d = parallelogramm_delta(s, b.xmid - sx / 2, yj, b.x2, b.y2)
        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        _, delta = draw_parallelogramm(gpen, s, b.xmid - d / 2, yj, b.x2, b.y2)
        draw_parallelogramm(
            gpen, s, b.xmid + d / 2, yj, b.x1, b.y2, direction="top-left"
        )
        # As in the V, the branches meet ish above the junction
        ish = self.inner_section_height * dc.stroke_y
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + delta, b.y2), (b.x2 - delta, b.y2), (b.xmid, yj + ish)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(pen, b.xmid - delta / 2, b.y1, b.xmid + delta / 2, yj)
