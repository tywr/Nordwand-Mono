from draw.rect import draw_rect


def draw_right_descender(pen, stroke_x, stroke_y, x1, x2, descent):
    """Bottom bar from x1 out to x2, ending in a stem going down to `descent`
    on the right (Ц Щ Җ)."""
    draw_rect(pen, x1, 0, x2, stroke_y)
    draw_rect(pen, x2 - stroke_x, descent, x2, stroke_y)
