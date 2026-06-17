import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.corner import draw_corner
from draw.rect import draw_rect


class LowercaseAGlyph(Glyph):
    name = "lowercase_a"
    unicode = "0x61"
    offset = -12
    accent_x_offset = 16
    mid_height = 0.525
    width_ratio = 0.95

    taper = 0.4

    # bot_hx_ratio = 2.2
    bot_hx_ratio = 1
    bot_hy_ratio = 1
    left_cap_hx_ratio = 1.0
    left_cap_hy_ratio = 0.65
    cap_hx_ratio = 1.25
    cap_hy_ratio = 1
    cap_start_height = 0.69
    cap_height = 0.74
    cap_offset = 0.015
    thinning = 1
    upper_bowl_mid = 0.5
    cap_stroke_x_ratio = 1.01
    cap_stroke_y_ratio = 1.00
    ending_thickness = 0.7
    overshoot_top = True
    overshoot_bottom = True

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="x_height",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        ec = self.extra_cut(dc)
        sx = dc.stroke_x
        csx, csy = (
            self.cap_stroke_x_ratio * dc.stroke_x,
            self.cap_stroke_y_ratio * dc.stroke_y,
        )
        dx = csx - dc.stroke_x
        ry = (self.mid_height * b.height + dc.stroke_alt / 2) / b.height
        ymid = b.y1 + self.mid_height * b.height
        xmu = b.x1 + self.upper_bowl_mid * b.width
        ycap = b.y1 + self.cap_start_height * b.height
        yl = ymid + dc.stroke_alt / 2
        hx, hy = b.hx, b.hy * ry
        bhx, bhy = self.bot_hx_ratio * b.hx, self.bot_hy_ratio * b.hy
        ycut = b.y1 + self.cap_height * b.height - ec
        xc = b.x1 + self.cap_offset * b.width
        chx = self.cap_hx_ratio * b.hx
        lchx = self.left_cap_hx_ratio * b.hx
        lchy = self.left_cap_hy_ratio * b.hy

        # Lower half half of the bowl
        draw_arch(
            pen,
            csx,
            csy,
            b.x1,
            b.y1,
            b.x2 + dx,
            yl,
            hx,
            hy,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        # Upper half of the bowl
        draw_corner(
            pen,
            csx,
            dc.stroke_alt,
            b.x1,
            (b.y1 + yl) / 2,
            xmu,
            yl,
            bhx,
            hy,
            orientation="top-right",
        )
        draw_rect(
            pen,
            xmu,
            yl - dc.stroke_alt,
            b.x2 - 0.5 * dc.stroke_x,
            yl,
        )

        # Cap
        xmid = (xc + b.x2) / 2
        draw_corner(
            pen, sx, csy, b.x2, ycap, xmid, b.y2, lchx, lchy, orientation="top-left"
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            csx * self.thinning,
            csy,
            xc,
            b.ymid,
            xmid,
            b.y2,
            chx,
            b.hy,
            orientation="top-right",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x1, b.ymid, b.xmid, ycut)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Stem
        draw_rect(
            pen,
            b.x2 - sx,
            0,
            b.x2,
            ycap,
        )
