from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect


class DaggerGlyph(Glyph):
    name = "dagger"
    unicode = "0x2020"
    offset = 0
    width_ratio = 1
    bar_width = 0.85  # Relative to the body width
    bottom = 0.7  # Stem bottom below the baseline, relative to the descender
    # Crossbar centers, relative to the stem length from its bottom
    bars = (0.72,)

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        y1, y2 = self.bottom * dc.descent, dc.ascent
        draw_rect(pen, b.xmid - sx / 2, y1, b.xmid + sx / 2, y2)

        w = self.bar_width * b.width / 2
        for r in self.bars:
            y = y1 + r * (y2 - y1)
            draw_rect(pen, b.xmid - w, y - sy / 2, b.xmid + w, y + sy / 2)


class DoubleDaggerGlyph(DaggerGlyph):
    name = "double_dagger"
    unicode = "0x2021"
    bars = (0.25, 0.75)
