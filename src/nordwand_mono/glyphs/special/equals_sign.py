from nordwand_mono.glyphs import InfiniteLigatureGlyph


class EqualsSignGlyph(InfiniteLigatureGlyph):
    name = "equals_sign"
    unicode = "0x3D"
    offset = 0
    side_offset = 0.08
    width_ratio = 1
    gap = 0.4
    stroke_ratio = 0.92

    def horizontal_bar_heights(self, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        g = self.gap * b.height
        return dc.math + g / 2, dc.math - g / 2

    def horizontal_bar_stroke(self, dc):
        return dc.stroke_x * self.stroke_ratio

    def horizontal_bar_bounds(self, dc):
        so = self.side_offset * dc.window_width
        return so, dc.window_width - so
