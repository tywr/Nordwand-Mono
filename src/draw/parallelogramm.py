from math import sqrt, atan2, sin, cos
from draw.polygon import draw_polygon


def _solve_parallelogram_stroke(
    stroke_x, stroke_y, x1, y1, x2, y2, tol=1e-6, max_iter=100
):
    w = max(x2, x1) - min(x2, x1)
    h = max(y2, y1) - min(y2, y1)

    # Initial guess: angle of the bare diagonal (delta=0)
    theta = atan2(h, w)

    for _ in range(max_iter):
        s = sqrt((stroke_x * sin(theta)) ** 2 + (stroke_y * cos(theta)) ** 2)

        denom = h**2 - s**2
        if abs(denom) < 1e-12:
            break  # degenerate case

        inner = w**2 + h**2 - s**2
        if inner < 0:
            break  # stroke too thick for this geometry

        delta = (s * (h * sqrt(inner) - s * w)) / denom
        new_theta = atan2(h, w - delta)

        if abs(new_theta - theta) < tol:
            theta = new_theta
            break

        theta = new_theta

    s = sqrt((stroke_x * sin(theta)) ** 2 + (stroke_y * cos(theta)) ** 2)
    denom = h**2 - s**2
    delta = (s * (h * sqrt(w**2 + h**2 - s**2) - s * w)) / denom

    return s, delta, theta


def draw_parallelogramm_legacy(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    direction="top-right",
    no_draw=False,
    delta=None,
):
    if delta is None:
        # w = max(x2, x1) - min(x2, x1)
        # h = max(y2, y1) - min(y2, y1)
        s, delta, theta = _solve_parallelogram_stroke(
            stroke_x, stroke_y, x1, y1, x2, y2
        )
        # s = sqrt((stroke_x * cos(theta)) ** 2 + (stroke_y * sin(theta)) ** 2)
        # delta = (s * (h * sqrt(w**2 + h**2 - s**2) - s * w)) / (h**2 - s**2)
        # theta = atan2(h, w - delta)
    else:
        # Forced delta — derive theta from the slanted-edge geometry:
        # the slanted edge has horizontal run w and vertical run h - delta,
        # so theta (angle from vertical) = atan2(w, h - delta).
        w = max(x2, x1) - min(x2, x1)
        h = max(y2, y1) - min(y2, y1)
        theta = atan2(w, h - delta)
    if no_draw:
        return theta, delta
    if direction == "top-right":
        draw_polygon(
            pen, points=[(x1, y1), (x1 + delta, y1), (x2, y2), (x2 - delta, y2)]
        )
        return theta, delta
    elif direction == "bottom-right":
        draw_polygon(
            pen, points=[(x2 - delta, y2), (x2, y2), (x1 + delta, y1), (x1, y1)]
        )
        return theta, delta
    if direction == "top-left":
        draw_polygon(
            pen, points=[(x1, y1), (x2 + delta, y2), (x2, y2), (x1 - delta, y1)]
        )
        return theta, delta
    elif direction == "bottom-left":
        draw_polygon(
            pen, points=[(x1, y1), (x1 - delta, y1), (x2, y2), (x2 + delta, y2)]
        )
        return theta, delta
    else:
        raise ValueError("Value should be either `top` or `bottom`")


def parallelogramm_delta(stroke, x1, y1, x2, y2):
    """Horizontal width of a slanted band from (x1, y1) to (x2, y2) whose
    perpendicular thickness is `stroke`.

    The band's long edges run from (x1, y1) to (x2 - delta, y2) and from
    (x1 + delta, y1) to (x2, y2), so with w and h the spans and phi the
    edges' angle from vertical, stroke = delta * cos(phi). Solving
    stroke^2 * (h^2 + (w - delta)^2) = delta^2 * h^2 for delta gives the
    closed form below.
    """
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    t = stroke
    if h <= t:
        raise ValueError(f"Band height {h} must exceed its stroke {t}")
    return t * (h * sqrt(w**2 + h**2 - t**2) - t * w) / (h**2 - t**2)


def draw_parallelogramm(
    pen,
    stroke,
    x1,
    y1,
    x2,
    y2,
    direction="top-right",
    no_draw=False,
    overwrite_section=None,
):
    """Slanted band with horizontal ends, from (x1, y1) to (x2, y2), drawn
    with a perpendicular thickness of `stroke` whatever its angle, so the
    same stroke gives the same weight on any diagonal and scales linearly
    across weights. Returns (phi, delta): the long edges' angle from
    vertical and the horizontal width of the ends.

    `overwrite_section` forces that horizontal width instead, e.g. the
    `delta` returned by another parallelogramm, so the two share the same
    section and join flush. `stroke` is then ignored, and the thickness
    follows from the section and the angle."""
    if overwrite_section is None:
        delta = parallelogramm_delta(stroke, x1, y1, x2, y2)
    else:
        delta = overwrite_section
    phi = atan2(abs(x2 - x1) - delta, abs(y2 - y1))
    if no_draw:
        return phi, delta
    if direction == "top-right":
        points = [(x1, y1), (x1 + delta, y1), (x2, y2), (x2 - delta, y2)]
    elif direction == "bottom-right":
        points = [(x2 - delta, y2), (x2, y2), (x1 + delta, y1), (x1, y1)]
    elif direction == "top-left":
        points = [(x1, y1), (x2 + delta, y2), (x2, y2), (x1 - delta, y1)]
    elif direction == "bottom-left":
        points = [(x1, y1), (x1 - delta, y1), (x2, y2), (x2 + delta, y2)]
    else:
        raise ValueError(f"Unknown direction {direction}")
    draw_polygon(pen, points=points)
    return phi, delta


