import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.polygon import draw_polygon
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    offset = 34
    width_ratio = 1.00
    branch_ratio = 0.75
    mid_ratio = 0.58
    upper_branch_offset = 0.055
    stroke_ratio = 1.0
    branch_overlap = 0.8
    upper_branch_shift_ratio = 0.1
    cut_shift_ratio = -0.45

    def draw(self, pen, dc, draw_stem=True):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
        )
        sx, _ = self.get_strokes(dc)
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        xo = self.upper_branch_shift_ratio * max(dc.stroke_x - dc.default_stroke, 0)
        xc = self.cut_shift_ratio * max(dc.stroke_x - dc.default_stroke, 0)
        xtop = b.x2 - self.upper_branch_offset * b.width + xo
        ymid = b.y1 + self.mid_ratio * b.height
        s = self.stroke_ratio * dc.stroke_x

        # Left ascender stem
        if draw_stem:
            draw_rect(pen, b.x1, 0, b.x1 + sx, dc.ascent)

        glyph = ufoLib2.objects.Glyph()

        # Lower branch
        _, d = draw_parallelogramm(
            glyph.getPen(),
            s,
            xb,
            ymid,
            b.x2,
            b.y1,
            direction="bottom-right",
        )

        # Upper branch
        draw_parallelogramm(
            glyph.getPen(),
            0,
            xb,
            ymid,
            xtop,
            b.y2,
            overwrite_section=d,
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(cut_glyph.getPen(), [(b.x2, b.y1), (xtop, b.y2), (b.x1 + sx + d + xc, ymid)])
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
