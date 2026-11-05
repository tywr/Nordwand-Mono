from fontTools.pens.recordingPen import RecordingPen

from glyphs.accents import Accent
from draw.loop import draw_loop


class HookAbove(Accent):
    """Small hook above (Vietnamese ả, ể, ở): a flat top turning down on the
    right, its drop leaning back to the left."""

    name = "hookabove"
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

        # The mark spans [x0, x0 + w] x [y0 - h, y0]; center it on (x, y)
        x0, y0 = x - w / 2, y + h / 2

        # Top-right quarter of a loop: right along the top, then down
        b = dc.body_bounds(offset=0)
        rec = RecordingPen()
        draw_loop(
            rec,
            sx,
            sy,
            x0 - w,
            y0 - 2 * h,
            x0 + w,
            y0,
            b.hx * 2 * w / b.width,
            b.hy * 2 * h / b.height,
            quarter="top-right",
        )

        # Shear left what hangs below the horizontal stroke, which stays put
        y_stroke = y0 - sy

        def lean(px, py):
            return px - self.shear * max(0, y_stroke - py), py

        for op, args in rec.value:
            getattr(pen, op)(*(lean(*p) for p in args))
