from draw.descender import draw_right_descender


class RightDescenderGlyph:
    """Mixin drawing the base letter narrowed by `right_offset` on its right,
    then `draw_right_descender` in the room left (Ц Щ Җ).

    Narrowing goes through width_ratio and offset, so the strokes keep their
    weight. Put it before the base class: `class X(RightDescenderGlyph, BaseGlyph)`.
    """

    right_offset = 0.12  # Room for the descender, relative to the body width
    descent_ratio = 0.75
    base_kwargs = {}  # Passed to the base draw, e.g. {"draw_descender": False}
    # Thin the descender at heavy weights, like the stems of Ш and Ж
    damp_descender = False

    def draw(self, pen, dc):
        width_ratio, offset = self.width_ratio, self.offset
        b = dc.body_bounds(offset=offset, width_ratio=width_ratio)
        rx = b.x2 - self.right_offset * b.width
        self.width_ratio = (rx - b.x1 - dc.stroke_x) / dc.width
        self.offset = offset + (rx - b.x2) / 2
        try:
            super().draw(pen, dc, **self.base_kwargs)
        finally:
            self.width_ratio, self.offset = width_ratio, offset
        sx = dc.stroke_x * getattr(self, "stroke_x_ratio", 1)
        if self.damp_descender:
            sx = max(0, 0.8 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)
        sy = dc.stroke_y * getattr(self, "stroke_y_ratio", 1)
        draw_right_descender(
            pen, sx, sy, rx - sx, b.x2, self.descent_ratio * dc.descent
        )
