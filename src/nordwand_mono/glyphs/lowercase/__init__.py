from abc import ABC

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.glyphs import Glyph


class TailedLowercaseGlyph(Glyph, ABC):
    """Lowercase glyphs whose right stem curves down-left into a cut tail in
    the descender (g, y_2)"""

    tail_hx_ratio = 1.0
    tail_hy_ratio = 1.0
    tail_stroke_y_ratio = 1.0
    tail_offset = 0.03
    cut_ratio = 0.265
    y1_offset = 0.065
    extra_cut_ratio = 0.2
    stroke_y_dampening = 0.8

    def draw_tail(self, pen, dc, b):
        """Right stem over the x-height and the tail below it, in body `b`."""
        ec = self.extra_cut(dc)
        sx, sy = self.get_strokes(dc)
        sy *= self.tail_stroke_y_ratio
        xt = b.x1 + self.tail_offset * b.width
        h = 2 * (abs(dc.descent) + dc.v_overshoot)

        # Right stem — full x_height
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.x_height)

        # Corner curving down-left into the descender
        glyph = ufoLib2.objects.Glyph()
        draw_loop(
            glyph.getPen(),
            self.get_thinned_stroke(dc),
            sy,
            xt,
            -h / 2,
            b.x2,
            h / 2,
            b.hx * (b.x2 - xt) / b.width * self.tail_hx_ratio,
            b.hy * h / b.height,
            quarter="bottom-left"
        )
        draw_loop(
            glyph.getPen(),
            sx,
            sy,
            xt,
            -h / 2,
            b.x2,
            h / 2,
            b.hx * (b.x2 - xt) / b.width,
            b.hy * h / b.height,
            quarter="bottom-right"
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            dc.descent - dc.v_overshoot + b.height * self.cut_ratio + ec,
            b.xmid,
            b.ymid,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
