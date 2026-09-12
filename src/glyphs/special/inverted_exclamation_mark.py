from glyphs import Glyph
from draw.polygon import draw_polygon
from draw.rect import draw_rect


class InvertedExclamationMarkGlyph(Glyph):
    name = "inverted_exclamation_mark"
    unicode = "0xA1"
    offset = 0
    width_ratio = 1
    gap = 0.35
    height_overflow = 0.05
    stroke_ratio = 1
    dot_stroke_ratio = 1.5
    taper_length = 0.25
    taper = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx = dc.stroke_x * self.stroke_ratio
        g = self.gap * b.height
        dh = self.height_overflow * b.height
        h = b.y2 + dh - b.y1 - g

        # Dot
        s = self.dot_stroke_ratio * dc.stroke_x
        draw_rect(pen, b.xmid - s / 2, dc.x_height - s, b.xmid + s / 2, dc.x_height)

        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            dc.descent,
            b.xmid + dc.stroke_x / 2,
            dc.descent + g + h * self.taper_length,
        )
        draw_polygon(
            pen,
            points=[
                (b.xmid + self.taper * sx / 2, dc.x_height - g),
                (b.xmid - self.taper * sx / 2, dc.x_height - g),
                (b.xmid - sx / 2, dc.descent + g + h * self.taper_length),
                (b.xmid + sx / 2, dc.descent + g + h * self.taper_length),
            ],
        )
