import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class Circumflex(Accent):
    name = "circumflex"
    unicode = "0x5E"
    height = 0.35
    width = 1
    stroke_ratio = 1
    overlap = 0.5
    upper_section_height = 1

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        w = self.width * dc.width
        x1, x2, xmid = x - w / 2, x + w / 2, x
        y1, y2 = y - h / 2, y + h / 2
        s = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * s
        ush = self.upper_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        _, delta = draw_parallelogramm(gpen, s, x1, y1, xmid + ov, y2)
        draw_parallelogramm(gpen, s, x2, y1, xmid - ov, y2, direction="top-left")
        # Upside-down v: the branches meet ush below the apex
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(x1 + delta, y1), (x2 - delta, y1), (xmid, y2 - ush)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)


class ModifierCircumflex(Circumflex):
    name = "modifier_circumflex"
    unicode = "0x2C6"
