import dataclasses

from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph
from glyphs.uppercase.stem_diagonal.m import UppercaseMGlyph
from glyphs.uppercase.t import UppercaseTGlyph


class TradeMarkSignGlyph(Glyph):
    """Scaled-down T and M side by side, with their tops at the cap height.

    As in the ordinal indicators, the letters are drawn with heavier strokes
    before scaling, so the final strokes are `stroke_ratio` of the regular ones.
    """

    name = "trade_mark_sign"
    unicode = "0x2122"
    offset = 0
    scale = 0.46
    stroke_ratio = 0.7
    gap = 0.03  # Between the letters, relative to the cell width

    def draw(self, pen, dc):
        k = self.stroke_ratio / self.scale
        heavy = dataclasses.replace(
            dc,
            stroke_x=dc.stroke_x * k,
            stroke_y=dc.stroke_y * k,
            stroke_alt=dc.stroke_alt * k,
        )
        s = self.scale
        letters = []
        for source in (UppercaseTGlyph, UppercaseMGlyph):
            rec = RecordingPen()
            source().draw(rec, heavy)
            bp = BoundsPen(None)
            rec.replay(bp)
            letters.append((rec, bp.bounds))

        gap = self.gap * dc.window_width
        total = sum(s * (x2 - x1) for _, (x1, _, x2, _) in letters) + gap
        x = (dc.window_width - total) / 2 + self.offset
        for rec, (x1, _, x2, y2) in letters:
            t = Transform(s, 0, 0, s, x - s * x1, dc.cap - s * y2)
            rec.replay(TransformPen(pen, t))
            x += s * (x2 - x1) + gap
