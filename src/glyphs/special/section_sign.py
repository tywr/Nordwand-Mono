from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph
from glyphs.numbers.three import ThreeGlyph


class SectionSignGlyph(Glyph):
    name = "section_sign"
    unicode = "0xA7"
    offset = 0

    def draw(self, pen, dc):
        recording = RecordingPen()
        ThreeGlyph().draw(recording, dc)

        bounds_pen = BoundsPen(None)
        recording.replay(bounds_pen)
        x_min, y_min, x_max, y_max = bounds_pen.bounds
        glyph_length = y_max - y_min
        offset = glyph_length / 4 - dc.stroke_y / 4

        recording.replay(
            TransformPen(pen, Transform(1, 0, 0, 1, 0, -offset))
        )
        recording.replay(
            TransformPen(
                pen,
                Transform(
                    -1,
                    0,
                    0,
                    -1,
                    x_min + x_max,
                    y_min + y_max + offset,
                ),
            )
        )
