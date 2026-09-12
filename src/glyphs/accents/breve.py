from glyphs.accents import Accent
from draw.loop import draw_loop


class Breve(Accent):
    name = "breve"
    unicode = "0x306"
    height = 0.5
    offset_y = 0.05
    width = 1.1
    stroke_ratio = 1.1
    hx_ratio = 0.5
    hy_ratio = 0.5

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        w = self.width * dc.width
        x1, x2 = x - w / 2, x + w / 2
        y1, y2 = y - h / 2, y + h / 2
        hx = dc.hx * self.hx_ratio
        hy = dc.hy * self.hy_ratio
        oy = self.offset_y * dc.x_height

        draw_loop(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            x1,
            y1 + oy,
            x2,
            y2 + oy,
            hx,
            hy,
            cut="top",
        )
