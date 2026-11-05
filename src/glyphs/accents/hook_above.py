from glyphs.accents import Accent
from draw.loop import draw_loop
from draw.rect import draw_rect
from shapes.superellipse import Superellipse


class HookAbove(Accent):
    """Small dotless question mark (Vietnamese ả, ể, ở): an arch from the
    left turning back to the center, then a short stem down."""

    name = "hookabove"
    unicode = None
    generated_only = True
    width = 0.6
    height = 0.4
    bowl = 0.85
    stroke_ratio = 0.7

    def draw_at(self, pen, dc, x, y):
        w = self.width * dc.width
        h = self.height * dc.x_height
        # Thickens slower than the strokes, like dots, so that the small
        # counter stays open in bold
        k = (dc.stroke_x / dc.default_stroke) ** dc.dot_exponent
        sx = self.stroke_ratio * dc.default_stroke * k
        sy = sx * dc.stroke_y / dc.stroke_x
        top, bottom = y + h / 2, y - h / 2

        # The bowl and the stem hanging from its end are both centered on x
        b = dc.body_bounds(offset=0)
        se = Superellipse(b.x1, b.y1, b.x2, b.y2, b.hx, b.hy).resize(
            x - w / 2, top - self.bowl * h, x + w / 2, top
        )
        for quarter in ("top-left", "top-right", "bottom-right"):
            draw_loop(
                pen, sx, sy, se.x1, se.y1, se.x2, se.y2, se.hx, se.hy, quarter=quarter
            )

        draw_rect(pen, x - sx / 2, bottom, x + sx / 2, se.y1 + sy)
