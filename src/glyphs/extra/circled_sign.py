import dataclasses

from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph
from glyphs.uppercase.round.c import UppercaseCGlyph
from glyphs.uppercase.bowl.r import UppercaseRGlyph
from draw.loop import draw_loop


class CircledSignGlyph(Glyph):
    """A capital scaled down inside a ring from the baseline to the cap height.

    As in the ordinal indicators, the letter is drawn with heavier strokes
    before scaling, so its final strokes are `stroke_ratio` of the regular ones.
    Subclasses set `unicode` and the `source` glyph class.
    """

    offset = 0
    margin = 0.06  # Ring distance from the cell edges, relative to the cell width
    ring_ratio = 0.6  # Ring stroke, relative to the regular strokes
    scale = 0.42
    stroke_ratio = 0.6
    y_start = 0.2

    def draw(self, pen, dc):
        w = dc.window_width
        d = (1 - 2 * self.margin) * w
        sx, sy = self.ring_ratio * dc.stroke_x, self.ring_ratio * dc.stroke_y
        ys = self.y_start * dc.x_height
        cx, cy = w / 2 + self.offset, (ys + dc.cap) / 2
        draw_loop(
            pen,
            sx,
            sy,
            cx - d / 2,
            ys,
            cx + d / 2,
            dc.cap,
            dc.cap_hx * (d - sx) / dc.width,
            dc.cap_hy * (dc.cap - sy) / dc.x_height,
        )

        k = self.stroke_ratio / self.scale
        heavy = dataclasses.replace(
            dc,
            stroke_x=dc.stroke_x * k,
            stroke_y=dc.stroke_y * k,
            stroke_alt=dc.stroke_alt * k,
        )
        rec = RecordingPen()
        self.source().draw(rec, heavy)
        bp = BoundsPen(None)
        rec.replay(bp)
        x1, y1, x2, y2 = bp.bounds

        s = self.scale
        t = Transform(s, 0, 0, s, cx - s * (x1 + x2) / 2, cy - s * (y1 + y2) / 2)
        rec.replay(TransformPen(pen, t))


class CopyrightSignGlyph(CircledSignGlyph):
    name = "copyright_sign"
    unicode = "0xA9"
    source = UppercaseCGlyph


class RegisteredSignGlyph(CircledSignGlyph):
    name = "registered_sign"
    unicode = "0xAE"
    source = UppercaseRGlyph
