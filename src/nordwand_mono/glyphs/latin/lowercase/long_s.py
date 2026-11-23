from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.square_corner import draw_square_corner
from nordwand_mono.draw.rect import draw_rect


class LowercaseLongSGlyph(Glyph):
    name = "lowercase_long_s"
    unicode = "0x17F"
    offset = -36
    width_ratio = 1.04
    rl_ratio = 0.59  # Share of the width right of the stem center, as in f

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        width = dc.width + dc.default_stroke
        right_len = width * self.rl_ratio - dc.stroke_x / 2

        # Stem
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.x_height
        )
        # Corner curving right at the top
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - dc.stroke_x / 2,
            dc.x_height,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.ascent,
            gx=dc.square_corner_gx,
            gy=dc.square_corner_gy,
            orientation="top-right",
        )
