import dataclasses

from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from nordwand_mono.glyphs import Glyph


class OrdinalIndicatorGlyph(Glyph):
    """A lowercase letter scaled down and raised so its top meets the cap.

    The letter is drawn with heavier strokes before scaling, so the final
    strokes are `stroke_ratio` of the regular ones instead of shrinking with
    the letter. Subclasses set `unicode` and the `source` glyph class.
    """

    offset = 0
    scale = 0.55
    stroke_ratio = 0.7
    top_ratio = 1  # Top of the character, relative to the cap height

    def draw(self, pen, dc):
        draw_scaled(
            pen,
            dc,
            self.source,
            self.scale,
            self.stroke_ratio,
            dc.window_width / 2 + self.offset,
            self.top_ratio * dc.cap,
        )


def draw_scaled(pen, dc, source, scale, stroke_ratio, cx, top):
    """Draw `source` scaled by `scale`, centred on `cx` with its top at `top`."""
    k = stroke_ratio / scale
    heavy = dataclasses.replace(
        dc,
        stroke_x=dc.stroke_x * k,
        stroke_y=dc.stroke_y * k,
        stroke_alt=dc.stroke_alt * k,
    )
    rec = RecordingPen()
    source().draw(rec, heavy)

    bp = BoundsPen(None)
    rec.replay(bp)
    x_min, _, x_max, y_max = bp.bounds

    s = scale
    t = Transform(s, 0, 0, s, cx - s * (x_min + x_max) / 2, top - s * y_max)
    rec.replay(TransformPen(pen, t))
