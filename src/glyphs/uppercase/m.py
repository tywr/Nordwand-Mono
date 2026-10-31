import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseMGlyph(UppercaseGlyph):
    name = "uppercase_m"
    unicode = "0x4D"
    offset = 0
    overlap = 0.25
    mid_overlap = 0.6
    depth = 0.6
    inner_thickness_ratio = 2.4
    inner_height = 0.2
    width_ratio = 1.16
    inner_stroke_ratio = 1
    upper_section_height = 1.0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_uppercase,
        )
        tsx = dc.stroke_x * self.stroke_x_ratio
        sx = max(0, 0.6 * (tsx - 90)) + min(90, tsx)
        si = sx * self.inner_stroke_ratio
        ov = sx * self.overlap
        delta = self.inner_thickness_ratio * sx
        yi = b.y1 + self.inner_height * b.height
        # Ink trap tips, upper_section_height below the top
        ush = self.upper_section_height * dc.stroke_y
        yik = b.y2 - ush

        # Vertical stems

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_rect(gpen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(gpen, b.x2 - sx, b.y1, b.x2, b.y2)
        # Diagonals, from their top corner `ov` inside the stems down to the
        # middle; shared with the ink traps below so both stay in sync
        bottom = yi - delta / 2
        left_top, left_bottom = b.x1 + sx - ov, b.xmid + sx * self.mid_overlap
        right_top, right_bottom = b.x2 - sx + ov, b.xmid - sx * self.mid_overlap
        _, dl = draw_parallelogramm(
            gpen,
            si,
            left_top,
            b.y2,
            left_bottom,
            bottom,
            direction="bottom-right",
        )
        _, dr = draw_parallelogramm(
            gpen,
            si,
            right_top,
            b.y2,
            right_bottom,
            bottom,
            direction="bottom-left",
        )
        draw_rect(
            gpen,
            b.xmid,
            yi,
            b.xmid,
            yi + delta / 2,
        )
        draw_rect(
            gpen,
            b.x1 + sx,
            b.y2 - delta,
            b.x1 + sx,
            b.y2,
        )
        draw_rect(
            gpen,
            b.x2 - sx,
            b.y2 - delta,
            b.x2 - sx,
            b.y2,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 + sx,
            yi - delta / 2,
            b.x2 - sx,
            yi,
        )
        # Ink traps: the diagonals' lower edges run from their top corner
        # inside the stems down to the bottom of the parallelograms. Where
        # an edge leaves its stem, the trap carves along the edge's extension
        # up to yik, tapering back into the stem halfway down to the baseline.
        for x_stem, x_top, x_bottom in (
            (b.x1 + sx, left_top, left_bottom - dl),
            (b.x2 - sx, right_top, right_bottom + dr),
        ):

            def x_at(y):
                return x_top + (x_bottom - x_top) * (y - b.y2) / (bottom - b.y2)

            # Height where the lower edge crosses the stem's inner side
            yj = b.y2 + (x_stem - x_top) * (bottom - b.y2) / (x_bottom - x_top)
            if yik > yj:
                draw_polygon(
                    cut_glyph.getPen(),
                    points=[
                        (x_stem, yj),
                        (x_at(yik), yik),
                        (x_stem, (b.y1 + yj) / 2),
                    ],
                )

        # As in the V, cut between the diagonals' upper edges so the middle
        # vertex keeps a solid section of ush above its flat bottom at yi
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (left_top + dl, b.y2),
                (right_top - dr, b.y2),
                (b.xmid, yi + ush),
            ],
        )

        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
