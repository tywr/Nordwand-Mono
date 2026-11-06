from glyphs.accents import Accent
from draw.loop import draw_loop


class Horn(Accent):
    """Spur growing out of the right shoulder of o and u (Vietnamese ơ, ư):
    a stroke going right, then curving up.

    Unlike most accents, `draw_at` anchors the mark by the left end of its
    bottom edge, which callers place inside the base outline so the two
    merge.
    """

    name = "horn"
    unicode = None
    generated_only = True  # Only used inside composed glyphs
    width = 0.1
    height = 0.2
    stroke_y_ratio = 1.0
    taper = 2.5

    def draw_at(self, pen, dc, x, y, width_ratio=None):
        """`sx` and `sy` are the base glyph's strokes, `dc`'s by default."""
        taper = min(1, self.taper * dc.taper)
        sx = dc.stroke_x
        sy = dc.stroke_y * taper
        w = self.width * dc.width + sx
        h = self.height * dc.x_height + sy

        b = dc.body_bounds(offset=0)
        draw_loop(
            pen,
            sx,
            sy,
            x - w,
            y - sy,
            x + w,
            y + 2 * h - sy,
            b.hx * 2 * w / b.width,
            b.hy * 2 * h / b.height,
            quarter="bottom-right",
        )

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=0.8 * dc.x_height)
