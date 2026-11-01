from math import hypot

from draw.polygon import draw_polygon
from glyphs.box import BoxGlyph, box_glyph


class DiagonalBoxGlyph(BoxGlyph):
    """Light lines joining opposite corners of the cell."""

    rising = False  # ╱
    falling = False  # ╲

    def draw(self, pen, dc):
        (x1, y1, x2, y2), _ = self.cell(dc)
        s = self.stroke("light")
        # Horizontal width giving the line a thickness of `s`
        t = s * hypot(x2 - x1, y2 - y1) / (y2 - y1) / 2
        # Extend past the corners along the line, by `bleed` vertically
        b = self.bleed
        bx = b * (x2 - x1) / (y2 - y1)
        x1, y1, x2, y2 = x1 - bx, y1 - b, x2 + bx, y2 + b
        if self.rising:
            draw_polygon(pen, [(x1 - t, y1), (x1 + t, y1), (x2 + t, y2), (x2 - t, y2)])
        if self.falling:
            draw_polygon(pen, [(x1 - t, y2), (x2 - t, y1), (x2 + t, y1), (x1 + t, y2)])


GLYPHS = [
    box_glyph(DiagonalBoxGlyph, 0x2571, rising=True),
    box_glyph(DiagonalBoxGlyph, 0x2572, falling=True),
    box_glyph(DiagonalBoxGlyph, 0x2573, rising=True, falling=True),
]
