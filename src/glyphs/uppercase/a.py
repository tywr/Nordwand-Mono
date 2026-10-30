from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseAGlyph(UppercaseGlyph):
    name = "uppercase_a"
    unicode = "0x41"
    offset = 0
    bar_height = 0.38
    overlap = 0.5
    stroke_x_ratio = 1.02
    width_ratio = 1.2
    branch_stroke_ratio = 1.0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sy = dc.stroke_y * self.stroke_y_ratio
        sx = self.diag_stroke_dampening(self.branch_stroke_ratio, dc.stroke_x, coef=0.2)
        ec = self.extra_cut(dc)

        ov = self.overlap * sx
        hb = self.bar_height * b.height - ec

        # Left branch
        draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x2,
            b.y1,
            b.xmid - ov,
            b.y2,
            direction="top-left",
            delta=sx,
        )
        # Right branch
        draw_parallelogramm(
            pen, sx, sy, b.x1, b.y1, b.xmid + ov, b.y2, delta=sx
        )

        # Crossbar: ends follow the branch centerlines, so it always
        # reaches into both strokes and never pokes out of them
        def lerp(x0, x1, y):
            return x0 + (x1 - x0) * (y - b.y1) / (b.y2 - b.y1)

        def left(y):
            return lerp(b.x1 + sx / 2, b.xmid + ov - sx / 2, y)

        def right(y):
            return lerp(b.x2 - sx / 2, b.xmid - ov + sx / 2, y)

        draw_polygon(
            pen,
            points=[
                (left(hb - sy), hb - sy),
                (right(hb - sy), hb - sy),
                (right(hb), hb),
                (left(hb), hb),
            ],
        )
