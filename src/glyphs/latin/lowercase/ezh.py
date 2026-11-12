import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LatinLowercaseEzhGlyph(Glyph):
    """A flat-topped 3 from the x-height down into the descender (ʒ), drawn
    like the three_2: a top bar, a diagonal down to the middle and an open
    bottom loop."""

    name = "latin_lowercase_ezh"
    unicode = "0x292"
    offset = 0
    loop_width_ratio = 0.92
    # Middle of the glyph, relative to its height from the descent
    mid_ratio = 0.55
    taper = 0.9
    hx_ratio = 1.0
    hy_ratio = 1.0
    width_ratio = 1.0
    diag_stroke_ratio = 1.0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, overshoot_right=True, width_ratio=self.width_ratio
        )
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x, dc.stroke_y
        y1, y2 = dc.descent - dc.v_overshoot, b.y2
        height = y2 - y1
        hx = b.hx * self.hx_ratio
        # b.hy is sized for the x-height, the ezh is taller
        hy = b.hy * self.hy_ratio * height / b.height

        ymid = y1 + self.mid_ratio * height
        xl = b.x1 + (1 - self.loop_width_ratio) * b.width / 2
        xr = b.x2 - (1 - self.loop_width_ratio) * b.width / 2
        ry = (y2 - (y1 + y2) / 2 + sy / 2) / height

        # Top bar
        draw_rect(pen, xl, y2 - sy, xr, y2)
        _, delta = draw_parallelogramm(
            pen,
            self.diag_stroke_ratio * sx,
            b.xmid - sx,
            ymid + sy * self.taper - sy / 2,
            xr,
            y2 - sy,
            direction="top-right",
        )

        # Bottom loop
        base_glyph = ufoLib2.objects.Glyph()
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            y1,
            b.x2,
            ymid + sy / 2,
            hx,
            hy * ry * 2 * self.mid_ratio,
            taper=self.taper,
            side="top",
        )

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1,
            ymid - height / 4 + ec,
            b.x1 + b.width / 2,
            ymid + height / 4 - ec,
        )
        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Extension of the middle bar
        draw_rect(
            pen,
            b.xmid - sx,
            ymid - sy / 2,
            b.xmid - sx + delta,
            ymid + sy * self.taper - sy / 2,
        )
