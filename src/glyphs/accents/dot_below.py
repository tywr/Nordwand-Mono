from glyphs.accents.dot import DotAbove
from draw.dot import dot_size, draw_dot


class DotBelow(DotAbove):
    """Dot hanging below the baseline (Vietnamese ạ, ệ, ợ).

    `draw_at` takes the baseline as y and hangs the dot `gap` below it.
    """

    name = "dotbelow"
    unicode = None
    generated_only = True  # Only used inside composed glyphs
    gap = 0.08

    def draw_at(self, pen, dc, x, y):
        _, h = dot_size(dc, self.dot_ratio)
        draw_dot(pen, dc, x, y - self.gap * dc.x_height - h / 2, self.dot_ratio)

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=0)
