import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.loop import draw_loop


class QuestionMarkGlyph(Glyph):
    name = "question_mark"
    unicode = "0x3F"
    offset = 0
    width_ratio = 1
    loop_ratio_left = 0.6
    loop_ratio_right = 0.5
    opening = 0.74
    hx_ratio = 1
    gap = 0.33
    gap_shift_ratio = 0.75
    curve_height = 0.4
    curve_thinning_shift_ratio = 0.15
    curve_thinning = 0.02
    curve_ratio = 1.5
    curve_shift_ratio = 0.005
    stroke_y_dampening = 0.7
    stroke_x_dampening = 0.9
    thinning = 0.8

    def draw(self, pen, dc):
        from nordwand_mono.glyphs.special.full_stop import FullStopGlyph

        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            overshoot_top=True,
        )
        sx, sy = self.get_strokes(dc)
        ec = self.extra_cut(dc)
        yc = b.y1 + self.opening * b.height + ec
        yl = (1 - self.loop_ratio_left) * b.height
        yr = (1 - self.loop_ratio_right) * b.height
        yo = self.gap_shift_ratio * max(0, sx - dc.default_stroke)
        ys = self.gap * b.height + yo
        hx = self.hx_ratio * b.hx
        tho = self.curve_thinning_shift_ratio * (sx - dc.default_stroke)
        th = self.curve_thinning * b.height + tho
        ro = self.curve_shift_ratio * max(0, sx - dc.default_stroke)
        r = self.curve_ratio + ro

        # Left part of the top-loop
        glyph = ufoLib2.objects.Glyph()
        draw_loop(
            glyph.getPen(),
            self.get_thinned_stroke(dc),
            sy,
            b.x1,
            yl,
            b.x2,
            b.y2,
            hx,
            b.hy * self.loop_ratio_left,
            quarter="top-left",
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            b.y1,
            b.x2 + 10,
            yc,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # Right part of the top loop
        loop = draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            yr,
            b.x2,
            b.y2,
            hx,
            b.hy * self.loop_ratio_right,
            quarter="top-right",
        )

        # Mid Curve
        ym = (b.y2 + yr) / 2
        lhy, lihy = loop["outer"].hy, loop["inner"].hy
        pen.moveTo((b.x2 - sx, ym))
        pen.curveTo(
            (b.x2 - sx, ym - r * lihy - th),
            (b.xmid - sx / 2, ys + r * lhy - th),
            (b.xmid - sx / 2, ys),
        )
        pen.lineTo((b.xmid + sx / 2, ys))
        pen.curveTo(
            (b.xmid + sx / 2, ys + r * lihy + th),
            (b.x2, ym - r * lhy + th),
            (b.x2, ym),
        )
        pen.closePath()

        fsp = FullStopGlyph()
        fsp.draw(pen, dc)
