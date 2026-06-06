import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.corner import draw_corner
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercaseGGlyph(SingleStoryLowercaseGlyph):
    name = "lowercase_g"
    unicode = "0x67"
    offset = -10

    hy_ratio = 0.92
    tail_offset = 0
    tail_stroke_x_ratio = 0.96
    tail_stroke_y_ratio = 1.01
    tail_hx_ratio = 1
    tail_hy_ratio = 0.7
    tail_offset = 0.15
    cut_ratio = 0.265
    tail_offset = 0.04
    y1_offset = 0.065

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
        )
        hy = self.hy_ratio * b.hy
        bsx, bsy = (
            self.bowl_stroke_x_ratio * dc.stroke_x,
            self.bowl_stroke_y_ratio * dc.stroke_y,
        )
        tsx, tsy = (
            self.tail_stroke_x_ratio * dc.stroke_x,
            self.tail_stroke_y_ratio * dc.stroke_y,
        )
        thx, thy = (
            self.tail_hx_ratio * dc.hx,
            self.tail_hy_ratio * dc.hy,
        )
        y1 = b.y1 + self.y1_offset * b.height


        xt = b.x1 + self.tail_offset * b.width

        # Bowl (open on the right, mirrored from b)
        draw_arch(
            pen,
            bsx,
            bsy,
            b.x1,
            y1,
            b.x2,
            b.y2,
            b.hx,
            hy,
            taper=dc.taper * self.taper,
            side="right",
        )

        # Right stem with gap at baseline and dent inset
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.x_height)

        # Corner curving down-left into the descender
        draw_corner(
            pen,
            dc.stroke_x,
            tsy,
            b.x2,
            0,
            b.xmid,
            dc.descent - dc.v_overshoot,
            thx,
            thy,
            orientation="bottom-left",
        )

        glyph = ufoLib2.objects.Glyph()
        draw_corner(
            glyph.getPen(),
            tsx,
            tsy,
            xt,
            0,
            b.xmid,
            dc.descent - dc.v_overshoot,
            b.hx,
            b.hy,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            dc.descent - dc.v_overshoot + b.height * self.cut_ratio,
            b.xmid,
            b.ymid,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
