import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from math import radians

from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen

from draw.arch import draw_arch
from draw.polygon import draw_polygon
from draw.rect import draw_rect
from glyphs.accents import Accent


class Ogonek(Accent):
    """Half of a loop hanging below the baseline: the loop is drawn with its
    top apex at the origin and cut along its axis, then rotated around that
    apex and cut flat above sy / 2 so it sits on the letter."""

    name = "ogonek"
    unicode = "0x2DB"
    width_ratio = 0.6
    stroke_x_ratio = 0.9
    stroke_y_dampening = 0.0
    depth = 0.8
    angle = 12
    taper = 1.2
    stem_ratio = 1.0
    hx_ratio = 0.9
    hy_ratio = 0.9

    def draw_at(
        self, pen, dc, x, y, width=None, start=0, cut_top=False, cut_slant=False
    ):
        """`x`, `y + start` is where the loop's top apex lands; `width` is
        the thickness of the loop's side (by default a stem width). With
        `cut_top`, everything above sy / 2 is cut once pivoted. With
        `cut_slant`, everything right of the 45° line going up-left from
        the apex is cut."""
        b = dc.body_bounds(
            offset=0,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        sx = self.stroke_x_ratio * dc.stroke_x
        sy = min(dc.stroke_y, 70) + self.stroke_y_dampening * max(0, dc.stroke_y, 70)
        # ec = self.extra_cut(dc)
        ec = 0
        w = b.width
        h = self.depth * abs(dc.descent)
        taper = min(1, dc.taper * self.taper)

        glyph = ufoLib2.objects.Glyph()
        draw_arch(
            glyph.getPen(),
            sx,
            sy,
            -w / 2,
            -h,
            w / 2,
            sy,
            b.hx * w / (b.x2 - b.x1) * self.hx_ratio,
            b.hy * (h + sy) / (b.y2 - b.y1) * self.hy_ratio,
            side="top",
            cut="right",
            taper=taper,
        )
        draw_rect(glyph.getPen(), 0, -h, ec, -h + sy)

        # Pivot around the apex, then optionally cut everything above sy / 2
        pivoted = ufoLib2.objects.Glyph()
        glyph.draw(
            TransformPen(pivoted.getPen(), Transform().rotate(radians(self.angle)))
        )
        res = BooleanGlyph(pivoted)
        cut_glyph = ufoLib2.objects.Glyph()
        r = w + h  # Covers the pivoted loop whatever the angle
        if cut_slant:
            draw_polygon(cut_glyph.getPen(), [(-r, r), (r, -r), (r, r)])
        if cut_top:
            draw_rect(cut_glyph.getPen(), -r, sy / 2, r, r)
        res = res.difference(BooleanGlyph(cut_glyph))
        res.draw(TransformPen(pen, Transform().translate(x, y + start)))

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=0)
