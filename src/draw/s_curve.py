from math import tan, cos, sin
from draw.parallelogramm import draw_parallelogramm_vertical


def draw_s_curve(
    pen,
    sx: float,
    sy: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    hx: float,
    hy: float,
    height: float,
    angle: float,
) -> None:
    rhy = 1.5
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
    s = (sx + sy) / 2
    ihx, ihy = hx - sx, hy - sy

    dx = 50
    dy = 50
    theta, delta = draw_parallelogramm_vertical(
        pen,
        sx,
        sy,
        xm + dx,
        ym - dy,
        xm - dx,
        ym + dy,
    )
    
    # Upper part, from parallelogramm, to top-left
    pen.moveTo((xm - dx, ym + dy))
    pen.curveTo((xm - dx - sin(theta) * ihx, ym + dy + cos(theta) * ihx), (x1 + sx, y2 - ihy), (x1 + sx, y2))
    pen.lineTo((x1, y2))
    pen.curveTo((x1, y2 - ihy * rhy), (xm - dx - sin(theta) * hx, ym + dy - delta + cos(theta) * hx), (xm - dx, ym + dy - delta))
    print(theta, delta)
