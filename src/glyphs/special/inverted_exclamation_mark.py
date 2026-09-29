from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from config import FontConfig as fc
from glyphs.special.exclamation_mark import ExclamationMarkGlyph


class InvertedExclamationMarkGlyph(ExclamationMarkGlyph):
    name = "inverted_exclamation_mark"
    unicode = "0xA1"

    def draw(self, pen, dc):
        recording = RecordingPen()
        super().draw(recording, dc)

        bounds_pen = BoundsPen(None)
        recording.replay(bounds_pen)
        _, y_min, _, y_max = bounds_pen.bounds
        scale_y = (dc.x_height - dc.descent) / (y_max - y_min)

        transform = Transform(
            -1,
            0,
            0,
            -scale_y,
            fc.window_width,
            dc.descent + y_max * scale_y,
        )
        recording.replay(TransformPen(pen, transform))
