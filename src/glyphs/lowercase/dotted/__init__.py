from abc import ABC, abstractmethod
from glyphs import Glyph

from draw.dot import draw_dot


class DottedLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    dot_position = "xmid"
    dot_ratio = 1.2
    rl_ratio = 0.5

    @abstractmethod
    def draw_base(self, pen, dc): ...

    def draw(self, pen, dc):
        self.draw_base(pen, dc)
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        xpos = b.x1 + self.rl_ratio * b.width
        draw_dot(pen, dc, xpos, dc.accent, self.dot_ratio)
