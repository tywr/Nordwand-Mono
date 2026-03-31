def draw_cross_curve(
    pen,
    stroke,
    x1, y1,
    x2, y2,
    hx, hy,
):
    """Draw a center-symmetric S-curve stroke from (x1,y1) to (x2,y2).

    The curve starts at the bottom-left corner, crosses through the center
    of the bounding box, and ends at the top-right corner.
    The stroke is drawn inside the bounding box.

    At the corners the tangent is vertical; at the center it is horizontal.
    """
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    hw = (x2 - x1) / 2
    hh = (y2 - y1) / 2
    ihx = hx * (hw - stroke) / hw if hw > 0 else 0
    ihy = hy * (hh - stroke) / hh if hh > 0 else 0

    s2 = stroke / 2

    pen.moveTo((x1, y1))
    # Left edge, bottom half
    pen.curveTo((x1, y1 + hy), (mid_x - hx, mid_y + s2), (mid_x, mid_y + s2))
    # Left edge, top half
    pen.curveTo((mid_x + ihx, mid_y + s2), (x2 - stroke, y2 - ihy), (x2 - stroke, y2))
    # Top-right cap
    pen.lineTo((x2, y2))
    # Right edge, top half
    pen.curveTo((x2, y2 - hy), (mid_x + hx, mid_y - s2), (mid_x, mid_y - s2))
    # Right edge, bottom half
    pen.curveTo((mid_x - ihx, mid_y - s2), (x1 + stroke, y1 + ihy), (x1 + stroke, y1))
    pen.closePath()
