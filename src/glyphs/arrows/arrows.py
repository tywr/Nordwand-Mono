from math import radians

from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph
from draw.chevron import draw_chevron
from draw.polygon import draw_polygon
from draw.rect import draw_rect


class RightArrowGlyph(Glyph):
    """Base arrow, pointing right. The other arrows rotate it by `angle`
    (degrees, counterclockwise) around the centre of the cell at math height;
    `double` adds a head at the back, `filled_head` makes the head a solid
    triangle instead of a chevron."""

    name = "right_arrow"
    unicode = "0x2192"
    offset = 0
    side_offset_left = 0.05
    side_offset_right = 0.02
    width_ratio = 1.33
    overlap = 0.6
    span = 0.4
    arrow_width = 0.5
    stroke_ratio = 1
    angle = 0
    double = False
    # Size of the heads of double arrows, relative to a single arrow's head
    double_head_ratio = 0.6
    # Length of the arrow relative to the parenthesis, for arrows that need
    # more room than the cell width (e.g. vertical ones). None fits the width
    length_ratio = None
    filled_head = False

    def draw(self, pen, dc):
        ymid = dc.math
        if self.angle:
            xmid = dc.window_width / 2
            pen = TransformPen(
                pen,
                Transform()
                .translate(xmid, ymid)
                .rotate(radians(self.angle))
                .translate(-xmid, -ymid),
            )
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.stroke_ratio
        sy = s
        # With two heads, both ends sit at the head's offset
        left = self.side_offset_right if self.double else self.side_offset_left
        x1 = left * dc.window_width
        x2 = dc.window_width - self.side_offset_right * dc.window_width
        head = x2 - (1 - self.arrow_width) * dc.window_width
        if self.length_ratio:
            half = self.length_ratio * dc.parenthesis_length / 2
            x1, x2 = dc.window_width / 2 - half, dc.window_width / 2 + half
        if self.double:
            head *= self.double_head_ratio
            h *= self.double_head_ratio
        if self.filled_head:
            draw_polygon(pen, [(x2, ymid), (x2 - head, ymid + h / 2), (x2 - head, ymid - h / 2)])
            delta = 2 * head - 2  # The shaft overlaps the head by a unit
        else:
            _, delta = draw_chevron(pen, s, x2, x2 - head, ymid, h)
        if self.double:
            draw_chevron(pen, s, x1, x1 + head, ymid, h)
            x1 += delta / 2
        draw_rect(pen, x1, ymid - sy / 2, x2 - delta / 2, ymid + sy / 2)


class LeftArrowGlyph(RightArrowGlyph):
    name = "left_arrow"
    unicode = "0x2190"
    angle = 180


class UpArrowGlyph(RightArrowGlyph):
    name = "up_arrow"
    unicode = "0x2191"
    angle = 90


class DownArrowGlyph(RightArrowGlyph):
    name = "down_arrow"
    unicode = "0x2193"
    angle = -90


class LeftRightArrowGlyph(RightArrowGlyph):
    name = "left_right_arrow"
    unicode = "0x2194"
    double = True
    # Longer than the cell is wide, so both heads fit at full size: it
    # overflows into the neighbouring cells
    double_head_ratio = 0.85
    length_ratio = 0.55


class UpDownArrowGlyph(LeftRightArrowGlyph):
    name = "up_down_arrow"
    unicode = "0x2195"
    angle = 90


class NorthWestArrowGlyph(RightArrowGlyph):
    name = "north_west_arrow"
    unicode = "0x2196"
    angle = 135


class NorthEastArrowGlyph(RightArrowGlyph):
    name = "north_east_arrow"
    unicode = "0x2197"
    angle = 45


class SouthEastArrowGlyph(RightArrowGlyph):
    name = "south_east_arrow"
    unicode = "0x2198"
    angle = -45


class SouthWestArrowGlyph(RightArrowGlyph):
    name = "south_west_arrow"
    unicode = "0x2199"
    angle = -135


# Long arrows, longer than the cell: they overflow into the neighbouring cells


class LongRightArrowGlyph(RightArrowGlyph):
    name = "long_right_arrow"
    unicode = "0x27F6"
    length_ratio = 1


class LongLeftArrowGlyph(LongRightArrowGlyph):
    name = "long_left_arrow"
    unicode = "0x27F5"
    angle = 180


class LongLeftRightArrowGlyph(LeftRightArrowGlyph):
    name = "long_left_right_arrow"
    unicode = "0x27F7"
    length_ratio = 1


# Dingbats: heavier or triangle-headed variants of the right arrow


class HeavyWideHeadedRightArrowGlyph(RightArrowGlyph):
    name = "heavy_wide_headed_right_arrow"
    unicode = "0x2794"
    stroke_ratio = 1.5
    filled_head = True
    arrow_width = 0.45
    span = 0.5


class HeavyRoundTippedRightArrowGlyph(RightArrowGlyph):
    name = "heavy_round_tipped_right_arrow"
    unicode = "0x279C"
    stroke_ratio = 1.5


class TriangleHeadedRightArrowGlyph(RightArrowGlyph):
    name = "triangle_headed_right_arrow"
    unicode = "0x279D"
    filled_head = True
    arrow_width = 0.35
    span = 0.3


class HeavyTriangleHeadedRightArrowGlyph(TriangleHeadedRightArrowGlyph):
    name = "heavy_triangle_headed_right_arrow"
    unicode = "0x279E"
    stroke_ratio = 1.5
    span = 0.36
