import pathops
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.asymetric_arch import draw_asymetric_arch
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect


class LowercaseAGlyph(Glyph):
    name = "lowercase_a"
    unicode = "0x61"
    offset = -12
    accent_x_offset = 16
    mid_height = 0.52
    width_ratio = 0.99
    cap_handle_shift = -0.025

    taper = 0.65

    top_loop_ratio = 0.66
    cap_height = 0.74
    cap_offset = 0.045
    thinning = 1
    bottom_loop_xmid = 0.5
    # Height where the bottom of the bowl joins the stem, ratio of the body
    bowl_join_height = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="x_height",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        self.draw_a(pen, dc, b, dc.stroke_x, dc.stroke_y)

    def draw_a(self, pen, dc, b, sx, sy, stem=True, right_taper=None):
        """Bottom and top loops within `b`, without the stem; returns the
        bottom of the top loop."""
        ec = self.extra_cut(dc)
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

        # Lower half of the bottom loop: from the left side, where the upper
        # half starts, down to the bottom and up to the stem, joined higher
        ybl = (b.y1 + ybmid) / 2
        ytmid = b.y1 + self.top_loop_ratio * b.height / 2
        draw_asymetric_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ytmid,
            b.xmid,
            ybl,
            b.hx,
            b.hy * (ytmid - b.y1) / (b.height / 2),
            taper=right_taper if right_taper else self.taper * dc.taper,
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
            b.x2 - sx,
            yl,
        )

        # Top loop. Skia rather than booleanOperations, which drops the curve
        # of the arch in some heavier weights of the æ
        arch = pathops.Path()
        draw_arch(
            pathops.PathPen(arch),
            sx,
            sy,
            b.x1,
            yt1,
            b.x2,
            b.y2,
            b.hx,
            b.hy * (b.y2 - yt1) / b.height,
            handle_shift=self.cap_handle_shift,
            quarter="top-right",
            taper=right_taper if right_taper else 1,
        )
        loop = pathops.Path()
        draw_loop(
            pathops.PathPen(loop),
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
        cut = pathops.Path()
        draw_rect(pathops.PathPen(cut), b.x1, b.ymid, b.xmid, ycut)
        top = pathops.op(arch, loop, pathops.PathOp.UNION)
        pathops.op(top, cut, pathops.PathOp.DIFFERENCE).draw(pen)

        if stem:
            # Lower stem
            draw_rect(
                pen,
                b.x2 - sx,
                0,
                b.x2,
                (yt1 + b.y2) / 2,
            )
        else:
            draw_rect(
                pen,
                b.x2 - sx,
                (b.y1 + ybmid) / 2,
                b.x2 + sx * (right_taper - 1),
                (yt1 + b.y2) / 2,
            )

        return yt1
