from glyphs.uppercase.bowl.r import UppercaseRGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class UppercaseR2Glyph(UppercaseRGlyph):
    name = "uppercase_r_2"
    font_feature = {"cv05": 1}

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        w = self.loop_width * b.width
        ymid = b.y1 + (1 - self.loop_ratio) * b.height
        xmid = b.x1 + w / 2
        # yl = b.y1 - (ymid + sy - b.y1)
        yl = ymid + sy - (self.loop_ratio * b.height)

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Upper loop (narrower, displaced left)
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x1 + w,
            b.y2,
            b.hx * self.loop_width,
            b.hy * self.loop_ratio,
            cut="left",
            side="bottom",
            taper=0.75,
        )

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, xmid, b.y2)
        draw_rect(pen, b.x1, ymid, xmid, ymid + sy)
        draw_rect(pen, b.x1, ymid, (b.x1 + b.x2) / 2, ymid + 0.25 * sy)

        # Lower loop
        # draw_arch(
        #     pen,
        #     sx,
        #     sy,
        #     b.x1,
        #     yl,
        #     b.x1 + w,
        #     ymid + sy,
        #     b.hx,
        #     b.hy * (1 - self.loop_ratio) * 2,
        #     quarter="top-right",
        #     side="top",
        #     taper=0.75,
        # )
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            yl,
            b.x2,
            ymid + sy,
            b.hx,
            b.hy * self.loop_ratio,
            quarter="top-right",
            side="top",
            taper=0.75,
        )
        draw_rect(
            pen,
            b.x2 - sx,
            b.y1,
            b.x2,
            (ymid + sy + yl) / 2,
        )
