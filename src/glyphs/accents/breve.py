from config import FontConfig as fc
from glyphs.accents import Accent
from draw.loop import draw_loop


class Breve(Accent):
    name = "breve"
    unicode = "0x2D8"
    offset_y = 0
    width = 1
    stroke_ratio = 1
    # Handles, relative to those of a loop the size of the breve's box
    hx_ratio = 0.5
    hy_ratio = 0.83

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        w = self.width * dc.width
        x1, x2 = x - w / 2, x + w / 2
        # Only the bottom half of the loop is drawn, `h` high: center it on y
        y1, y2 = y - h / 2, y + 3 * h / 2
        # dc.hx and dc.hy are sized for a body as wide as dc.width and as
        # tall as the x-height: rescale them to the box, so that the curve
        # keeps its shape whatever the width and height of the breve
        hx = dc.hx * self.hx_ratio * w / dc.width
        hy = dc.hy * self.hy_ratio * (y2 - y1) / dc.x_height
        oy = self.offset_y * dc.x_height

        draw_loop(
            pen,
            self.stroke_ratio * dc.stroke_alt,
            self.stroke_ratio * dc.stroke_alt,
            x1,
            y1 + oy,
            x2,
            y2 + oy,
            hx,
            hy,
            cut="top",
        )


class CombiningBreve(Breve):
    name = "combining_breve"
    unicode = "0x306"
    number_characters = 0

    def draw(self, pen, dc):
        # Fallback placement when shaping does not apply the ccmp glyph.
        self.draw_at(pen, dc, x=-fc.window_width / 2, y=fc.accent_cap)
