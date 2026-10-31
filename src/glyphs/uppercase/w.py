import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseWGlyph(UppercaseGlyph):
    name = "uppercase_w"
    unicode = "0x57"
    offset = 0
    overlap = 1
    outer_branch_ratio = 0.265
    inner_height = 1
    width_ratio = 1.27
    stroke_ratio = 0.99  # Perpendicular thickness of the outer branches
    inner_stroke_ratio = 0.984  # And of the inner ones
    lower_section_height = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            offset=self.offset,
            width_ratio=self.width_ratio,
            # min_margin=dc.min_margin_lowercase,
        )
        lsh = self.lower_section_height * dc.stroke_y
        so = self.stroke_ratio * dc.stroke_x
        si = self.inner_stroke_ratio * dc.stroke_x
        ov = self.overlap * so
        xi1 = b.x1 + self.outer_branch_ratio * b.width
        xi2 = b.x2 - self.outer_branch_ratio * b.width
        yi = b.y1 + self.inner_height * b.height

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        # Outer branches; `do` is their horizontal width
        _, do = draw_parallelogramm(
            gpen, so, b.x1, b.y2, xi1 + ov / 2, b.y1, direction="bottom-right"
        )
        draw_parallelogramm(
            gpen, so, b.x2, b.y2, xi2 - ov / 2, b.y1, direction="bottom-left"
        )
        # Inner branches, their feet starting where the outer ones do and
        # meeting at the middle; `di` is their horizontal width
        _, di = draw_parallelogramm(
            gpen, si, xi1 + ov / 2 - do, b.y1, b.xmid + do / 2, yi, direction="top-right"
        )
        draw_parallelogramm(
            gpen, si, xi2 - ov / 2 + do, b.y1, b.xmid - do / 2, yi, direction="top-left"
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.x1 + do, b.y2),
                (b.xmid + do / 2 - di, b.y2),
                (xi1, lsh),
            ],
        )
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.xmid - do / 2 + di, b.y2),
                (b.x2 - do, b.y2),
                (xi2, lsh),
            ],
        )
        draw_polygon(
            cut_glyph.getPen(),
            points=[(xi1 + ov / 2, b.y1), (xi2 - ov / 2, b.y1), (b.xmid, b.y2 - lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
