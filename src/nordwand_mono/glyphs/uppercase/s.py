from nordwand_mono.glyphs.uppercase import UppercaseGlyph
from nordwand_mono.draw.corner import draw_corner


class UppercaseSGlyph(UppercaseGlyph):
    name = "uppercase_s"
    unicode = "0x53"
    offset = 4
    hx_ratio = 1
    hy_ratio = 1
    mid_height = 0.51
    opening1 = 0.27
    opening2 = 0.735
    thinning = 1
    left_offset = 0.04
    right_offset = 0.02
    curve_thinning = 0.008
    curve_ratio = 2.0
    curve_shift_ratio = 0.000
    width_ratio = 1.05
    ending_hx_ratio = 1
    thinning = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = self.get_strokes(dc)
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        ec = self.extra_cut(dc)
        yc1 = b.y1 + b.height * self.opening1 + ec
        yc2 = b.y1 + b.height * self.opening2 - ec
        ymid = b.y1 + self.mid_height * b.height
        x1 = b.x1 + self.left_offset * b.width
        x2 = b.x2 - self.right_offset * b.width
        hxt = (1 - self.left_offset - self.right_offset) * b.hx
        ym1 = (b.y2 + ymid - sy / 2) / 2
        ym2 = (b.y1 + ymid + sy / 2) / 2
        th = self.curve_thinning * b.height
        ro = self.curve_shift_ratio * max(0, sx - dc.default_stroke)
        r = self.curve_ratio + ro

        thx, thy, tihx, tihy = draw_corner(
            pen,
            sx,
            sy,
            x1,
            ym1,
            b.xmid,
            b.y2,
            hxt,
            hy * (1 - self.mid_height),
            orientation="top-right",
        )
        bhx, bhy, bihx, bihy = draw_corner(
            pen,
            sx,
            sy,
            b.x2,
            ym2,
            b.xmid,
            b.y1,
            hx,
            hy * self.mid_height,
            orientation="bottom-left",
        )

        # Mid Curve
        pen.moveTo((x1, ym1))
        pen.curveTo(
            (x1, ym1 - r * thy + th), (b.x2 - sx, ym2 + r * bihy + th), (b.x2 - sx, ym2)
        )
        pen.lineTo((b.x2, ym2))
        pen.curveTo(
            (b.x2, ym2 + r * bhy - th), (x1 + sx, ym1 - r * tihy - th), (x1 + sx, ym1)
        )
        pen.closePath()

        # Endings, from the openings to the middle of the top and bottom
        draw_corner(
            pen,
            self.get_thinned_stroke(dc),
            sy,
            x2,
            yc2,
            b.xmid,
            b.y2,
            hxt * self.ending_hx_ratio,
            2 * hy * (b.y2 - yc2) / b.height,
            orientation="top-left",
        )
        draw_corner(
            pen,
            self.get_thinned_stroke(dc),
            sy,
            b.x1,
            yc1,
            b.xmid,
            b.y1,
            hx * self.ending_hx_ratio,
            2 * hy * (yc1 - b.y1) / b.height,
            orientation="bottom-right",
        )
