import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.loop import draw_loop
from draw.rect import draw_rect


class LowercaseAGlyph(Glyph):
    name = "lowercase_a"
    unicode = "0x61"
    offset = -12
    accent_x_offset = 16
    mid_height = 0.52
    width_ratio = 0.99

    taper = 0.65

    top_loop_ratio = 0.66
    cap_height = 0.74
    cap_offset = 0.04
    thinning = 1
    bottom_loop_xmid = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="x_height",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x, dc.stroke_y
        ymid = b.y1 + self.mid_height * b.height
        yl = ymid + dc.stroke_alt / 2
        ycut = b.y1 + self.cap_height * b.height - ec

        # Bottom loop variables
        xbmid = b.x1 + self.bottom_loop_xmid * b.width
        xb2 = 2 * xbmid - b.x1
        ybmid = ymid + dc.stroke_alt / 2

        # Top loop variables
        xt1 = b.x1 + self.cap_offset * b.width
        xt2 = 2 * b.xmid - xt1
        yt1 = b.y2 - self.top_loop_ratio * b.height

        # Lower half half of the bottom loop
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ybmid,
            b.hx,
            b.hy * (ybmid - b.y1) / b.height,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        # Upper half of the bottom loop
        draw_loop(
            pen,
            sx,
            dc.stroke_alt,
            b.x1,
            b.y1,
            xb2,
            ybmid,
            b.hx * (xb2 - b.x1) / b.width,
            b.hy * (ybmid - b.y1) / b.height,
            quarter="top-left",
        )
        draw_rect(
            pen,
            xbmid,
            yl - dc.stroke_alt,
            b.x2 - sx / 2,
            yl,
        )

        # Top loop
        loop_glyph = ufoLib2.objects.Glyph()
        draw_loop(
            loop_glyph.getPen(),
            sx,
            sy,
            b.x1,
            yt1,
            b.x2,
            b.y2,
            b.hx,
            b.hy * (b.y2 - yt1) / b.height,
            quarter="top-right",
        )
        draw_loop(
            loop_glyph.getPen(),
            sx * self.thinning,
            sy,
            xt1,
            yt1,
            xt2,
            b.y2,
            b.hx * (xt2 - xt1) / b.width,
            b.hy * (b.y2 - yt1) / b.height,
            quarter="top-left",
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
            (yt1 + b.y2) / 2,
        )
