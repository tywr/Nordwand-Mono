from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.rect import draw_rect
import pathops
from nordwand_mono.glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseEGlyph(RoundLowercaseGlyph):
    name = "lowercase_e"
    unicode = "0x65"
    offset = 2
    width_ratio = 1
    mid_height = 0.52
    tail_offset = 0.01
    tail_height = 0.268
    left_hx_ratio = 1
    right_hx_ratio = 1.1
    right_thinning = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.get_strokes(dc)
        self.draw_e(pen, dc, b, sx, sy)

    def draw_e(self, pen, dc, b, sx, sy, left_taper=None):
        """The whole e within `b`. With `left_taper`, the left side is
        thinned to that ratio of `sx` from the outside, so it can share a
        stroke with a glyph on its left."""
        ec = self.extra_cut(dc)
        yo = b.y1 + self.tail_height * b.height + ec
        ymid = b.y1 + self.mid_height * b.height
        yt1 = b.y2 - (1 - self.mid_height) * b.height * 2
        yt2 = b.y1 + self.mid_height * b.height * 2
        xt = b.x2 + self.tail_offset * b.width
        lhx = self.left_hx_ratio * b.hx
        rhx = self.right_hx_ratio * b.hx

        # Half-left as the o-shape
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            yt1,
            b.x2,
            b.y2,
            b.hx,
            b.hy * (b.y2 - yt1) / b.height,
            taper=left_taper if left_taper else 1,
            side="left",
            cut="bottom",
        )

        # Bottom-left quarter, then bottom-right quarter widened to `xt`
        # Skia rather than booleanOperations, which drops the curve of the
        # bottom-left quarter in heavier weights of the æ
        loop = pathops.Path()
        draw_arch(
            pathops.PathPen(loop),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            yt2,
            lhx,
            b.hy * (yt2 - b.y1) / b.height,
            taper=left_taper if left_taper else 1,
            side="left",
            quarter="bottom-left",
        )
        draw_arch(
            pathops.PathPen(loop),
            sx * self.right_thinning,
            sy,
            2 * b.xmid - xt,
            b.y1,
            xt,
            yt2,
            rhx,
            b.hy * (yt2 - b.y1) / b.height,
            taper=left_taper if left_taper else 1,
            side="left",
            quarter="bottom-right",
        )

        cut = pathops.Path()
        draw_rect(
            pathops.PathPen(cut),
            b.xmid,
            yo,
            b.xmid + b.width,
            ymid,
        )
        pathops.op(loop, cut, pathops.PathOp.DIFFERENCE).draw(pen)

        draw_rect(
            pen,
            b.x1 + sx / 2,
            ymid,
            b.x2 - sx / 2,
            ymid + dc.stroke_alt / 2,
        )
        draw_rect(
            pen,
            b.x1 + sx / 2,
            ymid - dc.stroke_alt / 2,
            b.x2,
            ymid,
        )
