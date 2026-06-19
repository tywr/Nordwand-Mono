import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseWGlyph(Glyph):
    name = "lowercase_w"
    unicode = "0x77"
    offset = 0
    overlap = 1
    outer_branch_ratio = 0.25
    inner_height = 1
    width_ratio = 1.27
    stroke_ratio = 1.1
    lower_section_height = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            # min_margin=dc.min_margin_lowercase,
        )
        tsx = dc.stroke_x * self.stroke_ratio
        sx = max(0, 0.9 * (tsx - dc.default_stroke)) + min(dc.default_stroke, tsx)
        ov = self.overlap * sx
        xi1 = b.x1 + self.outer_branch_ratio * b.width
        xi2 = b.x2 - self.outer_branch_ratio * b.width
        yi = b.y1 + self.inner_height * b.height
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm(
            gpen,
            0,
            0,
            b.x1,
            b.y2,
            xi1 + ov / 2,
            b.y1,
            delta=sx,
            direction="bottom-right",
        )
        draw_parallelogramm(
            gpen,
            0,
            0,
            b.x2,
            b.y2,
            xi2 - ov / 2,
            b.y1,
            delta=sx,
            direction="bottom-left",
        )
        draw_parallelogramm(
            gpen,
            0,
            0,
            xi1 - ov / 2,
            b.y1,
            b.xmid + sx / 2,
            yi,
            delta=sx,
            direction="top-right",
        )
        draw_parallelogramm(
            gpen,
            0,
            0,
            xi2 - ov / 2 + sx,
            b.y1,
            b.xmid - sx / 2,
            yi,
            delta=sx,
            direction="top-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.x1 + sx, b.y2),
                (b.xmid - sx / 2, b.y2),
                (xi1, lsh),
            ],
        )
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.xmid + sx / 2, b.y2),
                (b.x2 - sx, b.y2),
                (xi2, lsh),
            ],
        )
        draw_polygon(
            cut_glyph.getPen(),
            points=[(xi1 + ov / 2, b.y1), (xi2 - ov / 2, b.y1), (b.xmid, b.y2 - lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
