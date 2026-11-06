from draw.arch import draw_arch
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseSchwaGlyph(RoundLowercaseGlyph):
    """The e turned upside down: a whole bottom half, and the aperture on the
    top left, between the bar and `tail_height` below the top."""

    name = "lowercase_schwa"
    unicode = "0x259"
    offset = -2
    width_ratio = 1
    mid_height = 0.48
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
        self.draw_schwa(pen, dc, b, sx, sy)

    def draw_schwa(self, pen, dc, b, sx, sy):
        ec = self.extra_cut(dc)
        yo = b.y2 - self.tail_height * b.height - ec
        ymid = b.y1 + self.mid_height * b.height
        yb2 = b.y1 + self.mid_height * b.height * 2
        yt1 = b.y2 - (1 - self.mid_height) * b.height * 2

        # Half-bottom as the o-shape
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            yb2,
            b.hx,
            b.hy * (yb2 - b.y1) / b.height,
            taper=1,
            side="left",
            cut="top",
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_arch(
            loop_glyph.getPen(),
            sx,
            sy,
            b.x1,
            yt1,
            b.x2,
            b.y2,
            b.hx,
            b.hy * (b.y2 - yt1) / b.height,
            taper=1,
            side="left",
            cut="bottom",
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid - b.width,
            ymid,
            b.xmid,
            yo,
        )
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # The bar reaches the outer edge on the side of the aperture
        draw_rect(
            pen,
            b.x1,
            ymid,
            b.x2 - sx / 2,
            ymid + dc.stroke_alt / 2,
        )
        draw_rect(
            pen,
            b.x1 + sx / 2,
            ymid - dc.stroke_alt / 2,
            b.x2 - sx / 2,
            ymid,
        )
