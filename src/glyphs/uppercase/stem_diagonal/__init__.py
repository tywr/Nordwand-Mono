from abc import ABC
from glyphs.uppercase import UppercaseGlyph


class StemDiagonalUppercaseGlyph(UppercaseGlyph, ABC):
    """M, N: two stems joined by thinner diagonals, with ink traps where the
    diagonals leave the stems"""

    height = "cap"
    overlap = 0.25
    inner_stroke_ratio = 0.95
    section_height = 1

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            height=self.height,
            width_ratio=self.width_ratio,
            uppercase=True,
            min_margin=dc.min_margin_uppercase,
        )

    def inner_stroke(self, stroke, dc):
        """Diagonal stroke, growing slower than `stroke` past the default weight"""
        si = stroke * self.inner_stroke_ratio
        return max(0, 0.7 * (si - dc.default_stroke)) + min(dc.default_stroke, si)
