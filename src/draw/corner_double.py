def draw_corner_double(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    ox,
    oy,
    c=0.5,
    orientation="bottom-right",
):
    """Draw a solid quarter-curve corner with two control points.

    (x1, y1) is the outer start of the curve, (x2, y2) is the outer end.
    The stroke always goes inward (away from the corner).

    The corner point is at (x2, y1) or (x1, y2) depending on orientation:
        bottom-right: corner at (x2, y1) — curve goes right then up
        top-right:    corner at (x1, y2) — curve goes up then right
        top-left:     corner at (x2, y1) — curve goes left then down
        bottom-left:  corner at (x1, y2) — curve goes down then left
    """
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    a = (oy * h) / (ox * w)
    iw = abs(w - stroke_x)
    ih = abs(h - stroke_y)
    ihx = hx * (w - stroke_x) / w if w > 0 else 0
    ihy = hy * (h - stroke_y) / h if h > 0 else 0

    if orientation == "bottom":
        # Corner at (x1, y2). Start on right, end on bottom.
        ix1 = x1 - stroke_x
        iy1 = y1
        ix2 = x2
        iy2 = y2 + stroke_y

    elif orientation == "top-left":
        # Corner at (x1, y2). Start on right, end on top.
        ix1 = x1 - stroke_x
        iy1 = y1
        ix2 = x2
        iy2 = y2 - stroke_y

    elif orientation == "top-right":
        # Corner at (x1, y2). Start on left, end on top.
        ix1 = x1 + stroke_x
        iy1 = y1
        ix2 = x2
        iy2 = y2 - stroke_y
        imx2 = ix1 + ox * iw
        imy2 = iy1 + oy * ih

        pen.moveTo((ix1, iy1))
        pen.curveTo((ix1, iy1 + ihy), (imx2 - c * ihy / a, imy2 - c * ihy), (imx2, imy2))
        pen.curveTo((imx2 + c * ihy / a, imy2 + c * ihy), (ix2 - ihx, iy2), (ix2, iy2))
        # pen.curveTo((ix1 - ihx, iy1), (imx2 + 2 * ihy / a, imy2 + ihy), (imx2, imy2))
        # pen.curveTo((imx2 - 2 * ihy / a, imy2 - ihy), (ix2, iy2 + ihy), (ix2, iy2))
        pen.closePath()

    elif orientation == "bottom-right":
        # Corner at (x1, y2). Start on left, end on bottom.
        ix1 = x1 + stroke_x
        iy1 = y1
        ix2 = x2
        iy2 = y2 + stroke_y

    return hx, hy, ihx, ihy
