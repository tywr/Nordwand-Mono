from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseOGlyph(RoundLowercaseGlyph):
    name = "lowercase_o"
    unicode = "0x6F"
    offset = 0
    width_ratio = 1

    def draw(
        self,
        pen,
        dc,
    ):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.get_strokes(dc)
        self.draw_o(pen, dc, b, sx, sy)

    def draw_o(self, pen, dc, b, sx, sy, right_taper=None):
        """The whole o within `b`. With `right_taper`, the right side is
        thinned to that ratio of `sx` from the outside, so it can share a
        stroke with a glyph on its right."""
        if right_taper:
            draw_arch(
                pen,
                sx,
                sy,
                b.x1,
                b.y1,
                b.x2,
                b.y2,
                b.hx,
                b.hy,
                taper=right_taper,
                side="right",
            )
        else:
            draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
