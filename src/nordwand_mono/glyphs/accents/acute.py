from nordwand_mono.config import FontConfig as fc
from nordwand_mono.glyphs.accents import Accent
from nordwand_mono.draw.parallelogramm import parallelogramm_delta
from nordwand_mono.draw.polygon import draw_polygon


def draw_slant(pen, s, x, y, w, h, taper, side=1):
    """Slanted stroke of perpendicular thickness `s` in its middle, its base
    centered on x and its top `w` to the right (`side` 1) or to the left
    (`side` -1), `h` high and centered on y. Its ends are horizontal, the base
    `taper` times as wide as the top, around the same center line as the
    parallelogramm of stroke `s`, so the middle keeps its width."""
    d = parallelogramm_delta(s, 0, 0, w, h)
    top = 2 * d / (1 + taper)
    bottom = taper * top
    xt = x + side * (w - d)
    yb, yt = y - h / 2, y + h / 2
    draw_polygon(
        pen,
        points=[
            (x - bottom / 2, yb),
            (x + bottom / 2, yb),
            (xt + top / 2, yt),
            (xt - top / 2, yt),
        ],
    )


class Acute(Accent):
    name = "acute"
    unicode = "0xB4"
    height = 0.32
    width = 0.55
    stroke_ratio = 1.0
    taper = 0.7  # Width of the base, relative to the top

    def scaled(self, dc, k):
        """Same slant, its height and its slanted part scaled by `k`"""
        w, h = self.width * dc.width, self.height * dc.x_height
        d = parallelogramm_delta(self.stroke_ratio * dc.stroke_x, 0, 0, w, h)
        self.width = (d + k * (w - d)) / dc.width
        self.height *= k
        return self

    def draw_at(self, pen, dc, x, y, stroke_ratio=None):
        h = self.height * dc.x_height
        s = self.stroke_ratio * dc.stroke_x
        xo = 1.15 * (s - dc.default_stroke)
        w = self.width * dc.width + xo
        draw_slant(pen, s, x, y, w, h, self.taper)


class Tonos(Acute):
    name = "tonos"
    unicode = "0x0384"


class CombiningAcute(Acute):
    name = "combining_acute"
    unicode = "0x0301"
    number_characters = 0

    def draw(self, pen, dc):
        # Fallback placement when shaping does not apply the ccmp glyph.
        self.draw_at(pen, dc, x=-fc.window_width / 2, y=fc.accent_cap)
