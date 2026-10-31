import dataclasses

from glyphs.uppercase import UppercaseGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class NumeroSignGlyph(UppercaseGlyph):
    """A narrowed N followed by a small o-like loop hanging from the cap height."""

    name = "numero_sign"
    unicode = "0x2116"
    offset = 0
    counter_ratio = 0.12  # Inner diameter of the ring, relative to the cell width
    ring_stroke_ratio = 0.45  # Ring and bar strokes, relative to the regular ones
    n_stroke_ratio = 0.75  # The N strokes, relative to the regular ones
    gap = 0.05  # Between the N and the ring, relative to the cell width
    bar_gap = 0.06  # Between the ring and the bar below, relative to the cell width
    width_ratio = 1.22

    def draw(self, pen, dc):
        margin = dc.min_margin_uppercase
        # The counter keeps its size and the ring grows with the stroke
        s = self.ring_stroke_ratio * dc.stroke_x
        ring = self.counter_ratio * dc.window_width + 2 * s
        x1 = margin + self.offset
        x2 = dc.window_width - margin + self.offset

        # Ring, its top on the cap height and its right side on the margin.
        # Handles scaled from the lowercase o bowl to the ring's size.
        ring_bottom = dc.cap - ring
        draw_loop(
            pen,
            s,
            self.ring_stroke_ratio * dc.stroke_y,
            x2 - ring,
            ring_bottom,
            x2,
            dc.cap,
            dc.hx * ring / (dc.width + dc.stroke_x),
            dc.hy * ring / dc.x_height,
        )

        # Bar under the ring, as wide as it
        bar_top = ring_bottom - self.bar_gap * dc.window_width
        bar = self.ring_stroke_ratio * dc.stroke_y
        draw_rect(pen, x2 - ring, bar_top - bar, x2, bar_top)

        # N filling the room left of the ring. body_bounds spans
        # width * width_ratio + stroke_x, centered on the cell plus offset.
        snx = max(0, 0.2 * (dc.stroke_x - 90)) + min(90, dc.stroke_x) * self.n_stroke_ratio
        sny = max(0, 0.2 * (dc.stroke_y - 70)) + min(70, dc.stroke_y) * self.n_stroke_ratio
        ndc = dataclasses.replace(
            dc,
            stroke_x=snx,
            stroke_y=sny,
        )
        n_width = x2 - ring - self.gap * dc.window_width - x1
        n = UppercaseNGlyph()
        n.width_ratio = (n_width - ndc.stroke_x) / ndc.width
        n.offset = x1 + n_width / 2 - dc.window_width / 2
        n.draw(pen, ndc)
