from math import cos, radians, sin
from config import FontConfig as fc
from glyphs.accents import Accent


class Ogonek(Accent):
    """Hook hanging below the baseline: it leaves the letter heading
    diagonally down-left, then flattens along the bottom into a tail
    pointing right."""

    name = "ogonek"
    unicode = "0x2DB"
    depth = 0.95  # Below the baseline, as a fraction of the descender
    lean = 0.22  # How far the bowl swings left, as a fraction of the body width
    reach = 0.32  # Tail end, right of the hook's center, as a fraction of the body width
    angle = 32  # Initial direction, in degrees from vertical, towards the left
    stem_ratio = 1.0  # Default start width, relative to stroke_x
    tail_ratio = 1.0  # Weight of the flat bottom at the tail end, relative to stroke_y
    tension = 0.6  # Curve handle length, as a fraction of each segment's span
    inner_turn = 0.5  # Inner edge turn point, right of the outer one, in start widths

    def draw_at(self, pen, dc, x, y, width=None, start=0, flush=False):
        """`x` is the center of the hook where it leaves the letter, `y` the
        line it hangs from and `width` its horizontal span there (by default
        a stem width), so it can cover the full stem it protrudes from.
        `start` is the height above `y` where the hook begins; the bottom
        stays at the same depth below `y` whatever the start. With `flush`,
        both edges drop straight to the start line before curving, so the
        hook continues the stem's edges instead of notching in."""
        w0 = width if width is not None else self.stem_ratio * dc.stroke_x
        w1 = self.tail_ratio * dc.stroke_y
        a = radians(self.angle)
        dx, dy = -sin(a), -cos(a)  # Shared initial direction of both edges

        # Overlap the letter by half a stroke so the hook joins it cleanly.
        overlap_top = y + start + dc.stroke_y / 2
        top = y + start if flush else overlap_top
        bottom = y - self.depth * abs(dc.descent)
        lean = self.lean * dc.width
        x_end = min(
            x + self.reach * dc.width, fc.window_width - fc.min_margin_lowercase
        )

        def edge(x0, y_bottom, x_turn):
            drop = top - y_bottom
            run = x_end - x_turn
            return (
                (x0, top),
                (x0 + dx * self.tension * drop / cos(a), top + dy * self.tension * drop),
                (x_turn - self.tension * run * 0.5, y_bottom),
                (x_end, y_bottom),
            )

        # Outer edge swings further left and lower; the inner edge turns
        # tighter and sits w1 above it at the tail.
        outer = edge(x - w0 / 2, bottom, x - lean)
        inner = edge(x + w0 / 2, bottom + w1, x - lean + self.inner_turn * w0)

        if flush:
            pen.moveTo((outer[0][0], overlap_top))
            pen.lineTo(outer[0])
        else:
            pen.moveTo(outer[0])
        pen.curveTo(*outer[1:])
        pen.lineTo(inner[3])
        pen.curveTo(inner[2], inner[1], inner[0])
        if flush:
            pen.lineTo((inner[0][0], overlap_top))
        pen.closePath()

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=0)
