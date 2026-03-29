from config import FontConfig as fc
from glyphs.base import superellipse_ear


def draw_d(
    pen,
    stroke: int,
    taper=None,
    taper_ratio=1.0,
    center_x=None,
    x_ratio=1.0,
    height=None,
):
    x1 = fc.width / 2 - fc.o_width / 2 - stroke / 2
    y1 = 0
    x2 = fc.width / 2 + fc.o_width / 2 + stroke / 2
    y2 = fc.x_height
    superellipse_ear.draw_superellipse_ear(
        pen,
        stroke,
        x1,
        y1,
        x2,
        y2,
        fc.o_hx,
        fc.o_hy,
        fc.tooth,
        side="right",
    )
