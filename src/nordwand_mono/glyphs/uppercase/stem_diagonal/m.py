import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs.uppercase.stem_diagonal import StemDiagonalUppercaseGlyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.polygon import draw_polygon


class UppercaseMGlyph(StemDiagonalUppercaseGlyph):
    name = "uppercase_m"
    unicode = "0x4D"
    offset = 0
    mid_overlap = 0.3
    inner_thickness_ratio = 2.4
    inner_height = 0.2
    width_ratio = 1.16
    stroke_dampening = 0.8

    def draw(self, pen, dc):
        b = self.body(dc)
        sx = max(0, self.stroke_dampening * (dc.stroke_x - dc.default_stroke)) + min(
            dc.default_stroke, dc.stroke_x
        )
        si = self.inner_stroke(sx, dc)
        ov = sx * self.overlap
        ovm = sx * self.mid_overlap
        delta = self.inner_thickness_ratio * sx
        yi = b.y1 + self.inner_height * b.height
        # Ink trap tips, section_height below the top
        ush = self.section_height * dc.stroke_y
        yik = b.y2 - ush

        # Vertical stems

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_rect(gpen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(gpen, b.x2 - sx, b.y1, b.x2, b.y2)

        left_top, left_bottom = b.x1 + sx - ov, b.xmid + ovm
        right_top, right_bottom = b.x2 - sx + ov, b.xmid - ovm
        _, dl = draw_parallelogramm(
            gpen,
            si,
            left_top,
            b.y2,
            left_bottom,
            yi,
            direction="bottom-right",
        )
        _, dr = draw_parallelogramm(
            gpen,
            si,
            right_top,
            b.y2,
            right_bottom,
            yi,
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

        # Ink traps: the diagonals' lower edges run from their top corner
        # inside the stems down to their flat bottom at yi. Where
        # an edge leaves its stem, the trap carves along the edge's extension
        # up to yik, tapering back into the stem halfway down to the baseline.
        for x_stem, x_top, x_bottom in (
            (b.x1 + sx, left_top, left_bottom - dl),
            (b.x2 - sx, right_top, right_bottom + dr),
        ):

            def x_at(y):
                return x_top + (x_bottom - x_top) * (y - b.y2) / (yi - b.y2)

            # Height where the lower edge crosses the stem's inner side
            yj = b.y2 + (x_stem - x_top) * (yi - b.y2) / (x_bottom - x_top)
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
