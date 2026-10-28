from math import tan
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs import Glyph
from glyphs.numbers.three import ThreeGlyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from utils.pens import NullPen


class AmpersandGlyph(Glyph):
    name = "ampersand"
    unicode = "0x26"
    offset = -50
    width_ratio = 1.08
    upper_width = 0.8
    upper_height = 0.4
    lower_width = 1
    hook_ratio = 0.12
    hook_drop = 2
    hook_below_baseline = 0
    hook_outside_cell = 0.24
    end_height_ratio = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )

        ox = self.hook_outside_cell * b.width
        h = self.upper_height * b.height
        w = self.upper_width * b.width
        xu1, xu2 = b.xmid - w / 2, b.xmid + w / 2
        yu1, yu2 = b.y2 - h, b.y2

        # Same handles as the top loop of the 3, the loop being drawn lower for
        # bolder weights while the junction stays where it was
        loop = ThreeGlyph().top_loop(dc).resize(xu1, yu1, xu2, yu2)
        xj = xu1 + self.hook_ratio * w
        (_, y1), (_, y2) = loop.intersection_x(x=xj)
        yj = min(y1, y2)

        yu1 -= 2 * self.extra_cut(dc)
        loop = loop.resize(xu1, yu1, xu2, yu2)
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xu1,
            yu1,
            xu2,
            yu2,
            loop.hx,
            loop.hy,
            cut="bottom",
        )

        # Draw the parallelogramm to the bottom right, its top lowered for
        # bolder weights to leave room for the curves to turn
        dhy = self.hook_below_baseline * b.height
        yd = yj - self.hook_drop * self.extra_cut(dc)
        theta, delta = draw_parallelogramm(
            NullPen(),
            dc.stroke_x,
            dc.stroke_y,
            b.x2 + ox,
            -dhy,
            xj,
            yd,
            direction="top-left",
        )

        # Draw the curve to the intersection
        ym = 0.5 * yu1 + 0.5 * yu2
        hy = ym - yd - tan(theta) * (xj - xu1)
        pen.moveTo((xu1, ym))
        pen.curveTo(
            (xu1, ym - hy),
            (xj, yd),
            (b.x2 + ox - delta, -dhy),
        )
        pen.lineTo((b.x2 + ox, -dhy))
        pen.curveTo(
            (xj + delta, yd),
            (xu1 + dc.stroke_x, ym - hy),
            (xu1 + dc.stroke_x, ym),
        )
        pen.closePath()

        # Draw the lower bowl
        xbm = b.xmid
        lw = self.lower_width * b.width
        lh = yj - b.y1

        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xbm - lw / 2,
            b.y1,
            xbm + lw / 2,
            yj,
            b.hx * lw / b.width,
            b.hy * lh / b.height,
            cut="top",
            side="top",
            taper=0.5,
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_arch(
            loop_glyph.getPen(),
            dc.stroke_x,
            dc.stroke_y,
            xbm - lw / 2,
            b.y1,
            xbm + lw / 2,
            yj,
            b.hx * lw / b.width,
            b.hy * lh / b.height,
            cut="right",
            side="top",
            taper=0.5,
        )

        xcut = xj + delta - (yj - yd) / tan(theta)
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), xcut, 0.5 * b.y1 + 0.5 * yj, b.x2, b.y2)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Draw the height extension
        eh = self.end_height_ratio * b.height
        draw_rect(
            pen, xbm + lw / 2 - dc.stroke_x, 0.5 * b.y1 + 0.5 * yj, xbm + lw / 2, eh
        )
