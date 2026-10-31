from shapes.superellipse import Superellipse


def draw_loop(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    cut=None,
    quarter=None,
) -> dict:
    """Stroked superellipse. `cut` removes one half of it, while `quarter`
    ("top-right", "top-left", "bottom-left" or "bottom-right") only keeps
    that quarter."""
    outer_se = Superellipse(x1=x1, y1=y1, x2=x2, y2=y2, hx=hx, hy=hy)
    inner_se = outer_se.reduce(
        right=stroke_x, left=stroke_x, top=stroke_y, bottom=stroke_y
    )

    if quarter is None:
        outer_se.draw(pen, clockwise=False, cut=cut)
        inner_se.draw(pen, clockwise=True, cut=cut)
    else:
        o0, o1, o2, o3 = outer_se.quarter(quarter)
        i0, i1, i2, i3 = inner_se.quarter(quarter)
        pen.moveTo(o0)
        pen.curveTo(o1, o2, o3)
        pen.lineTo(i3)
        pen.curveTo(i2, i1, i0)
        pen.closePath()

    return {
        "outer": outer_se,
        "inner": inner_se,
    }
