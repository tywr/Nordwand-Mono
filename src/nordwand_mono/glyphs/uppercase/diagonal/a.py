import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs.uppercase.diagonal import DiagonalUppercaseGlyph
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.polygon import draw_polygon


class UppercaseAGlyph(DiagonalUppercaseGlyph):
    name = "uppercase_a"
    unicode = "0x41"
    offset = 0
    bar_height = 0.39
    bar_shift_coef = 0.2

    def draw_branches(self, pen, dc, b):
        """Both branches meeting at the apex, with the crotch cut below it.
        Returns the overlap at the apex and the branches' horizontal width."""
        sx, sy = self.get_strokes(dc)
        s = self.branch_stroke_ratio * sx
        ov = self.overlap * s
        ush = self.section_height * sy

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        # Left branch
        draw_parallelogramm(
            gpen, s, b.x2, b.y1, b.xmid - ov, b.y2, direction="top-left"
        )
        # Right branch
        _, delta = draw_parallelogramm(gpen, s, b.x1, b.y1, b.xmid + ov, b.y2)

        # As in the V, cut where the branches cross so the apex keeps a fixed
        # depth above the inner crotch instead of thickening
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + delta, b.y1), (b.x2 - delta, b.y1), (b.xmid, b.y2 - ush)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
        return ov, delta

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.get_strokes(dc)
        yo = self.bar_shift_coef * (dc.stroke_x - dc.default_stroke)
        hb = self.bar_height * b.height + yo
        ov, delta = self.draw_branches(pen, dc, b)

        # Crossbar: ends follow the branch centerlines, so it always
        # reaches into both strokes and never pokes out of them
        def lerp(x0, x1, y):
            return x0 + (x1 - x0) * (y - b.y1) / (b.y2 - b.y1)

        def left(y):
            return lerp(b.x1 + delta / 2, b.xmid + ov - delta / 2, y)

        def right(y):
            return lerp(b.x2 - delta / 2, b.xmid - ov + delta / 2, y)

        draw_polygon(
            pen,
            points=[
                (left(hb - sy), hb - sy),
                (right(hb - sy), hb - sy),
                (right(hb), hb),
                (left(hb), hb),
            ],
        )
