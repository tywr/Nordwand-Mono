from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect


class BulletGlyph(Glyph):
    name = "bullet"
    unicode = "0x2022"
    offset = 0
    width_ratio = 1
    # Side length: mostly fixed, plus a share that grows with the weight
    size_ratio = 0.25  # Relative to the x-height
    stroke_ratio = 1.0  # Relative to stroke_x

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        s = self.size_ratio * dc.x_height + self.stroke_ratio * dc.stroke_x
        y = dc.math
        draw_rect(pen, b.xmid - s / 2, y - s / 2, b.xmid + s / 2, y + s / 2)
