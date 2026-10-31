import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 1.0
    overlap = 0.536
    lower_section_height = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * s
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm(
            gpen, s, b.xmid + ov, b.y1, b.x1, b.y2, direction="top-left"
        )
        _, delta = draw_parallelogramm(gpen, s, b.xmid - ov, b.y1, b.x2, b.y2)
        # As in the v, the branches meet lsh above the baseline
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + delta, b.y2), (b.x2 - delta, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # Tail continuing the right branch below the baseline: same edges'
        # slope, so the same stroke gives it the same horizontal width
        w2 = b.x2 - (b.xmid - ov)
        h2 = b.y2 - b.y1
        dx_tail = -(w2 - delta) * abs(dc.descent) / h2
        draw_parallelogramm(
            pen,
            s,
            b.xmid - ov + delta,
            b.y1,
            b.xmid - ov + dx_tail,
            dc.descent,
            direction="bottom-left",
        )
