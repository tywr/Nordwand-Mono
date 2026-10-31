from math import cos, radians, tan
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseWGlyph(Glyph):
    name = "lowercase_w"
    unicode = "0x77"
    offset = 0
    overlap = 0.5
    outer_angle = 7.5
    inner_height = 1
    width_ratio = 1.27
    stroke_ratio = 1
    inner_stroke_ratio = 0.85
    thin_boost = 0.1
    lower_section_height = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        lsh = self.lower_section_height * dc.stroke_y
        boost = self.thin_boost * max(0, dc.default_stroke - dc.stroke_x)
        sx = max(0, 0.8 * (dc.stroke_x - dc.default_stroke)) + min(
            dc.default_stroke, dc.stroke_x
        )
        so = self.stroke_ratio * sx
        si = self.inner_stroke_ratio * sx + boost
        # Outer feet placed so the branches' edges keep outer_angle in every
        # weight: their run is the slant over the height plus the horizontal
        # width of a stroke so at that angle
        a = radians(self.outer_angle)
        run = b.height * tan(a) + so / cos(a)
        xi1 = b.x1 + run
        xi2 = b.x2 - run
        yi = b.y1 + self.inner_height * b.height

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()

        # Outer branches; `do` is their horizontal width
        _, do = draw_parallelogramm(
            gpen, so, b.x1, b.y2, xi1, b.y1, direction="bottom-right"
        )
        ov = self.overlap * do
        draw_parallelogramm(gpen, so, b.x2, b.y2, xi2, b.y1, direction="bottom-left")

        # Inner branches, their feet starting where the outer ones do and
        # meeting at the middle; `di` is their horizontal width
        _, di = draw_parallelogramm(
            gpen,
            si,
            xi1 - ov,
            b.y1,
            b.xmid + ov / 2,
            yi,
            direction="top-right",
        )
        draw_parallelogramm(
            gpen, si, xi2 + ov, b.y1, b.xmid - ov / 2, yi, direction="top-left"
        )

        def x_at(p, q, y):
            """x of the line through p and q at height y."""
            return p[0] + (q[0] - p[0]) * (y - p[1]) / (q[1] - p[1])

        # Inner edges of the strokes, as (bottom, top) points
        outer_l = ((xi1, b.y1), (b.x1 + do, b.y2))
        outer_r = ((xi2, b.y1), (b.x2 - do, b.y2))
        inner_l_out = ((xi1 - ov, b.y1), (b.xmid + ov / 2 - di, yi))
        inner_r_out = ((xi2 + ov, b.y1), (b.xmid - ov / 2 + di, yi))
        # The feet's inner ends, whichever stroke reaches further in
        foot_l = max(xi1, xi1 - ov + di)
        foot_r = min(xi2, xi2 + ov - di)

        cut_glyph = ufoLib2.objects.Glyph()
        # Lower counters, as in the V: their tips sit lsh above the baseline,
        # halfway between the two edges they cut
        for outer, inner in ((outer_l, inner_l_out), (outer_r, inner_r_out)):
            draw_polygon(
                cut_glyph.getPen(),
                points=[
                    (x_at(*outer, b.y2), b.y2),
                    (x_at(*inner, b.y2), b.y2),
                    ((x_at(*outer, lsh) + x_at(*inner, lsh)) / 2, lsh),
                ],
            )
        # Middle counter, its tip lsh below the top of the inner branches
        draw_polygon(
            cut_glyph.getPen(),
            points=[(foot_l, b.y1), (foot_r, b.y1), (b.xmid, yi - lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
