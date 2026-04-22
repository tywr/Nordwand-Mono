from glyphs import LigatureGlyph
from draw.dented_rect import draw_dented_rect


class DoubleHyphenGlyph(LigatureGlyph):
    """Ligature glyph for -- (two consecutive underscores).

    Draws a single continuous bar spanning the full width of two cells
    (2 * window_width), creating a seamless connection between underscores.
    """

    name = "double_hyphen"
    components = ["hyphen_minus", "hyphen_minus"]
    number_characters = 2
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sy = dc.stroke_y
        # Draw a bar that spans two full glyph widths edge-to-edge
        draw_dented_rect(
            pen, b.x1, dc.math - sy / 2, dc.window_width, dc.math + sy / 2, side="right"
        )
        draw_dented_rect(
            pen,
            dc.window_width,
            dc.math - sy / 2,
            b.x2 + dc.window_width,
            dc.math + sy / 2,
            side="left",
        )
