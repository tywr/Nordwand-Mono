from glyphs.accents import Accent
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class Cedilla(Accent):
    name = "cedilla"
    unicode = "0xB8"
    x_ratio = 0.4
    cut_ratio = 0.7
    stroke_ratio_x = 0.75
    stroke_ratio_y = 0.75
    stroke_y_dampening = 0.3
    neck_length = 0.05
    flat_ratio = 0.1
    slant_ratio = 1.25
    y_start = 0

    def draw_at(self, pen, dc, x, y):
        h = abs(dc.descent)
        w = self.x_ratio * dc.width
        wl = (1 - self.flat_ratio) * w
        yr = h / dc.x_height
        yn = -self.neck_length * dc.x_height
        esy = max(0, dc.stroke_y - 70)
        sx = self.stroke_ratio_x * dc.stroke_x
        sy = (
            self.stroke_ratio_y * min(dc.stroke_y, 70)
            + self.stroke_y_dampening * esy
        )
        sl = self.slant_ratio * sx

        # Neck: shorter than its stroke in bold, so it's sized by its
        # horizontal section rather than a perpendicular stroke
        draw_parallelogramm(
            pen,
            0,
            x - sl / 2,
            yn - sy,
            x + sl / 2,
            self.y_start,
            overwrite_section=sx,
        )
        draw_loop(
            pen,
            sx,
            sy,
            x - wl,
            yn - h,
            x + wl,
            yn,
            dc.hx * self.x_ratio,
            dc.hy * yr,
            cut="left",
        )
        draw_rect(
            pen,
            x - sl / 2,
            yn - h,
            x,
            yn - h + sy,
        )
