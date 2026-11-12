from glyphs import Glyph
from draw.square_corner import draw_square_corner
from draw.rect import draw_rect


class LowercaseFBase(Glyph):
    """Lowercase f: a stem with a corner to the top right and a cross bar,
    at the x-height or lower with `low_bar`. `bottom` ends the stem plainly
    (None), with a bar on the baseline ("serif"), or with a tail curving
    left into the descender ("hook")."""

    unicode = "0x66"
    offset = -36
    rl_ratio = 0.59
    width_ratio = 1.04
    low_bar = False
    # Top of the low cross bar, relative to the x-height
    low_bar_height = 0.88
    bottom_right_reach = 0.9
    bottom = None

    def bar_width(self, b, dc):
        """Width shared by the cross bar and the serif, kept the same across
        weights."""
        return dc.width + dc.default_stroke

    def cross_bar_top(self, dc):
        return (self.low_bar_height if self.low_bar else 1) * dc.x_height

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        width = self.bar_width(b, dc)
        right_len = width * self.rl_ratio - dc.stroke_x / 2
        left_len = width * (1 - self.rl_ratio) - dc.stroke_x / 2
        yc = self.cross_bar_top(dc)

        # Stem
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.x_height
        )

        # Cross-bar
        draw_rect(
            pen,
            b.xmid - left_len - dc.stroke_x / 2,
            yc - dc.stroke_y,
            b.xmid + right_len + dc.stroke_x / 2,
            yc,
        )

        # Corner
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - dc.stroke_x / 2,
            dc.x_height,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.ascent,
            orientation="top-right",
        )

        if self.bottom == "serif":
            # Centered on the stem, as long as the left of the cross bar
            draw_rect(
                pen,
                b.xmid - left_len - dc.stroke_x / 2,
                0,
                b.xmid + right_len * self.bottom_right_reach + dc.stroke_x / 2,
                dc.stroke_y,
            )
        elif self.bottom == "hook":
            draw_square_corner(
                pen,
                dc.stroke_x,
                dc.stroke_y,
                b.xmid + dc.stroke_x / 2,
                0,
                b.x1,
                dc.descent,
                orientation="bottom-left",
            )


class LowercaseFGlyph(LowercaseFBase):
    name = "lowercase_f"


class LowercaseF2Glyph(LowercaseFBase):
    name = "lowercase_f_2"
    default_italic = True
    offset = -22
    rl_ratio = 0.55
    width_ratio = 1.05
    bottom = "hook"

    def bar_width(self, b, dc):
        return b.width


class LowercaseF3Glyph(LowercaseFGlyph):
    name = "lowercase_f_3"
    font_feature = {"ss20": 1}
    low_bar = True


class LowercaseF4Glyph(LowercaseF2Glyph):
    name = "lowercase_f_4"
    font_feature = {"ss20": 1}
    default_italic = False
    italic_only = True
    low_bar = True


class LowercaseF5Glyph(LowercaseFGlyph):
    name = "lowercase_f_5"
    font_feature = {"cv11": 1, "ss01": 1}
    regular_only = True
    bottom = "serif"


class LowercaseF6Glyph(LowercaseF5Glyph):
    name = "lowercase_f_6"
    font_feature = {"ss20": 1}
    # ss20 on top of cv11
    alternate_of = "lowercase_f_5"
    low_bar = True
