from glyphs import LigatureGlyph
from draw.chevron import draw_chevron
from glyphs.special.greater_than_sign import GreaterThenSignGlyph
from glyphs.special.hyphen_minus import HyphenMinusGlyph
from draw.rect import draw_rect


class RightArrowGlyph(LigatureGlyph):
    """Ligature glyph for ->"""

    name = "right_arrow_liga"
    components = ["hyphen_minus", "greater_than_sign"]
    feature_tags = (
        "liga",
        "ss02",
    )
    number_characters = 2
    joinable = True
    # Notch where the two cells meet, like the junctions of `----` (dlig),
    # showing the ligature stands for two characters
    dent = True
    width_ratio = 0.88
    overlap = 0.6
    side_offset = 0.05
    span = GreaterThenSignGlyph.span
    gap = 0.0
    stroke_ratio = 1

    def draw(self, pen, dc, join_left=False):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        x1 = self.side_offset * dc.window_width
        hyphen = HyphenMinusGlyph()
        if join_left:
            # Start where the junction of the `-` before ends, as thick as it
            s = hyphen.horizontal_bar_stroke(dc)
            x1 = s * hyphen.ligature_junction_width / 2
        g = self.gap * dc.window_width
        _, delta = draw_chevron(
            pen,
            self.stroke_ratio * dc.stroke_x,
            b.x2 + dc.window_width,
            b.x1 + dc.window_width,
            ymid,
            h,
        )
        x2 = b.x2 + dc.window_width - delta - g
        if not self.dent:
            draw_rect(pen, x1, ymid - s / 2, x2, ymid + s / 2)
            return
        w = dc.window_width
        jw = s * hyphen.ligature_junction_width
        d = s * hyphen.ligature_dent_stroke
        draw_rect(pen, x1, ymid - s / 2, w - jw / 2, ymid + s / 2)
        draw_rect(pen, w - jw / 2, ymid - d / 2, w + jw / 2, ymid + d / 2)
        draw_rect(pen, w + jw / 2, ymid - s / 2, x2, ymid + s / 2)
