"""Letters with a bar across their stem (Ғ ғ Ұ ұ)."""

from draw.rect import draw_rect
from glyphs.cyrillic.lowercase.ghe import CyrillicLowercaseGheGlyph
from glyphs.cyrillic.lowercase.lookalikes import CyrillicLowercaseStraightUGlyph
from glyphs.cyrillic.uppercase.ghe import CyrillicUppercaseGheGlyph
from glyphs.cyrillic.uppercase.lookalikes import CyrillicUppercaseStraightUGlyph


class CyrillicUppercaseGheStrokeGlyph(CyrillicUppercaseGheGlyph):
    name = "cyrillic_uppercase_ghe_stroke"
    unicode = "0x0492"
    bar_y = 0.45  # Relative to the cap height
    # Bar reach past the stem, as fractions of the body width
    bar_left = 0.1
    bar_right = 0.3

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, s = dc.stroke_x * self.stroke_x_ratio, dc.stroke_alt
        y = self.bar_y * b.height
        draw_rect(
            pen,
            b.x1 - self.bar_left * b.width,
            y - s / 2,
            b.x1 + sx + self.bar_right * b.width,
            y + s / 2,
        )


class CyrillicLowercaseGheStrokeGlyph(CyrillicLowercaseGheGlyph):
    name = "cyrillic_lowercase_ghe_stroke"
    unicode = "0x0493"
    bar_y = 0.45  # Relative to the x-height
    # Bar reach past the stem, as fractions of the body width
    bar_left = 0.15
    bar_right = 0.3

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = dc.stroke_alt
        y = self.bar_y * b.height
        draw_rect(
            pen,
            b.x1 - self.bar_left * b.width,
            y - s / 2,
            b.x1 + dc.stroke_x + self.bar_right * b.width,
            y + s / 2,
        )


class CyrillicUppercaseStraightUStrokeGlyph(CyrillicUppercaseStraightUGlyph):
    name = "cyrillic_uppercase_straight_u_stroke"
    unicode = "0x04B0"
    bar_y = 0.28  # Relative to the cap height, below the junction
    bar_width = 0.6  # Relative to the body width

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        s, w = dc.stroke_alt, self.bar_width * b.width
        y = self.bar_y * b.height
        draw_rect(pen, b.xmid - w / 2, y - s / 2, b.xmid + w / 2, y + s / 2)


class CyrillicLowercaseStraightUStrokeGlyph(CyrillicLowercaseStraightUGlyph):
    name = "cyrillic_lowercase_straight_u_stroke"
    unicode = "0x04B1"
    bar_y = 0.45  # Relative to the descent, across the stem
    bar_width = 0.5  # Relative to the body width

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s, w = dc.stroke_alt, self.bar_width * b.width
        y = self.bar_y * dc.descent
        draw_rect(pen, b.xmid - w / 2, y - s / 2, b.xmid + w / 2, y + s / 2)
