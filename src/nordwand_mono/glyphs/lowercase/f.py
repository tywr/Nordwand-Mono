from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.cross_bar import cross_bar_stem
from nordwand_mono.draw.square_corner import draw_square_corner
from nordwand_mono.draw.rect import draw_rect


class LowercaseFBase(Glyph):
    """Lowercase f: a stem with a corner to the top right and a cross bar,
    at the x-height or lower with `low_bar`. `bottom` ends the stem plainly
    (None), with a bar on the baseline ("serif"), or with a tail curving
    left into the descender ("hook")."""

    unicode = "0x66"
    offset = -36
    rl_ratio = 0.59
    width_ratio = 1.00
    low_bar = False
    # Top of the low cross bar, relative to the x-height
    low_bar_height = 0.92
    bottom_right_reach = 0.9
    bottom = None
    cross_bar = True
    # The corner ends terminal_offset * width inside the right of the cross
    # bar; the stem stays on the body's center, see `cross_bar_stem`
    terminal_offset = 0
    centered_stem = True
    stroke_y_dampening = 0.75 
    mid_shift_coef = 0
    expand_factor = 0.9

    def cross_bar_top(self, dc):
        return (self.low_bar_height if self.low_bar else 1) * dc.x_height

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio, expand_factor=self.expand_factor
        )
        sx, sy = self.get_strokes(dc)
        x1, x2, xs, xt = cross_bar_stem(
            b, self.rl_ratio, self.terminal_offset, self.centered_stem
        )
        yc = self.cross_bar_top(dc)

        # Add slight offset as weight increase
        xs += self.mid_shift_coef * (sx - dc.default_stroke)

        # Stem
        draw_rect(pen, xs - sx / 2, 0, xs + sx / 2, dc.x_height)

        # Cross-bar
        if self.cross_bar:
            draw_rect(pen, x1, yc - dc.stroke_y, x2, yc)

        # Corner, to the terminal
        draw_square_corner(
            pen,
            sx,
            sy,
            xs - sx / 2,
            dc.x_height,
            xt,
            dc.ascent,
            gx=dc.square_corner_gx,
            gy=dc.square_corner_gy,
            orientation="top-right",
        )

        if self.bottom == "serif":
            # From the left of the cross bar, reaching bottom_right_reach of
            # the way from the stem to the terminal
            right_len = xt - xs - sx / 2
            draw_rect(
                pen,
                x1,
                0,
                xs + right_len * self.bottom_right_reach + sx / 2,
                dc.stroke_y,
            )
        elif self.bottom == "hook":
            # Half the body left of the stem
            draw_square_corner(
                pen,
                sx,
                sy,
                xs + sx / 2,
                0,
                xs - b.width / 2,
                dc.descent,
                gx=dc.square_corner_gx,
                gy=dc.square_corner_gy,
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
    alternative_character_comment = "Only applies in regular font"
    bottom = "serif"


class LowercaseF6Glyph(LowercaseF5Glyph):
    name = "lowercase_f_6"
    font_feature = {"ss20": 1}
    # ss20 on top of cv11
    alternate_of = "lowercase_f_5"
    low_bar = True
