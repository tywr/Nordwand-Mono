from draw.rect import draw_rect


def dot_size(dc, ratio):
    """Optically even dot (width, height) for the current weight.

    `ratio` is the dot size relative to the stroke at the regular weight.
    Growing with stroke ** dot_exponent (< 1) makes dots relatively bigger in
    thin weights and smaller in bold ones. The height borrows dot_squash of
    the x/y stroke contrast so the dot doesn't look tall.
    """
    w = ratio * dc.default_stroke * (dc.stroke_x / dc.default_stroke) ** dc.dot_exponent
    h = w * (dc.stroke_y / dc.stroke_x) ** dc.dot_squash
    return w, h


def draw_dot(pen, dc, x, y, ratio):
    """Dot centered on (x, y)."""
    w, h = dot_size(dc, ratio)
    draw_rect(pen, x - w / 2, y - h / 2, x + w / 2, y + h / 2)
    return w, h
