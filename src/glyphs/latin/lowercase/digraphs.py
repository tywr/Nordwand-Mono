"""IPA affricate digraphs, two lowercase letters joined in one cell. The tesh
(ʧ) has its own module, for its joining bar."""

from glyphs.joint import JointGlyph, LeftBarJointGlyph
from glyphs.latin.lowercase.esh import LatinLowercaseEshGlyph
from glyphs.latin.lowercase.ezh import LatinLowercaseEzhGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.lowercase.z import LowercaseZGlyph
from draw.rect import draw_rect


class LatinLowercaseDezhGlyph(JointGlyph):
    """ʤ"""

    name = "latin_lowercase_dezh"
    unicode = "0x2A4"
    left_class = LowercaseDGlyph
    right_class = LatinLowercaseEzhGlyph
    width_ratio = 1.2
    overlap = -0.05
    def extra_draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        draw_rect(
            pen,
            b.x1 + b.width * self.scale_left,
            b.y2 - dc.stroke_y,
            b.x1 + 0.5 * (self.scale_left + 1) * b.width,
            b.y2,
        )


class LatinLowercaseDzGlyph(JointGlyph):
    """ʣ"""

    name = "latin_lowercase_dz"
    unicode = "0x2A3"
    left_class = LowercaseDGlyph
    right_class = LowercaseZGlyph
    width_ratio = 1.2
    overlap = 0.05


class LatinLowercaseTsGlyph(JointGlyph):
    """ʦ"""

    name = "latin_lowercase_ts"
    unicode = "0x2A6"
    left_class = LowercaseTGlyph
    right_class = LowercaseSGlyph
    width_ratio = 1.2
    overlap = 0

    def extra_draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        draw_rect(
            pen,
            b.x1 + b.width * self.scale_left,
            b.y1,
            b.x1 + b.width * self.scale_left + dc.stroke_x * 0.75,
            b.y1 + dc.stroke_y,
        )
        draw_rect(
            pen,
            b.x1 + b.width * self.scale_left + dc.stroke_x * 0.75,
            b.y1,
            b.x1 + b.width * self.scale_left + (1 - self.scale_left) * 0.5 * b.width,
            b.y1 - dc.v_overshoot + dc.stroke_y,
        )


class LatinLowercaseLezhGlyph(LeftBarJointGlyph):
    """ɮ"""

    name = "latin_lowercase_lezh"
    unicode = "0x26E"
    right_class = LatinLowercaseEzhGlyph
    width_ratio = 1.2
    overlap = -0.1
    width_ratio = 1.08

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

class LatinLowercaseTeshGlyph(JointGlyph):
    """ʧ"""

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
