from draw.rect import draw_rect
from glyphs.joint import JointGlyph
from glyphs.latin.lowercase.esh import LatinLowercaseEshGlyph
from glyphs.lowercase.t import LowercaseTGlyph


class LatinLowercaseTeshGlyph(JointGlyph):
    """The t joined to the esh (ʧ)."""

    name = "latin_lowercase_tesh"
    unicode = "0x2A7"
    left_class = LowercaseTGlyph
    right_class = LatinLowercaseEshGlyph
    width_ratio = 1.2
    overlap = 0
    scale_left = 0.5

    def extra_draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        draw_rect(
            pen,
            b.x1,
            b.y2 - dc.stroke_y,
            b.x1 + 0.5 * (self.scale_left + 1) * b.width,
            b.y2,
        )
