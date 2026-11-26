import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.polygon import draw_polygon


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 1.0
    overlap = 0.536
    lower_section_height = 1.2

    def tail_end(self, dc):
        """Height the tail runs down to"""
        return dc.descent

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * s
        lsh = self.lower_section_height * dc.stroke_y
        fork_y = b.y1
        # The Latin y shows more of its tail. Other letters share this outline.
        if self.unicode == LowercaseYGlyph.unicode:
            fork_y += (b.y2 - b.y1) * 0.08

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm(
            gpen, s, b.xmid + ov, fork_y, b.x1, b.y2, direction="top-left"
        )
        _, delta = draw_parallelogramm(gpen, s, b.xmid - ov, fork_y, b.x2, b.y2)
        # The opening ends lsh above the fork-to-tail junction.
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + delta, b.y2), (b.x2 - delta, b.y2), (b.xmid, fork_y + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # Tail continuing the right branch below the fork: same edges'
        # slope, so the same stroke gives it the same horizontal width
        w2 = b.x2 - (b.xmid - ov)
        h2 = b.y2 - fork_y
        yt = self.tail_end(dc)
        dx_tail = -(w2 - delta) * (fork_y - yt) / h2
        draw_parallelogramm(
            pen,
            s,
            b.xmid - ov + delta,
            fork_y,
            b.xmid - ov + dx_tail,
            yt,
            direction="bottom-left",
        )
