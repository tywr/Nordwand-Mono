import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon
from draw.rect import draw_rect
from glyphs.uppercase import UppercaseGlyph


class UppercaseAeGlyph(UppercaseGlyph):
    # Placeholder: plots the same as uppercase 'A' for the moment.
    name = "uppercase_ae"
    unicode = "0xC6"
    offset = 0
    bar_height = 0.35
    overlap = 0.25
    stroke_x_ratio = 1.02
    width_ratio = 1.2
    mid_ratio = 0.52
    xmid_ratio = 0.55
    branch_stroke_ratio = 0.99
    upper_section_height = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        sx = max(0, 0.8 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)

        ov = self.overlap * sx
        hb = self.bar_height * b.height
        ymid = b.y1 + self.mid_ratio * b.height
        xmid = b.x1 + self.xmid_ratio * b.width
        ush = self.upper_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        # Left branch
        s = self.branch_stroke_ratio * sx
        _, delta = draw_parallelogramm(gpen, s, b.x1, b.y1, xmid - ov, b.y2)
        draw_rect(gpen, xmid - sx / 2, b.y1, xmid + sx / 2, b.y2)

        # As in the A, cut between the branch and the stem so the apex keeps a
        # fixed depth above the inner crotch instead of thickening
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.x1 + delta, b.y1),
                (xmid - sx / 2, b.y1),
                (xmid - sx / 2, b.y2 - ush),
            ],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # Crossbar: the left end follows the branch centerline, so it always
        # reaches into the stroke and never pokes out of it
        def left(y):
            x0, x1 = b.x1 + delta / 2, xmid - ov - delta / 2
            return x0 + (x1 - x0) * (y - b.y1) / (b.y2 - b.y1)

        draw_polygon(
            pen,
            points=[(left(hb - sy), hb - sy), (xmid, hb - sy), (xmid, hb), (left(hb), hb)],
        )

        # Vertical stem
        draw_rect(pen, xmid, ymid - sy / 2, b.x2, ymid + sy / 2)

        # Top bar
        draw_rect(pen, xmid, b.y2 - sy, b.x2, b.y2)

        # Middle bar
        draw_rect(
            pen,
            xmid,
            b.y1,
            b.x2,
            b.y1 + sy,
        )
