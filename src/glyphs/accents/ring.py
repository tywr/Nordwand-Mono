from glyphs.accents import Accent
from draw.superellipse_loop import draw_superellipse_loop


class Ring(Accent):
    name = "ring"
    unicode = "0x2DA"
    loop_ratio_x = 0.7
    loop_ratio_y = 0.45

    def draw_at(self, pen, dc, x, y):
        stroke = dc.stroke_alt
        rx, ry = self.loop_ratio_x, self.loop_ratio_y
        h = ry * dc.x_height
        w = rx * dc.width
        draw_superellipse_loop(
            pen,
            stroke,
            stroke,
            x - w / 2,
            y - h / 2,
            x + w / 2,
            y + h / 2,
            dc.hx * rx,
            dc.hy * ry,
        )
