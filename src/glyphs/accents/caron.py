import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class Caron(Accent):
    name = "caron"
    unicode = "0x2C7"
    height = 0.35
    width = 1.1
    stroke_ratio = 1
    overlap = 0.5
    lower_section_height = 1

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        w = self.width * dc.width
        x1, x2, xmid = x - w / 2, x + w / 2, x
        y1, y2 = y - h / 2, y + h / 2
        s = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * s
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        _, delta = draw_parallelogramm(gpen, s, xmid - ov, y1, x2, y2)
        draw_parallelogramm(gpen, s, xmid + ov, y1, x1, y2, direction="top-left")
        # As in the v, the branches meet lsh above the foot
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(x1 + delta, y2), (x2 - delta, y2), (xmid, y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
