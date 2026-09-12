from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from config import FontConfig as fc
from glyphs.special.question_mark import QuestionMarkGlyph


class InvertedQuestionMarkGlyph(QuestionMarkGlyph):
    name = "inverted_question_mark"
    unicode = "0xBF"

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
