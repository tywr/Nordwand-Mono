from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from config import FontConfig as fc
from glyphs import Glyph
from draw.rect import draw_rect


class EuroSignGlyph(Glyph):
    name = "euro_sign"
    unicode = "0x20AC"
    offset = -10
    c_width_ratio = 0.94  # Narrower than the C, to fit the bars in the cell
    overhang = 0.2  # Bars reach past the left of the C, relative to its width
    bar_length = 0.8  # Bar length from its left end, relative to the C's width
    gap = 0.16  # Space between the bars, relative to the cap height

    def draw(self, pen, dc):
        from glyphs.uppercase.round.c import UppercaseCGlyph

        c = UppercaseCGlyph()
        c.width_ratio = self.c_width_ratio
        recording = RecordingPen()
        c.draw(recording, dc)
        bounds = BoundsPen(None)
        recording.replay(bounds)
        cx1, _, cx2, _ = bounds.bounds

        # Center the C and the bars together in the cell
        ov = self.overhang * (cx2 - cx1)
        dx = fc.window_width / 2 - (cx1 - ov + cx2) / 2
        recording.replay(TransformPen(pen, Transform(1, 0, 0, 1, dx, 0)))

        sy = dc.stroke_y * c.stroke_y_ratio
        x1 = cx1 + dx - ov
        x2 = x1 + self.bar_length * (cx2 - cx1)
        g = self.gap * dc.cap
        for y in (dc.cap / 2 - g / 2 - sy, dc.cap / 2 + g / 2):
            draw_rect(pen, x1, y, x2, y + sy)
