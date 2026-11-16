from nordwand_mono.glyphs import InfiniteLigatureGlyph


class HyphenMinusGlyph(InfiniteLigatureGlyph):
    name = "hyphen_minus"
    unicode = "0x2D"
    offset = 0
    side_offset = 0.2
    width_ratio = 1
    stroke_ratio = 0.92

    def horizontal_bar_heights(self, dc):
        return (dc.math,)

    def horizontal_bar_stroke(self, dc):
        return self.stroke_ratio * dc.stroke_x

    def horizontal_bar_bounds(self, dc):
        so = self.side_offset * dc.window_width
        return so, dc.window_width - so
