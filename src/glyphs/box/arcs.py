from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen

from draw.rect import draw_rect
from glyphs.box import BoxGlyph, box_glyph

K = 0.5523  # Bezier handle length of a quarter circle, relative to its radius


class ArcBoxGlyph(BoxGlyph):
    """Light rounded corner, drawn as ╭ then mirrored by `flip_x`/`flip_y`."""

    # Radius of the centre line, relative to half the cell width
    radius_ratio = 0.6
    flip_x = False
    flip_y = False

    def draw(self, pen, dc):
        (x1, y1, x2, y2), (cx, cy) = self.cell(dc)
        if self.flip_x:
            pen = TransformPen(pen, Transform(-1, 0, 0, 1, 2 * cx, 0))
        if self.flip_y:
            pen = TransformPen(pen, Transform(1, 0, 0, -1, 0, 2 * cy))

        s = self.stroke("light")
        r = self.radius_ratio * (cx - x1)
        ax, ay = cx + r, cy - r  # Centre of the arc
        ro, ri = r + s / 2, r - s / 2

        pen.moveTo((ax, ay + ro))
        pen.curveTo((ax - K * ro, ay + ro), (ax - ro, ay + K * ro), (ax - ro, ay))
        pen.lineTo((ax - ri, ay))
        pen.curveTo((ax - ri, ay + K * ri), (ax - K * ri, ay + ri), (ax, ay + ri))
        pen.closePath()
        # Overlap the arc by a unit, so no seam shows where they meet
        draw_rect(pen, ax - 1, cy - s / 2, x2 + self.bleed, cy + s / 2)
        draw_rect(pen, cx - s / 2, y1 - self.bleed, cx + s / 2, ay + 1)


GLYPHS = [
    box_glyph(ArcBoxGlyph, 0x256D),
    box_glyph(ArcBoxGlyph, 0x256E, flip_x=True),
    box_glyph(ArcBoxGlyph, 0x256F, flip_x=True, flip_y=True),
    box_glyph(ArcBoxGlyph, 0x2570, flip_y=True),
]
