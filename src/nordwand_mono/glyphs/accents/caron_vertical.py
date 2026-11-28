from nordwand_mono.draw.polygon import draw_polygon
from nordwand_mono.glyphs.accents import Accent


class CaronVertical(Accent):
    """Apostrophe-like caron placed beside an ascender, as in ď and ť.

    Unlike the other accents, `draw_at` anchors the mark by its top-left
    corner, since it sits to the right of a stem rather than above it.
    Callers place it `gap_width` past the stem.
    """

    name = "caron_vertical"
    unicode = None
    generated_only = True  # Only used inside composed glyphs
    stroke_ratio = 1.0
    taper = 0.7
    height = 0.4
    lean = 0.2
    gap = 0.15

    def top_width(self, dc):
        return self.stroke_ratio * dc.stroke_x

    def gap_width(self, dc):
        return self.gap * dc.width

    def draw_at(self, pen, dc, x, y):
        """Draw the mark with the top-left corner of its top edge at (x, y)."""
        w = self.top_width(dc)
        y1 = y - self.height * dc.x_height
        lean = self.lean * w
        draw_polygon(
            pen,
            points=[
                (x, y),
                (x + w, y),
                (x + w - lean - (1 - self.taper) * w / 2, y1),
                (x - lean + (1 - self.taper) * w / 2, y1),
            ],
        )

    def draw(self, pen, dc):
        self.draw_at(
            pen, dc, x=dc.window_width / 2 - self.top_width(dc) / 2, y=dc.ascent
        )
