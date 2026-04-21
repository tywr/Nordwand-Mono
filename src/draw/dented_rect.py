def draw_dented_rect(pen, x1, y1, x2, y2, dent=0.75, side="left"):
    """Draw a simple rectangle between two corner points."""
    if side == "left":
        h = (y2 - y1)
        pen.moveTo((x2, y1))
        pen.lineTo((x2, y2))
        pen.lineTo((x1, y2))
        pen.lineTo((x1, y2 - 0.5 * h))
        pen.lineTo((x1 + 0.5 * dent * h, y1))
        pen.closePath()
