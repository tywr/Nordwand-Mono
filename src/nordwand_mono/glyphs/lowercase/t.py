import math

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.cross_bar import cross_bar_stem
from nordwand_mono.draw.square_corner import draw_square_corner
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.polygon import draw_polygon


class LowercaseTGlyph(Glyph):
    name = "lowercase_t"
    unicode = "0x74"
    offset = -50
    width_ratio = 1.00
    rl_ratio = 0.58
    up_ratio = 0.39
    # Angle of the cut at the top of the stem, in degrees from the horizontal
    cut_angle = 35
    # The corner ends terminal_offset * width inside the right of the cross
    # bar; the stem stays on the body's center, see `cross_bar_stem`
    terminal_offset = 0
    centered_stem = True

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        x1, x2, xs, xt = cross_bar_stem(
            b, self.rl_ratio, self.terminal_offset, self.centered_stem
        )

        # Cross-bar at x_height
        draw_rect(pen, x1, dc.x_height - dc.stroke_y, x2, dc.x_height)
        # Corner curving down-right (shorter/flatter than f), at most half the
        # body past the stem, then a footer to the terminal
        corner_end = min(xs + b.width / 2, xt)
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xs - dc.stroke_x / 2,
            b.ymid,
            corner_end,
            0,
            orientation="bottom-right",
        )
        draw_rect(pen, corner_end, 0, xt, dc.stroke_y)

        glyph = ufoLib2.objects.Glyph()

        # Stem
        top = (1 + self.up_ratio) * dc.x_height
        draw_rect(glyph.getPen(), xs - dc.stroke_x / 2, b.ymid, xs + dc.stroke_x / 2, top)
        cut_glyph = ufoLib2.objects.Glyph()

        # From the top right of the stem, going down left at cut_angle
        right = xs + dc.stroke_x / 2
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (right, top),
                (x1, top - (right - x1) * math.tan(math.radians(self.cut_angle))),
                (x1, top),
            ],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
