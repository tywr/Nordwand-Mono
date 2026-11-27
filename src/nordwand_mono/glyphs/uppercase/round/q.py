import pathops

from nordwand_mono.glyphs.uppercase.round import RoundUppercaseGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class UppercaseQGlyph(RoundUppercaseGlyph):
    name = "uppercase_q"
    unicode = "0x51"
    offset = 0
    tail_width = 0.45
    tail_y_end = 1.0
    tail_x_end = 1.0
    tail_y_start = 0.5
    tail_x_start = 0.25
    tail_stroke_dampening = 0.6

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.get_strokes(dc)
        xs = b.x1 + self.tail_x_start * b.width
        ys = b.y1 + self.tail_y_start * b.height
        ye = self.tail_y_end * dc.descent
        xe = b.x1 + self.tail_x_end * b.width
        s = max(0, self.tail_stroke_dampening * (sx - dc.default_stroke)) + min(
            dc.default_stroke, sx
        )

        loop = draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )

        # Tail without its part inside the counter
        tail, counter = pathops.Path(), pathops.Path()
        draw_parallelogramm(pathops.PathPen(tail), s, xs, ys, xe, ye)
        loop["inner"].draw(pathops.PathPen(counter))
        pathops.op(tail, counter, pathops.PathOp.DIFFERENCE).draw(pen)
