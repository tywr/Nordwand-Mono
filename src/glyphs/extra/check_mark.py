from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class CheckMarkGlyph(Glyph):
    name = "check_mark"
    unicode = "0x2713"
    offset = 0
    width_ratio = 1.1
    # Top of the short arm, relative to x-height
    short_arm_ratio = 0.5
    # Bottom right corner of the vertex, relative to the body width
    vertex_ratio = 0.45
    stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        stroke = self.stroke_ratio * dc.stroke_x
        xv = b.x1 + self.vertex_ratio * (b.x2 - b.x1)
        # Both arms end on the same bottom right corner, so the vertex has a
        # flat foot as wide as the short arm's section
        draw_parallelogramm(
            pen,
            stroke,
            b.x1,
            self.short_arm_ratio * b.y2,
            xv,
            b.y1,
            direction="bottom-right",
        )
        _, delta = draw_parallelogramm(pen, stroke, xv, b.y1, b.x2, b.y2, no_draw=True)
        draw_parallelogramm(pen, stroke, xv - delta, b.y1, b.x2, b.y2)


class HeavyCheckMarkGlyph(CheckMarkGlyph):
    name = "heavy_check_mark"
    unicode = "0x2714"
    stroke_ratio = 1.5
