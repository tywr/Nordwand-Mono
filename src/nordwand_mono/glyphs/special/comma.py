from fontTools.misc.roundTools import otRound

from nordwand_mono.draw.polygon import draw_polygon
from nordwand_mono.glyphs import Glyph


class CommaGlyph(Glyph):
    name = "comma"
    unicode = "0x2C"
    offset = 0
    width_ratio = 1
    height_ratio = 0.75
    vertical_offset = 0.25
    foot_offset = 0.15
    taper = 0.66
    stroke_ratio = 1.2

    def points(self, dc):
        body = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        height = self.height_ratio * body.height
        stroke = self.stroke_ratio * dc.stroke_x
        top = self.vertical_offset * body.height
        foot_offset = self.foot_offset * body.width

        # Use grid-aligned edges so the upright head stays square in TTF.
        left = otRound(body.xmid - stroke / 2)
        right = otRound(body.xmid + stroke / 2)
        head_width = right - left
        top_y = otRound(top)
        bend_y = top_y - head_width

        foot_y = otRound(top - height + stroke)
        foot_left = otRound(body.xmid - stroke / 2 - foot_offset)
        # Pull the right edge in farther to accentuate its turn into the tail.
        foot_right = otRound(
            body.xmid + self.taper * stroke / 2 - foot_offset - 0.08 * head_width
        )

        return [
            (left, top_y),
            (right, top_y),
            (right, bend_y),
            (foot_right, foot_y),
            (foot_left, foot_y),
            (left, bend_y),
        ]

    def draw(self, pen, dc):
        draw_polygon(pen, points=self.points(dc))
