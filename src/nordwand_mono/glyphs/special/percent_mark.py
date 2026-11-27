from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.glyphs import Glyph


class PercentMarkGlyph(Glyph):
    name = "percent_mark"
    unicode = "0x25"
    offset = 0
    width_ratio = 1.2
    offset_ratio_x = 0.45
    offset_ratio_y = 0.45
    zero_ratio = 0.4
    zero_width_ratio = 0.47
    zero_stroke_ratio = 0.82
    stroke_ratio = 1

    def draw(self, pen, dc):
        body = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        width = self.zero_width_ratio * body.width
        height = self.zero_ratio * body.height
        # Keep the widened rings inside the horizontal bounds of the slash.
        offset_x = max(self.offset_ratio_x * body.width, width) / 2
        offset_y = self.offset_ratio_y * body.height / 2
        ring_stroke = self.zero_stroke_ratio * dc.stroke_alt
        slash_stroke = self.stroke_ratio * dc.stroke_x
        draw_parallelogramm(pen, slash_stroke, body.x1, body.y1, body.x2, body.y2)

        centers = (
            (body.x1 + offset_x, body.y2 - offset_y),
            (body.x2 - offset_x, body.y1 + offset_y),
        )
        for cx, cy in centers:
            draw_loop(
                pen,
                ring_stroke,
                ring_stroke,
                cx - width / 2,
                cy - height / 2,
                cx + width / 2,
                cy + height / 2,
                body.hx * self.zero_width_ratio,
                body.hy * self.zero_ratio,
            )
