from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.polygon import draw_polygon


class ExclamationMarkGlyph(Glyph):
    name = "exclamation_mark"
    unicode = "0x21"
    offset = 0
    width_ratio = 1
    gap = 0.33
    gap_shift_ratio = 0.75
    height_overflow = 0.05
    stroke_x_ratio = 1.15
    taper = 0.8

    def draw(self, pen, dc):
        from nordwand_mono.glyphs.special.full_stop import FullStopGlyph

        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = self.get_strokes(dc)
        yo = self.gap_shift_ratio * max(0, sx - dc.default_stroke)
        ys = self.gap * b.height + yo

        draw_polygon(
            pen,
            points=[
                (b.xmid + sx / 2, b.y2),
                (b.xmid - sx / 2, b.y2),
                (b.xmid - self.taper * sx / 2, ys),
                (b.xmid + self.taper * sx / 2, ys),
            ],
        )

        fsp = FullStopGlyph()
        fsp.draw(pen, dc)
