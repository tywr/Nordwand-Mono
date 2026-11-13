from abc import ABC
from glyphs.uppercase import UppercaseGlyph


class RoundUppercaseGlyph(UppercaseGlyph, ABC):
    """C, G, O, Q: a bowl overshooting the cap height and the baseline"""

    width_ratio = 1.01
    height = "cap"
    opening2 = 0.69
    right_hx_ratio = 1.2

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            height=self.height,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
