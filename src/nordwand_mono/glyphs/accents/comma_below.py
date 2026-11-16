from nordwand_mono.glyphs.accents import Accent
from nordwand_mono.draw.polygon import draw_polygon


class CommaBelow(Accent):
    """Tapered comma hanging below the baseline (Romanian ș, ț)."""

    name = "commabelow"
    unicode = "0x326"
    gap = 0.1  # Space between the baseline and the mark, relative to x-height
    depth = 1.0  # Bottom of the mark, as a fraction of the descender
    foot_offset = 0.12  # Leftward lean of the foot, relative to the body width
    taper = 0.66
    stroke_ratio = 1.1

    def draw_at(self, pen, dc, x, y):
        top = y - self.gap * dc.x_height
        bottom = y - self.depth * abs(dc.descent)
        sx = self.stroke_ratio * dc.stroke_x
        fx = self.foot_offset * dc.width

        draw_polygon(
            pen,
            points=[
                (x - sx / 2, top),
                (x + sx / 2, top),
                (x + self.taper * sx / 2 - fx, bottom),
                (x - sx / 2 - fx, bottom),
            ],
        )

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=0)
