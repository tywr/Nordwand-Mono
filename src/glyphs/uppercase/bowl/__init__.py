from abc import ABC
from glyphs.uppercase import UppercaseGlyph


class BowlUppercaseGlyph(UppercaseGlyph, ABC):
    """B, D, P, R: a stem on the left, closed by bowls on its right"""

    offset = 20
    width_ratio = 1.0
    height = "cap"
    hx_ratio = 1
    hy_ratio = 1

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            height=self.height,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
