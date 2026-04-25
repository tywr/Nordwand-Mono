from glyphs import Glyph
from draw.polygon import draw_polygon
from draw.rect import draw_rect


class ExclamationMarkGlyph(Glyph):
    name = "exclamation_mark"
    unicode = "0x21"
    offset = 0
    width_ratio = 1
    gap = 0.35
    height_overflow = 0.05
    stroke_ratio = 1
    taper_length = 0.25
    taper = 0.75

    def draw(self, pen, dc):
        from glyphs.special.full_stop import FullStopGlyph

        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx = dc.stroke_x * self.stroke_ratio
        g = self.gap * b.height
        dh = self.height_overflow * b.height
        h = b.y2 + dh - b.y1 - g

        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y1 + g + h * self.taper_length,
            b.xmid + dc.stroke_x / 2,
            b.y2 + dh,
        )
        draw_polygon(
            pen,
            points=[
                (b.xmid + sx / 2, b.y1 + g + h * self.taper_length),
                (b.xmid - sx / 2, b.y1 + g + h * self.taper_length),
                (b.xmid - self.taper * sx / 2, b.y1 + g),
                (b.xmid + self.taper * sx / 2, b.y1 + g),
            ],
        )

        fsp = FullStopGlyph()
        fsp.draw(pen, dc)
