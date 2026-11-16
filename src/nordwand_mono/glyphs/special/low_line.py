from nordwand_mono.glyphs import InfiniteLigatureGlyph


class LowLineGlyph(InfiniteLigatureGlyph):
    name = "low_line"
    unicode = "0x5F"
    offset = 0
    side_offset = 0.08
    stroke_ratio = 0.92
    width_ratio = 1

    def horizontal_bar_heights(self, dc):
        return (-self.horizontal_bar_stroke(dc) / 2,)

    def horizontal_bar_stroke(self, dc):
        return self.stroke_ratio * dc.stroke_x

    def horizontal_bar_bounds(self, dc):
        so = self.side_offset * dc.window_width
        return so, dc.window_width - so
