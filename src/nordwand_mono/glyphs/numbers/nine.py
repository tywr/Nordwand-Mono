from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen
from nordwand_mono.glyphs.numbers.six import SixGlyph


class NineGlyph(SixGlyph):
    """The 6 turned upside down: rotated by 180 degrees around the middle of
    the cap height, so its bottom overshoot becomes the top one"""

    name = "nine"
    unicode = "0x39"
    offset = -4

    def draw(self, pen, dc):
        # The rotation mirrors the offset around the middle of the cell, so
        # draw the 6 on the other side
        offset = self.offset
        self.offset = -offset
        try:
            rotate = Transform(-1, 0, 0, -1, dc.window_width, dc.cap)
            super().draw(TransformPen(pen, rotate), dc)
        finally:
            self.offset = offset
