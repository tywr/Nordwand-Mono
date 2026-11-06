from abc import ABC

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph
from shapes.superellipse import Superellipse
from draw.arch import draw_arch
from draw.rect import draw_rect


class OpenEGlyph(Glyph, ABC):
    """Shape shared by the number 3, the cyrillic ze, the greek epsilon and
    the latin open e: a narrower loop on top of a wider one, cut open on the
    left between `opening1` and `opening2`, with a bar in the middle.
    `mirrored` flips it horizontally, to open it on the right (epsilon, open
    e). `cap` draws it at the cap height with the handles of the capitals,
    `number` with those of the numbers."""

    offset = 0
    loop_width_ratio = 0.92
    mid_ratio = 0.515
    taper = 1
    hx_ratio = 1
    hy_ratio = 1
    width_ratio = 0.99
    mid_length = 0.7  # Length of the bar, relative to the body width
    opening1 = 0.265  # Bottom of the opening, relative to the body height
    opening2 = 0.765  # Top of the opening, relative to the body height
    stroke_x_ratio = 1
    stroke_y_ratio = 1
    mirrored = False
    cap = False
    number = False
    mid_stroke_alt = False  # Thinner middle bar, like the bar of the e

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            height="cap" if self.cap or self.number else "x_height",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=self.number,
            uppercase=self.cap,
        )

    def mid_stroke(self, dc):
        return dc.stroke_alt if self.mid_stroke_alt else dc.stroke_y * self.stroke_y_ratio

    def top_loop(self, dc) -> Superellipse:
        """Superellipse of the top loop, also used to shape similar loops."""
        b = self.body(dc)
        sy = dc.stroke_y * self.stroke_y_ratio
        ymid = b.y1 + self.mid_ratio * b.height
        ry = (b.y2 - b.ymid + sy / 2) / b.height
        return Superellipse(
            x1=b.x1 + (1 - self.loop_width_ratio) * b.width / 2,
            # The bottom of the loop sits on the top of the middle bar
            y1=ymid + self.mid_stroke(dc) / 2 - sy,
            x2=b.x2 - (1 - self.loop_width_ratio) * b.width / 2,
            y2=b.y2,
            hx=b.hx * self.hx_ratio,
            hy=b.hy * self.hy_ratio * ry * 2 * (1 - self.mid_ratio),
        )

    def draw(self, pen, dc):
        if self.mirrored:
            # Mirroring flips the contours direction, reverse them back
            mirror = (-1, 0, 0, 1, dc.window_width, 0)
            pen = TransformPen(ReverseContourPen(pen), mirror)
        self.draw_open_e(pen, dc)

    def draw_open_e(self, pen, dc):
        b = self.body(dc)
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio

        xc = b.x2 - self.mid_length * b.width - ec
        yc1 = b.y1 + self.opening1 * b.height + ec
        yc2 = b.y1 + self.opening2 * b.height - ec
        ymid = b.y1 + self.mid_ratio * b.height
        sm = self.mid_stroke(dc)
        ry = (b.y2 - b.ymid + sy / 2) / b.height
        base_glyph = ufoLib2.objects.Glyph()

        # Top loop
        taper = max(self.taper * dc.taper, 0.65)
        top = self.top_loop(dc)
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            top.x1,
            top.y1,
            top.x2,
            top.y2,
            top.hx,
            top.hy,
            taper=taper,
            side="bottom",
        )

        # Bottom loop
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid - sm / 2 + sy,
            hx,
            hy * ry * 2 * self.mid_ratio,
            taper=taper,
            side="top",
        )

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1,
            yc1,
            b.xmid,
            yc2,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Extension of the middle bar
        draw_rect(
            pen,
            xc,
            ymid - sm / 2,
            b.xmid,
            ymid + sm / 2,
        )
