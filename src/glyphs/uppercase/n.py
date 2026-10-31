import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseNGlyph(UppercaseGlyph):
    name = "uppercase_n"
    unicode = "0x4E"
    offset = 0
    middle_stroke_ratio = 1.0
    overlap = 0.25
    width_ratio = 1.04
    section_height = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
            min_margin=dc.min_margin_uppercase,
        )
        sx = dc.stroke_x * self.stroke_x_ratio
        ov = sx * self.overlap
        sh = self.section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()

        # Vertical stems
        draw_rect(gpen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(gpen, b.x2 - sx, b.y1, b.x2, b.y2)

        # Diagonal, from its bottom corner `ov` inside the right stem to its
        # top corner `ov` inside the left one
        x_bottom, x_top = b.x2 - sx + ov, b.x1 + sx - ov
        _, delta = draw_parallelogramm(
            gpen,
            sx * self.middle_stroke_ratio,
            x_bottom,
            b.y1,
            x_top,
            b.y2,
            direction="top-left",
        )

        # Ink traps, as in the M. Each edge of the diagonal leaves a stem at
        # an acute angle: the lower edge leaves the left stem under the top,
        # the upper edge leaves the right stem above the baseline. Where it
        # does, the trap carves along the edge's extension into the stem up
        # to `sh` from the stem's end, tapering back halfway to the other end.
        cut_glyph = ufoLib2.objects.Glyph()
        for x_stem, edge, y_end, y_far in (
            # Lower edge, from the top-left corner down to the bottom-left one
            (b.x1 + sx, ((x_top, b.y2), (x_bottom - delta, b.y1)), b.y2, b.y1),
            # Upper edge, from the bottom-right corner up to the top-right one
            (b.x2 - sx, ((x_bottom, b.y1), (x_top + delta, b.y2)), b.y1, b.y2),
        ):
            (xa, ya), (xb, yb) = edge

            def x_at(y):
                return xa + (xb - xa) * (y - ya) / (yb - ya)

            # Height where the edge crosses the stem's inner side
            yj = ya + (x_stem - xa) * (yb - ya) / (xb - xa)
            # Trap tip, `sh` from the stem's end on the diagonal's side
            y_tip = y_end - sh if y_end > y_far else y_end + sh
            if (y_tip - yj) * (y_end - y_far) > 0:
                draw_polygon(
                    cut_glyph.getPen(),
                    points=[
                        (x_stem, yj),
                        (x_at(y_tip), y_tip),
                        (x_stem, (y_far + yj) / 2),
                    ],
                )

        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
