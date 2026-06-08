from abc import ABC, abstractmethod
from glyphs import Glyph

from draw.rect import draw_rect


class DottedLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    dot_height = 1.2
    dot_position = "xmid"
    dot_width = 1.2

    @abstractmethod
    def draw_base(self, pen, dc): ...

    def draw(self, pen, dc):
        self.draw_base(pen, dc)
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        dw = self.dot_width * dc.stroke_x

        # Accent dot
        xpos = getattr(b, self.dot_position)
        dh = self.dot_height * dc.stroke_x
        draw_rect(
            pen,
            xpos - dw / 2,
            dc.accent - dh / 2,
            xpos + dw / 2,
            dc.accent + dh / 2,
        )
