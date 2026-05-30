import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.corner import draw_corner
from draw.rect import draw_rect


class AeGlyph(Glyph):
    # Placeholder: plots the same as lowercase 'a' for the moment.
    name = "ae"
    unicode = "0xE6"
    offset = 0
    mid_height = 0.52
    width_ratio = 1.16
    taper = 0.3
    hx_ratio = 0.5
    hy_ratio = 1
    cap_hx_ratio = 0.7
    cap_hy_ratio = 1
    cap_height = 0.7
    cap_offset = 0.02
    thinning = 1
    cap_stroke_x_ratio = 1.01
    cap_stroke_y_ratio = 1.00
    ending_thickness = 0.8
    tail_offset = 0.00
    tail_height = 0.31

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        sx = max(0, 0.7 * (dc.stroke_x - 90)) + min(90, dc.stroke_x)
        csx, csy = (
            self.cap_stroke_x_ratio * dc.stroke_x,
            self.cap_stroke_y_ratio * dc.stroke_y,
        )
        dx = csx - sx
        ry = (self.mid_height * b.height + dc.stroke_alt / 2) / b.height
        ymid = b.y1 + self.mid_height * b.height
        yl = ymid + dc.stroke_alt / 2
        hx, hy = b.hx * self.hx_ratio, b.hy * ry * self.hy_ratio
        ycut = b.y1 + self.cap_height * b.height
        xc = b.x1 + self.cap_offset * b.width
        chx = self.cap_hx_ratio * b.hx
        xt = b.x2 + self.tail_offset * b.width
        yo = b.y1 + self.tail_height * b.height

        ax2, axmid = b.xmid + sx / 2, (b.x1 + b.xmid + sx / 2) / 2
        ex1, exmid = b.xmid - sx / 2, (b.x2 + b.xmid - sx / 2) / 2

        # Lower half half of the bowl
        draw_arch(
            pen,
            csx,
            csy,
            b.x1,
            b.y1,
            ax2 + dx,
            yl,
            hx,
            hy,
            taper=self.taper,
            side="right",
            cut="top",
        )
        draw_rect(pen, b.xmid - sx / 2, (yl + b.y1) / 2, b.xmid, b.ymid)

        # Upper half of the bowl
        draw_corner(
            pen,
            csx,
            dc.stroke_alt,
            b.x1,
            (b.y1 + yl) / 2,
            axmid,
            yl,
            hx,
            hy,
            orientation="top-right",
        )
        draw_rect(
            pen,
            axmid,
            yl - dc.stroke_alt,
            ax2,
            yl,
        )

        # Cap
        xmid = (xc + ax2) / 2
        draw_corner(
            pen, sx, csy, ax2, b.ymid, xmid, b.y2, chx, b.hy, orientation="top-left"
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            sx * self.thinning,
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
        draw_rect(cut_glyph.getPen(), b.x1, b.ymid, axmid, ycut)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Top-right corner
        draw_corner(
            pen,
            sx,
            sy,
            b.x2 - dc.h_overshoot,
            b.ymid,
            exmid,
            b.y2,
            chx,
            hy,
            orientation="top-left",
        )
        draw_corner(
            pen,
            sx,
            sy,
            b.xmid - sx / 2,
            b.ymid,
            exmid,
            b.y2,
            chx,
            hy,
            orientation="top-right",
        )
        draw_corner(
            pen,
            sx,
            sy,
            b.xmid - sx / 2,
            b.ymid,
            exmid,
            b.y1,
            chx,
            hy,
            orientation="bottom-right",
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            sx * self.thinning,
            sy,
            b.x2 - dc.h_overshoot,
            b.ymid,
            exmid,
            b.y1,
            chx,
            b.hy,
            orientation="bottom-left",
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yo,
            b.xmid + b.width,
            b.ymid,
        )
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        draw_rect(
            pen,
            b.xmid,
            ymid,
            b.x2 - dc.h_overshoot - sx / 2,
            ymid + dc.stroke_alt / 2,
        )
        draw_rect(
            pen,
            b.xmid,
            ymid - dc.stroke_alt / 2,
            b.x2 - dc.h_overshoot,
            max(ymid, b.ymid),
        )
