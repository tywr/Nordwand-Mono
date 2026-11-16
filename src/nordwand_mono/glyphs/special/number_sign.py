from nordwand_mono.glyphs import InfiniteLigatureGlyph
from nordwand_mono.draw.rect import draw_rect


class NumberSignGlyph(InfiniteLigatureGlyph):
    name = "number_sign"
    unicode = "0x23"
    offset = 0
    width_ratio = 1.32
    gap = 0.42
    height = 1

    def _geometry(self, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        g = self.gap * b.width
        h = self.height * b.height
        xm1, xm2 = b.xmid - g / 2, b.xmid + g / 2
        ym1, ym2 = dc.math - g / 2, dc.math + g / 2
        y1, y2 = dc.math - h / 2, dc.math + h / 2
        return b, xm1, xm2, ym1, ym2, y1, y2

    def horizontal_bar_heights(self, dc):
        _, _, _, ym1, ym2, _, _ = self._geometry(dc)
        return ym1, ym2

    def horizontal_bar_stroke(self, dc):
        return dc.stroke_y

    def horizontal_bar_bounds(self, dc):
        b, _, _, _, _, _, _ = self._geometry(dc)
        return b.x1, b.x2

    def draw_non_horizontal(self, pen, dc):
        _, xm1, xm2, _, _, y1, y2 = self._geometry(dc)
        sx = dc.stroke_x / 2
        draw_rect(pen, xm1 - sx, y1, xm1 + sx, y2)
        draw_rect(pen, xm2 - sx, y1, xm2 + sx, y2)
