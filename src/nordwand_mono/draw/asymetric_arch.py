def draw_asymetric_arch(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    x3,
    y3,
    hx,
    hy,
    taper=0.5,
):
    """Bottom arch whose two ends sit at different heights, as the bowl of
    the a reaching up to its stem.

    The plain side leaves the left edge x1 at height y3 going down and
    reaches the bottom y1 at x3, then the tapered side rises to height y2 at
    the right edge x2 (x1 < x3 < x2, y1 < y3 < y2). As on a right taper of
    `draw_arch`, the tapered end is `taper` * stroke_x thick and its inner
    side lies stroke_x inside x2, so a stem drawn at x2 covers it.

    `hx` and `hy` are the handles of a quarter (x2 - x1) / 2 wide and
    y2 - y1 high, each quarter scaling them to its own size."""
    w, h = (x2 - x1) / 2, y2 - y1
    sx, sy = stroke_x, stroke_y
    xo2 = x2 - sx + taper * sx
    xi2 = x2 - sx

    def quarters(left, right, bottom):
        """Left quarter from (left, y3) down to (x3, bottom), then right
        quarter from there up to (right, y2)."""
        lw, lh = x3 - left, y3 - bottom
        rw, rh = right - x3, y2 - bottom
        return (
            ((left, y3), (left, y3 - hy * lh / h), (x3 - hx * lw / w, bottom), (x3, bottom)),
            ((x3, bottom), (x3 + hx * rw / w, bottom), (right, y2 - hy * rh / h), (right, y2)),
        )

    outer = quarters(x1, xo2, y1)
    inner = [seg[::-1] for seg in reversed(quarters(x1 + sx, xi2, y1 + sy))]

    pen.moveTo(outer[0][0])
    for seg in outer:
        pen.curveTo(*seg[1:])
    pen.lineTo(inner[0][0])
    for seg in inner:
        pen.curveTo(*seg[1:])
    pen.closePath()
