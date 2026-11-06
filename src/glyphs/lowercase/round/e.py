from draw.arch import draw_arch
from draw.loop import draw_loop
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseEGlyph(RoundLowercaseGlyph):
    name = "lowercase_e"
    unicode = "0x65"
    offset = 2
    width_ratio = 1
    mid_height = 0.52
    tail_offset = 0.00
    tail_height = 0.268

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
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

        loop_glyph = ufoLib2.objects.Glyph()
        draw_arch(
            loop_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            yt2,
            b.hx,
            b.hy * (yt2 - b.y1) / b.height,
            taper=left_taper if left_taper else 1,
            side="left",
            cut="top",
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yo,
            b.xmid + b.width,
            ymid,
        )
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

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
