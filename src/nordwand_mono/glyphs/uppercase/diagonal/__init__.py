from abc import ABC
from nordwand_mono.glyphs.uppercase import UppercaseGlyph


class DiagonalUppercaseGlyph(UppercaseGlyph, ABC):
    """A, V, W, X, Y: diagonal branches meeting at a vertex. The counter is cut
    where they cross, so the vertex keeps `section_height` of solid stroke
    instead of thickening"""

    width_ratio = 1.15
    height = "cap"
    branch_stroke_ratio = 1
    overlap = 0.25
    section_height = 1
    expand_factor=1.2

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset, height=self.height, width_ratio=self.width_ratio, expand_factor=self.expand_factor
        )
