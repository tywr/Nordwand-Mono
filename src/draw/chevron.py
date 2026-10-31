from draw.parallelogramm import draw_parallelogramm


def draw_chevron(pen, stroke, x_tip, x_back, y, height):
    """Draw a `<` / `>` shaped point whose tip is at (x_tip, y).

    The chevron points right when x_tip > x_back and left otherwise. Its
    two strokes, of perpendicular thickness `stroke`, span `height`
    vertically, centered on `y`. Returns the (phi, delta) of the lower
    stroke, delta being the horizontal width of the tip.
    """
    points_right = x_tip > x_back
    draw_parallelogramm(
        pen,
        stroke,
        x_tip,
        y,
        x_back,
        y + height / 2,
        direction="top-left" if points_right else "top-right",
    )
    return draw_parallelogramm(
        pen,
        stroke,
        x_back,
        y - height / 2,
        x_tip,
        y,
        direction="top-right" if points_right else "top-left",
    )
