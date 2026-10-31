from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm, parallelogramm_delta
from draw.rect import draw_rect


class UppercaseYGlyph(UppercaseGlyph):
    name = "uppercase_y"
    unicode = "0x59"
    offset = 0
    width_ratio = 1.22
    junction_ratio = 0.4
    branch_stroke_ratio = 0.89  # Perpendicular thickness of the branches

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        sx = dc.stroke_x * self.stroke_x_ratio

        yj = b.x1 + self.junction_ratio * b.height

        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, yj)

        # Both feet centered on the stem, which they cover within a unit
        s = self.branch_stroke_ratio * sx
        d = parallelogramm_delta(s, b.xmid - sx / 2, yj, b.x2, b.y2)
        draw_parallelogramm(pen, s, b.xmid - d / 2, yj, b.x2, b.y2)
        draw_parallelogramm(
            pen, s, b.xmid + d / 2, yj, b.x1, b.y2, direction="top-left"
        )
