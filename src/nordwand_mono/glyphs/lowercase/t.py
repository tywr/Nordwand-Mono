import math

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
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

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        right_len = b.width * self.rl_ratio - dc.stroke_x / 2
        left_len = b.width * (1 - self.rl_ratio) - dc.stroke_x / 2

        # Cross-bar at x_height
        draw_rect(
            pen,
            b.xmid - left_len - dc.stroke_x / 2,
            dc.x_height - dc.stroke_y,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.x_height,
        )
        # Corner curving down-right (shorter/flatter than f)
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - dc.stroke_x / 2,
            b.ymid,
            b.xmid + b.width / 2,
            0,
            orientation="bottom-right",
        )
        # Footer extension from corner to right edge
        draw_rect(
            pen,
            b.xmid + b.width / 2,
            0,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.stroke_y,
        )

        glyph = ufoLib2.objects.Glyph()

        # Stem
        draw_rect(
            glyph.getPen(),
            b.xmid - dc.stroke_x / 2,
            b.ymid,
            b.xmid + dc.stroke_x / 2,
            (1 + self.up_ratio) * dc.x_height,
        )
        cut_glyph = ufoLib2.objects.Glyph()

        # From the top right of the stem, going down left at cut_angle
        x2, top = b.xmid + dc.stroke_x / 2, (1 + self.up_ratio) * dc.x_height
        x1 = b.xmid - left_len - dc.stroke_x / 2
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (x2, top),
                (x1, top - (x2 - x1) * math.tan(math.radians(self.cut_angle))),
                (x1, top),
            ],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
