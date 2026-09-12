from glyphs import Glyph
from draw.polygon import draw_polygon


class RightSingleQuotationMarkGlyph(Glyph):
    name = "right_single_quotation_mark"
    unicode = "0x2019"
    offset = 0
    width_ratio = 1
    height_ratio = 0.55
    taper = 1.2
    delta = 0.1
    alpha = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = self.height_ratio * b.height
        s, st = dc.stroke_x, dc.stroke_x * self.taper
        d = self.delta * b.width

        p1x, p1y = b.xmid + s / 2 - d, dc.ascent - h
        p2x, p2y = b.xmid - s / 2 - d, dc.ascent - h
        p3x, p3y = b.xmid - st / 2, dc.ascent
        p4x, p4y = b.xmid + st / 2, dc.ascent

        ax = 0.25 * self.alpha * h
        ay = 0.25 * h

        pen.moveTo((p2x, p2y))
        pen.curveTo(
            (p2x + ax, p2y + ay),
            (p3x + ax, p3y - ay),
            (p3x, p3y),
        )
        pen.lineTo((p4x, p4y))
        pen.curveTo((p4x + ax, p4y - ay), (p1x + ax, p1y + ay), (p1x, p1y))
        pen.closePath()
