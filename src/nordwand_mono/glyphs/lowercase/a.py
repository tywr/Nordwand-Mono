import pathops
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.rect import draw_rect


class LowercaseAGlyph(Glyph):
    name = "lowercase_a"
    unicode = "0x61"
    offset = -12
    accent_x_offset = 16
    mid_height = 0.52
    width_ratio = 0.99

    taper = 0.65

    top_loop_ratio = 0.75
    cap_height = 0.74
    cap_offset = 0.045
    cap_hx_ratio = 1.05
    cap_hy_ratio = 1
    bowl_top_ratio = 1.05

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="x_height",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        self.draw_a(pen, dc, b, dc.stroke_x, dc.stroke_y)

    def draw_bowl(self, pen, dc, b, sx, sy, ymid, ytmid, taper):
        sa = dc.stroke_alt
        kx, ky = b.hx / (b.width / 2), b.hy / (b.height / 2)

        def corner(x1, y1, x2, y2):
            """Quarter from (x1, y1), its tangent vertical, to (x2, y2), its
            tangent horizontal."""
            pen.curveTo(
                (x1, y1 + ky * (y2 - y1)), (x2 + kx * (x1 - x2), y2), (x2, y2)
            )

        def side(x1, y1, x2, y2):
            """Quarter from (x1, y1), its tangent horizontal, to (x2, y2), its
            tangent vertical."""
            pen.curveTo(
                (x1 + kx * (x2 - x1), y1), (x2, y2 + ky * (y1 - y2)), (x2, y2)
            )

        # Outside: the tapered end pulls the bottom point left by half its
        # taper, so both bottom quarters keep the same handles there
        y_top = ymid + sa / 2
        y_ol = (b.y1 + y_top) / 2
        xo2 = b.x2 - sx + taper * sx
        x_om = b.xmid - (b.x2 - xo2) / 2
        pen.moveTo((b.x1, y_ol))
        corner(b.x1, y_ol, x_om, b.y1)
        side(x_om, b.y1, xo2, ytmid)
        pen.lineTo((xo2, y_top))
        x_ot = b.x1 + self.bowl_top_ratio * (x_om - b.x1)
        pen.lineTo((x_ot, y_top))
        side(x_ot, y_top, b.x1, y_ol)
        pen.closePath()

        # Inside
        x_im, y_im = b.xmid, b.y1 + sy
        xi1, xi2 = b.x1 + sx, b.x2 - sx
        y_it = ymid - sa / 2
        y_il = (y_im + y_it) / 2
        pen.moveTo((xi1, y_il))
        corner(xi1, y_il, x_im, y_it)
        pen.lineTo((xi2, y_it))
        pen.lineTo((xi2, ytmid))
        corner(xi2, ytmid, x_im, y_im)
        side(x_im, y_im, xi1, y_il)
        pen.closePath()

    def draw_a(self, pen, dc, b, sx, sy, stem=True, right_taper=None):
        """Bottom and top loops within `b`, without the stem; returns the
        bottom of the top loop."""
        ec = self.extra_cut(dc)
        ymid = b.y1 + self.mid_height * b.height
        ycut = b.y1 + self.cap_height * b.height - ec
        chx = self.cap_hx_ratio * b.hx
        chy = self.cap_hy_ratio * b.hy

        # Top loop variables
        yt1 = b.y2 - self.top_loop_ratio * b.height

        self.draw_bowl(
            pen,
            dc,
            b,
            sx,
            sy,
            ymid,
            b.y1 + self.top_loop_ratio * b.height / 2,
            right_taper if right_taper else self.taper * dc.taper,
        )

        xc1 = b.x1 + self.cap_offset * b.width
        top = pathops.Path()
        arc = pathops.Path()
        draw_arch(
            pathops.PathPen(arc),
            sx,
            sy,
            xc1,
            yt1,
            b.x2,
            b.y2,
            chx * (b.x2 - xc1) / b.width,
            chy * (b.y2 - yt1) / b.height,
            side="right",
            taper=right_taper if right_taper else 1,
            cut="bottom",
        )
        top = pathops.op(top, arc, pathops.PathOp.UNION)
        cut = pathops.Path()
        draw_rect(pathops.PathPen(cut), b.x1, b.ymid, b.xmid, ycut)
        pathops.op(top, cut, pathops.PathOp.DIFFERENCE).draw(pen)

        if stem:
            # Lower stem
            draw_rect(
                pen,
                b.x2 - sx,
                0,
                b.x2,
                (yt1 + b.y2) / 2,
            )
        else:
            draw_rect(
                pen,
                b.x2 - sx,
                (b.y1 + ymid + dc.stroke_alt / 2) / 2,
                b.x2 + sx * (right_taper - 1),
                (yt1 + b.y2) / 2,
            )

        return yt1
