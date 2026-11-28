from math import sqrt

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.polygon import draw_polygon


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    offset = 0
    width_ratio = 1.12
    stroke_ratio = 1.0
    lower_section_height = 1.2
    stroke_x_dampening = 0.8
    expand_factor = 1.1

    def tail_end(self, dc):
        """Height the tail runs down to"""
        return dc.descent

    def section(self, s, b):
        """Horizontal width d of both branches' ends, so their bottoms are
        the same [xmid - d/2, xmid + d/2]: a branch of stroke `s` from there
        up to its top corner spans w = (width + d) / 2 and has, as in
        parallelogramm_delta, s^2 (h^2 + (w - d)^2) = d^2 h^2, a quadratic
        in d whatever the body's width and height."""
        w, h = b.width, b.y2 - b.y1
        qa = h**2 - s**2 / 4
        qb = s**2 * w / 2
        qc = -(s**2) * (w**2 / 4 + h**2)
        return (-qb + sqrt(qb**2 - 4 * qa * qc)) / (2 * qa)

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio, expand_factor=self.expand_factor)
        s, _ = self.get_strokes(dc)
        delta = self.section(s, b)
        ov = delta / 2
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        # Both branches stand on the same bottom, one `delta` wide
        draw_parallelogramm(
            gpen,
            s,
            b.xmid + ov,
            b.y1,
            b.x1,
            b.y2,
            direction="top-left",
            overwrite_section=delta,
        )
        draw_parallelogramm(
            gpen, s, b.xmid - ov, b.y1, b.x2, b.y2, overwrite_section=delta
        )
        # As in the v, the branches meet lsh above the baseline
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + delta, b.y2), (b.x2 - delta, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # Tail continuing the right branch below the baseline: same edges'
        # slope, so the same stroke gives it the same horizontal width
        w2 = b.x2 - (b.xmid - ov)
        h2 = b.y2 - b.y1
        yt = self.tail_end(dc)
        dx_tail = -(w2 - delta) * (b.y1 - yt) / h2
        draw_parallelogramm(
            pen,
            s,
            b.xmid - ov + delta,
            b.y1,
            b.xmid - ov + dx_tail,
            yt,
            direction="bottom-left",
            overwrite_section=delta,
        )
