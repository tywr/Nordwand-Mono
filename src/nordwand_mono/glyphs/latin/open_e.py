from abc import ABC

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen

from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect


class OpenEGlyph(Glyph, ABC):
    """Shape shared by the number 3, the cyrillic ze, the greek epsilon and
    the latin open e: a narrower loop on top of a wider one, cut open on the
    left between `opening1` and `opening2`, with a bar in the middle.
    `mirrored` flips it horizontally, to open it on the right (epsilon, open
    e). `cap` draws it at the cap height with the handles of the capitals,
    `number` with those of the numbers."""

    offset = 0
    mid_ratio = 0.515
    taper = 1
    hx_ratio = 1
    hy_ratio = 1
    left_hx_ratio = 1.0
    width_ratio = 0.99
    mid_length = 0.7  # Length of the bar, relative to the body width
    opening1 = 0.245  # Bottom of the opening, relative to the body height
    opening2 = 0.765  # Top of the opening, relative to the body height
    top_left_offset = 0
    top_right_offset = 0.03
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
        return (
            dc.stroke_alt if self.mid_stroke_alt else self.get_strokes(dc)[1]
        )

    def draw(self, pen, dc):
        if self.mirrored:
            # Mirroring flips the contours direction, reverse them back
            mirror = (-1, 0, 0, 1, dc.window_width, 0)
            pen = TransformPen(ReverseContourPen(pen), mirror)
        self.draw_open_e(pen, dc)

    def draw_open_e(self, pen, dc):
        b = self.body(dc)
        ec = 0.66 * self.extra_cut(dc)
        sx, sy = self.get_strokes(dc)
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio

        xt1 = b.x1 + self.top_left_offset * b.width
        xt2 = b.x2 - self.top_left_offset * b.width
        xl1 = b.x1 + self.top_right_offset * b.width
        xl2 = b.x2 - self.top_right_offset * b.width
        xc = b.x2 - self.mid_length * b.width - ec
        yc1 = b.y1 + self.opening1 * b.height + ec
        yc2 = b.y1 + self.opening2 * b.height - ec
        ymid = b.y1 + self.mid_ratio * b.height
        sm = self.mid_stroke(dc)
        base_glyph = ufoLib2.objects.Glyph()
        taper = max(self.taper * dc.taper, 0.65)

        # Top loop
        ytmid = b.y1 + self.mid_ratio * b.height + self.mid_stroke(dc) / 2 - sy
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            xl1,
            ytmid,
            xl2,
            b.y2,
            hx * (xl2 - xl1) / b.width,
            hy * (b.y2 - ytmid) / b.height,
            taper=taper,
            side="bottom",
            cut="left",
        )
        draw_loop(
            base_glyph.getPen(),
            sx,
            sy,
            xt1,
            ytmid - 2 * ec,
            xt2,
            b.y2,
            hx * self.left_hx_ratio * (xt2 - xt1) / b.width,
            hy * (b.y2 - ytmid + 2 * ec) / b.height,
            quarter="top-left",
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
            hy * (ymid - sm / 2 + sy - b.y1) / b.height,
            taper=taper,
            side="top",
            cut="left",
        )
        draw_loop(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid - sm / 2 + sy + 2 * ec,
            hx * self.left_hx_ratio,
            hy * (ymid - sm / 2 + sy + 2 * ec - b.y1) / b.height,
            quarter="bottom-left",
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
