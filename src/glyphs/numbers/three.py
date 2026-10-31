import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from shapes.superellipse import Superellipse
from draw.arch import draw_arch
from draw.rect import draw_rect


class ThreeGlyph(NumberGlyph):
    name = "three"
    unicode = "0x33"
    offset = 0
    loop_width_ratio = 0.92
    mid_ratio = 0.52
    taper = 1
    len_mid = 0.7
    hx_ratio = 0.9
    hy_ratio = 0.9
    width_ratio = 1.08

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )

    def top_loop(self, dc) -> Superellipse:
        """Superellipse of the top loop, also used to shape similar loops."""
        b = self.body(dc)
        sy = dc.stroke_y * self.stroke_y_ratio
        ymid = b.y1 + self.mid_ratio * b.height
        ry = (b.y2 - b.ymid + sy / 2) / b.height
        return Superellipse(
            x1=b.x1 + (1 - self.loop_width_ratio) * b.width / 2,
            y1=ymid - sy / 2,
            x2=b.x2 - (1 - self.loop_width_ratio) * b.width / 2,
            y2=b.y2,
            hx=b.hx * self.hx_ratio,
            hy=b.hy * self.hy_ratio * ry * 2 * (1 - self.mid_ratio),
        )

    def draw(self, pen, dc):
        b = self.body(dc)
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio

        ymid = b.y1 + self.mid_ratio * b.height
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
            ymid + sy / 2,
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
            ymid - b.height / 4 + ec,
            b.x1 + b.width / 2,
            ymid + b.height / 4 - ec,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Extension of the middle bar
        draw_rect(
            pen,
            b.x1 + (1 - self.len_mid) * b.width,
            ymid - sy / 2,
            b.xmid,
            ymid + sy / 2,
        )
