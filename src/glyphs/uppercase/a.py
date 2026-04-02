from math import atan, sin, cos
from config import FontConfig as fc
from glyph import Glyph
from shapes.polygon import draw_polygon
from shapes.rect import draw_rect


class UppercaseAGlyph(Glyph):
    name = "uppercase_a"
    unicode = "0x41"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 0
        width = 420
        bar_height = 320

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset
        xmid = x1 + (x2 - x1) / 2

        a = width / 2
        b = fc.ascent
        theta = atan(b / a)
        x_delta = stroke / sin(theta)

        draw_polygon(
            pen,
            points=[
                (xmid + x_delta / 2, fc.ascent),
                (xmid + width / 2 + x_delta / 2, 0),
                (xmid + width / 2 - x_delta / 2, 0),
                (xmid - x_delta / 2, fc.ascent),
            ],
        )
        draw_polygon(
            pen,
            points=[
                (xmid + x_delta / 2, fc.ascent),
                (xmid - width / 2 + x_delta / 2, 0),
                (xmid - width / 2 - x_delta / 2, 0),
                (xmid - x_delta / 2, fc.ascent),
            ],
        )
        draw_polygon(
            pen,
            points=[
                (xmid + width / 2 - bar_height * cos(theta), bar_height * sin(theta)),
                (xmid + width / 2 - (bar_height - stroke) * cos(theta), (bar_height - stroke) * sin(theta)),
                (xmid - width / 2 + (bar_height - stroke) * cos(theta), (bar_height - stroke) * sin(theta)),
                (xmid - width / 2 + bar_height * cos(theta), bar_height * sin(theta)),
            ],
        )
