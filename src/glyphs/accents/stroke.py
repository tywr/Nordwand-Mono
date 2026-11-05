from math import atan2, cos
from draw.polygon import draw_polygon
from glyphs.accents import Accent


class Stroke(Accent):
    """Slanted bar crossing a stem, as in ł and Ł."""

    name = "stroke"
    unicode = None
    generated_only = True  # Only used inside composed glyphs
    left = 0.4  # Reach left of the stem center, as a fraction of the body width
    right = 0.4  # Reach right of the stem center
    rise = 0.3  # Vertical rise, as a fraction of the x-height
    stroke_ratio = 0.9

    def draw_at(self, pen, dc, x, y):
        x1, x2 = x - self.left * dc.width, x + self.right * dc.width
        h = self.rise * dc.x_height
        y1 = y - h * self.left / (self.left + self.right)
        y2 = y1 + h
        # Vertical thickness giving a perpendicular stroke of stroke_y weight.
        t = self.stroke_ratio * dc.stroke_y / cos(atan2(h, x2 - x1))
        draw_polygon(
            pen,
            points=[
                (x1, y1 - t / 2),
                (x2, y2 - t / 2),
                (x2, y2 + t / 2),
                (x1, y1 + t / 2),
            ],
        )


class UppercaseStroke(Stroke):
    # The L stem sits at the left of the cell, so the bar reaches mostly right.
    left = 0.28
    right = 0.5
