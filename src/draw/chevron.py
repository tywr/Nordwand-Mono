from draw.parallelogramm import draw_parallelogramm_legacy


def draw_chevron(pen, stroke_x, stroke_y, x_tip, x_back, y, height, delta):
    """Draw a `<` / `>` shaped point whose tip is at (x_tip, y).

    The chevron points right when x_tip > x_back and left otherwise. Its
    two strokes span `height` vertically, centered on `y`. Returns the
    (theta, delta) of the lower stroke.
    """
    points_right = x_tip > x_back
    draw_parallelogramm_legacy(
        pen,
        stroke_x,
        stroke_y,
        x_tip,
        y,
        x_back,
        y + height / 2,
        direction="top-left" if points_right else "top-right",
        delta=delta,
    )
    return draw_parallelogramm_legacy(
        pen,
        stroke_x,
        stroke_y,
        x_back,
        y - height / 2,
        x_tip,
        y,
        direction="top-right" if points_right else "top-left",
        delta=delta,
    )
