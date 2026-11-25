from nordwand_mono.glyphs.numbers.zero import ZeroGlyph


def _lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def _split_end(bezier, t):
    """Return the part of a cubic bezier after parameter t."""
    p0, p1, p2, p3 = bezier
    a, b, c = _lerp(p0, p1, t), _lerp(p1, p2, t), _lerp(p2, p3, t)
    d, e = _lerp(a, b, t), _lerp(b, c, t)
    return (_lerp(d, e, t), e, c, p3)


def _tangent_height(bezier, t, x):
    """Height at which the tangent line at parameter t crosses abscissa x."""
    (px, py), (dx, dy), _, _ = _split_end(bezier, t)
    return py + (x - px) * (dy - py) / (dx - px)


def _quarter(xm, ym, w, h, hx, hy, bulge, tip, sx, sy):
    """Beziers from the side point to the top/bottom point of one quarter:
    a near-straight flank up to the shoulder, then the untouched remainder of
    the superellipse quarter. The shoulder is the superellipse point whose
    tangent crosses the side point's vertical at height `tip`, so the flank
    and the superellipse share that tangent."""

    def p(dx, dy):
        return (xm + sx * dx, ym + sy * dy)

    corner = ((w, 0), (w, hy), (hx, h), (0, h))
    lo, hi = 1e-6, 1 - 1e-6
    for _ in range(60):
        mid = (lo + hi) / 2
        if _tangent_height(corner, mid, w + bulge) < tip:
            lo = mid
        else:
            hi = mid
    corner = _split_end(corner, lo)
    shoulder = corner[0]
    flank_handle = _lerp((w + bulge, tip), shoulder, 0.3)
    return [
        (p(w + bulge, 0), p(w + bulge, 0.55 * tip), p(*flank_handle), p(*shoulder)),
        tuple(p(*point) for point in corner),
    ]


def _reverse(beziers):
    return [b[::-1] for b in beziers[::-1]]


def _draw_bulged_loop(pen, x1, y1, x2, y2, hx, hy, bulge, tip, clockwise):
    args = ((x1 + x2) / 2, (y1 + y2) / 2, (x2 - x1) / 2, (y2 - y1) / 2)
    args += (hx, hy, bulge, tip)
    beziers = (
        _quarter(*args, 1, 1)
        + _reverse(_quarter(*args, -1, 1))
        + _quarter(*args, -1, -1)
        + _reverse(_quarter(*args, 1, -1))
    )
    if clockwise:
        beziers = _reverse(beziers)
    pen.moveTo(beziers[0][0])
    for _, c1, c2, end in beziers:
        pen.curveTo(c1, c2, end)
    pen.closePath()


class ZeroHexagonGlyph(ZeroGlyph):
    name = "zero_hexagon"
    font_feature = {"cv01": 2}
    width_ratio = 1.12
    bulge_ratio = 0.05
    tip_ratio = 0.4  # Relative to half-height
    alternative_character_comment = "Berkeley Mono zero style"

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            number=True,
        )
        sx, sy = self.get_strokes(dc)
        bulge = self.bulge_ratio * b.width / 2
        x1, x2 = b.x1 + bulge, b.x2 - bulge
        hx = self.hx_ratio * b.hx * (x2 - x1) / b.width
        hy = self.hy_ratio * b.hy
        tip = self.tip_ratio * b.height / 2

        _draw_bulged_loop(pen, x1, b.y1, x2, b.y2, hx, hy, bulge, tip, clockwise=False)

        # Inner contour: the outer box reduced by the stroke, handles scaled to match
        rx = (x2 - x1 - 2 * sx) / (x2 - x1)
        ry = (b.height - 2 * sy) / b.height
        _draw_bulged_loop(
            pen,
            x1 + sx,
            b.y1 + sy,
            x2 - sx,
            b.y2 - sy,
            hx * rx,
            hy * ry,
            bulge * ry,
            tip * ry,
            clockwise=True,
        )
        self.draw_mark(pen, dc, b)
