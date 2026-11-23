import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.polygon import draw_polygon


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    offset = 0
    width_ratio = 1.1
    stroke_ratio = 1
    inner_section_height = 0.85
    top_width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        ish = self.inner_section_height * dc.stroke_y
        w = self.top_width_ratio * b.width
        xt1, xt2 = b.xmid - w / 2, b.xmid + w / 2

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        _, delta = draw_parallelogramm(gpen, s, b.x1, b.y1, xt2, b.y2)
        draw_parallelogramm(gpen, s, b.x2, b.y1, xt1, b.y2, direction="top-left")
        # Where the centers of the diagonals cross, on b.xmid: at b.ymid with
        # the top as wide as the bottom, higher as the top narrows
        yc = b.y1 + b.height * (b.width - delta) / (b.width + w - 2 * delta)
        cut_glyph = ufoLib2.objects.Glyph()
        cpen = cut_glyph.getPen()
        draw_polygon(
            cpen,
            points=[(xt1 + delta, b.y2), (xt2 - delta, b.y2), (b.xmid, yc + ish)],
        )
        draw_polygon(
            cpen,
            points=[(b.x2 - delta, b.y1), (b.x1 + delta, b.y1), (b.xmid, yc - ish)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
