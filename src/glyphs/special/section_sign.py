from glyphs import Glyph
from draw.arch import draw_arch
from draw.loop import draw_loop


class SectionSignGlyph(Glyph):
    name = "section_sign"
    unicode = "0xA7"
    offset = 0
    width_ratio = 0.95
    height_ratio = 1.4  # Total height, relative to the cap height
    loop_ratio = 0.42  # Middle loop height, relative to the total height
    taper = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        height = self.height_ratio * dc.cap
        y_top = dc.cap / 2 + height / 2
        y_bottom = dc.cap / 2 - height / 2
        loop_h = self.loop_ratio * height
        loop_y1 = dc.cap / 2 - loop_h / 2
        loop_y2 = dc.cap / 2 + loop_h / 2

        def hy(h):
            return dc.hy * (h - sy) / dc.x_height

        draw_loop(pen, sx, sy, b.x1, loop_y1, b.x2, loop_y2, b.hx, hy(loop_h))

        # Each bowl's inner stroke overlaps the loop and tapers into it
        taper = max(self.taper * dc.taper, 0.65)
        bowl_h = y_top - (loop_y2 - sy)
        top = dict(y1=loop_y2 - sy, y2=y_top, side="bottom")
        bottom = dict(y1=y_bottom, y2=loop_y1 + sy, side="top")
        for bowl, cuts in ((top, ("bottom", "right")), (bottom, ("top", "left"))):
            for cut in cuts:
                draw_arch(
                    pen,
                    sx,
                    sy,
                    b.x1,
                    bowl["y1"],
                    b.x2,
                    bowl["y2"],
                    b.hx,
                    hy(bowl_h),
                    side=bowl["side"],
                    cut=cut,
                    taper=taper,
                )
