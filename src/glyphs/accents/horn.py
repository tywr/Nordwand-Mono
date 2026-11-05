import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from fontTools.pens.recordingPen import RecordingPen

from glyphs.accents import Accent
from draw.loop import draw_loop


class Horn(Accent):
    """Spur rising off the right shoulder of o and u (Vietnamese ơ, ư).

    Unlike most accents, `draw_at` anchors the mark by the left end of its
    bottom edge, which callers place inside the base outline so the two
    merge.
    """

    name = "horn"
    unicode = None
    generated_only = True  # Only used inside composed glyphs
    width = 0.66
    height = 0.4
    stroke_ratio = 0.9
    shear = 0.75

    def draw_at(self, pen, dc, x, y):
        w = self.width * dc.width
        h = self.height * dc.x_height
        sx = self.stroke_ratio * dc.stroke_x
        sy = self.stroke_ratio * dc.stroke_y

        # Bottom-right quarter of a loop: right from the anchor, then up
        b = dc.body_bounds(offset=0)
        rec = RecordingPen()
        draw_loop(
            rec,
            sx,
            sy,
            x - w,
            y - 2 * h,
            x + w,
            y,
            b.hx * 2 * w / b.width,
            b.hy * 2 * h / b.height,
            quarter="top-right",
        )

        y0 = y - sy

        def lean(px, py):
            return px - self.shear * max(0, y0 - py), py

        for op, args in rec.value:
            getattr(pen, op)(*(lean(*p) for p in args))

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=b.ymid)