def _solve_parallelogram_stroke_vertical(
    stroke_x, stroke_y, x1, y1, x2, y2, tol=1e-6, max_iter=100
):
    w = max(x2, x1) - min(x2, x1)
    h = max(y2, y1) - min(y2, y1)

    # Initial guess: angle of the bare diagonal
    theta = atan2(w, h)

    for _ in range(max_iter):
        s = sqrt((stroke_y * sin(theta)) ** 2 + (stroke_x * cos(theta)) ** 2)

        denom = w**2 - s**2
        if abs(denom) < 1e-12:
            break
        inner = w**2 + h**2 - s**2
        if inner < 0:
            break

        delta = (s * (w * sqrt(inner) - s * h)) / denom
        new_theta = atan2(w, h - delta)

        if abs(new_theta - theta) < tol:
            theta = new_theta
            break

        theta = new_theta

    s = sqrt((stroke_y * sin(theta)) ** 2 + (stroke_x * cos(theta)) ** 2)
    denom = w**2 - s**2
    delta = (s * (w * sqrt(w**2 + h**2 - s**2) - s * h)) / denom

    return s, delta, theta


def draw_parallelogramm_vertical(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    direction="top-right",
    no_draw=False,
    delta=None,
):
    """Parallelogram with vertical parallel sides and slanted top/bottom."""
    if delta is None:
        s, delta, theta = _solve_parallelogram_stroke_vertical(
            stroke_x, stroke_y, x1, y1, x2, y2
        )
    else:
        # Forced delta — derive theta from the slanted-edge geometry:
        # the slanted edge has horizontal run w and vertical run h - delta,
        # so theta (angle from vertical) = atan2(w, h - delta).
        w = max(x2, x1) - min(x2, x1)
        h = max(y2, y1) - min(y2, y1)
        theta = atan2(w, h - delta)
    if no_draw:
        return theta, delta
    if direction == "top-right":
        draw_polygon(
            pen, points=[(x1, y1), (x2, y2 - delta), (x2, y2), (x1, y1 + delta)]
        )
        return theta, delta
    elif direction == "bottom-right":
        draw_polygon(
            pen,
            points=[
                (x1, y1),
                (x1, y1 - delta),
                (x2, y2),
                (x2, y2 + delta),
            ],
        )
        return theta, delta
    elif direction == "top-left":
        draw_polygon(
            pen,
            points=[
                (x1, y1),
                (x1, y1 + delta),
                (x2, y2),
                (x2, y2 - delta),
            ],
        )
        return theta, delta
    elif direction == "bottom-left":
        draw_polygon(
            pen, points=[(x1, y1), (x2, y2 + delta), (x2, y2), (x1, y1 - delta)]
        )
        return theta, delta
    else:
        raise ValueError("Value should be either `top` or `bottom`")


def draw_smooth_parallelogramm_vertical(
    pen,
    delta,
    x1,
    y1,
    x2,
    y2,
    radius=20,
    direction="top-right",
):
    """Parallelogram with"""
    w = max(x2, x1) - min(x2, x1)
    h = max(y2, y1) - min(y2, y1)
    theta = atan2(w, h - delta)

    if direction == "top-right":
        pen.moveTo((x1, y1))
        pen.curveTo((x1, y1), (x1 + radius, y1), (x2, y2 - delta))
        pen.lineTo((x2, y2))
        pen.curveTo((x2, y2), (x1 + radius, y1 + delta), (x1, y1 + delta))
        pen.closePath()
        return theta, delta

    elif direction == "bottom-right":
        pen.moveTo((x1, y1))
        pen.lineTo((x1, y1 - delta))
        pen.curveTo((x1 + radius, y1 - delta), (x2, y2), (x2, y2))
        pen.lineTo((x2, y2 + delta))
        pen.curveTo((x2, y2 + delta), (x1 + radius, y1), (x1, y1))
        pen.closePath()
        return theta, delta

    elif direction == "top-left":
        pen.moveTo((x1, y1))
        pen.lineTo((x1, y1 + delta))
        pen.curveTo((x1, y1 + delta), (x1 - radius, y1 + delta), (x2, y2))
        pen.lineTo((x2, y2 - delta))
        pen.curveTo((x2, y2 - delta), (x1 - radius, y1), (x1, y1))
        pen.closePath()
        return theta, delta

    elif direction == "bottom-left":
        pen.moveTo((x1, y1))
        pen.curveTo((x1, y1), (x1 - radius, y1), (x2, y2 + delta))
        pen.lineTo((x2, y2))
        pen.curveTo((x2, y2), (x1 - radius, y1 - delta), (x1, y1 - delta))
        pen.closePath()
        return theta, delta
    else:
        raise ValueError("Value should be either `top` or `bottom`")
