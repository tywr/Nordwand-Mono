from math import hypot

from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen

from config import FontConfig as fc
from draw.circle import draw_circle
from draw.square_corner import draw_square_corner
from draw.polygon import draw_polygon
from draw.rect import draw_rect
from glyphs import Glyph
from glyphs.extra.ordinal_indicator import draw_scaled
from glyphs.uppercase.round.c import UppercaseCGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.uppercase.stem_diagonal.n import UppercaseNGlyph

K = 0.5523  # Bezier handle length of a quarter ellipse, relative to its radius


def draw_half_ellipse(pen, cx, cy, rx, ry, tx=None, ty=None):
    """Right half of the ellipse centred on (cx, cy), solid or as an outline.

    Without `tx`/`ty` the half ellipse is filled; otherwise it is an outline
    of horizontal thickness `tx` at its tip and vertical thickness `ty` at
    its ends.
    """
    pen.moveTo((cx, cy - ry))
    pen.curveTo((cx + K * rx, cy - ry), (cx + rx, cy - K * ry), (cx + rx, cy))
    pen.curveTo((cx + rx, cy + K * ry), (cx + K * rx, cy + ry), (cx, cy + ry))
    if tx is not None:
        ix, iy = rx - tx, ry - ty
        pen.lineTo((cx, cy + iy))
        pen.curveTo((cx + K * ix, cy + iy), (cx + ix, cy + K * iy), (cx + ix, cy))
        pen.curveTo((cx + ix, cy - K * iy), (cx + K * ix, cy - iy), (cx, cy - iy))
    pen.closePath()


class PowerlineGlyph(Glyph):
    """Powerline symbol spanning the full line height.

    Shapes are drawn pointing right; `mirror` flips them to point left.
    """

    offset = 0
    italic_skew = False
    mirror = False
    stroke_ratio = 0.6  # Weight of outline shapes, relative to the stroke
    # Units the flat side extends into the neighbouring cell, so no seam shows
    # against the adjoining segment at any size
    bleed = 0

    def draw(self, pen, dc):
        w = dc.window_width
        if self.mirror:
            pen = TransformPen(pen, Transform(-1, 0, 0, 1, w, 0))
        bottom, top = fc.window_descent, fc.window_ascent
        if self.bleed:
            draw_rect(pen, -self.bleed, bottom, 0, top)
        self.draw_shape(pen, dc, w, bottom, top)

    def line_width(self, dc, dx, dy):
        """Horizontal width of a line of slope dy/dx with the outline weight."""
        return self.stroke_ratio * dc.stroke_x * hypot(dx, dy) / abs(dy)


# Arrows


class RightHardDividerGlyph(PowerlineGlyph):
    name = "powerline_right_hard_divider"
    unicode = "0xE0B0"
    bleed = 40

    def draw_shape(self, pen, dc, w, bottom, top):
        draw_polygon(pen, [(0, bottom), (w, (bottom + top) / 2), (0, top)])


class LeftHardDividerGlyph(RightHardDividerGlyph):
    name = "powerline_left_hard_divider"
    unicode = "0xE0B2"
    mirror = True


class RightSoftDividerGlyph(PowerlineGlyph):
    name = "powerline_right_soft_divider"
    unicode = "0xE0B1"

    def draw_shape(self, pen, dc, w, bottom, top):
        mid = (bottom + top) / 2
        t = self.line_width(dc, w, top - mid)
        draw_polygon(
            pen,
            [
                (0, bottom),
                (t, bottom),
                (w, mid),
                (t, top),
                (0, top),
                (w - t, mid),
            ],
        )


class LeftSoftDividerGlyph(RightSoftDividerGlyph):
    name = "powerline_left_soft_divider"
    unicode = "0xE0B3"
    mirror = True


# Rounded segment ends


class RightHalfCircleGlyph(PowerlineGlyph):
    name = "powerline_right_half_circle"
    unicode = "0xE0B4"
    bleed = 40

    def draw_shape(self, pen, dc, w, bottom, top):
        draw_half_ellipse(pen, 0, (bottom + top) / 2, w, (top - bottom) / 2)


class LeftHalfCircleGlyph(RightHalfCircleGlyph):
    name = "powerline_left_half_circle"
    unicode = "0xE0B6"
    mirror = True


class RightHalfCircleThinGlyph(PowerlineGlyph):
    name = "powerline_right_half_circle_thin"
    unicode = "0xE0B5"

    def draw_shape(self, pen, dc, w, bottom, top):
        draw_half_ellipse(
            pen,
            0,
            (bottom + top) / 2,
            w,
            (top - bottom) / 2,
            tx=self.stroke_ratio * dc.stroke_x,
            ty=self.stroke_ratio * dc.stroke_y,
        )


class LeftHalfCircleThinGlyph(RightHalfCircleThinGlyph):
    name = "powerline_left_half_circle_thin"
    unicode = "0xE0B7"
    mirror = True


# Corner triangles and diagonals


class LowerLeftTriangleGlyph(PowerlineGlyph):
    name = "powerline_lower_left_triangle"
    unicode = "0xE0B8"
    bleed = 40

    def draw_shape(self, pen, dc, w, bottom, top):
        draw_polygon(pen, [(0, bottom), (w, bottom), (0, top)])


class LowerRightTriangleGlyph(LowerLeftTriangleGlyph):
    name = "powerline_lower_right_triangle"
    unicode = "0xE0BA"
    mirror = True


class UpperLeftTriangleGlyph(PowerlineGlyph):
    name = "powerline_upper_left_triangle"
    unicode = "0xE0BC"
    bleed = 40

    def draw_shape(self, pen, dc, w, bottom, top):
        draw_polygon(pen, [(0, bottom), (w, top), (0, top)])


class UpperRightTriangleGlyph(UpperLeftTriangleGlyph):
    name = "powerline_upper_right_triangle"
    unicode = "0xE0BE"
    mirror = True


class BackslashSeparatorGlyph(PowerlineGlyph):
    name = "powerline_backslash_separator"
    unicode = "0xE0B9"

    def draw_shape(self, pen, dc, w, bottom, top):
        t = self.line_width(dc, w, top - bottom)
        draw_polygon(pen, [(0, top), (t, top), (w, bottom), (w - t, bottom)])


class BackslashSeparatorRedundantGlyph(BackslashSeparatorGlyph):
    name = "powerline_backslash_separator_redundant"
    unicode = "0xE0BF"


class ForwardSlashSeparatorGlyph(BackslashSeparatorGlyph):
    name = "powerline_forwardslash_separator"
    unicode = "0xE0BB"
    mirror = True


class ForwardSlashSeparatorRedundantGlyph(ForwardSlashSeparatorGlyph):
    name = "powerline_forwardslash_separator_redundant"
    unicode = "0xE0BD"


# Status line symbols, drawn within the cap height like regular glyphs


class BranchGlyph(PowerlineGlyph):
    name = "powerline_branch"
    unicode = "0xE0A0"
    italic_skew = True
    stroke_ratio = 1
    width_ratio = 1
    fork = 0.22  # Height where the branch leaves the stem, relative to the cap
    gap = 0.6  # Cut in the stem above the branch, relative to the stroke
    arrow_width = 0.45  # Relative to the body width
    arrow_height = 0.3  # Relative to the cap

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, height="cap", width_ratio=self.width_ratio)
        sx = self.stroke_ratio * dc.stroke_x
        sy = self.stroke_ratio * dc.stroke_y
        y_join = self.fork * dc.cap + sy
        draw_rect(pen, b.x1, 0, b.x1 + sx, y_join)
        draw_rect(pen, b.x1, y_join + self.gap * dc.stroke_y, b.x1 + sx, dc.cap)

        aw = self.arrow_width * b.width
        ah = self.arrow_height * dc.cap
        xc = b.x2 - aw / 2
        y_arrow = dc.cap - ah
        x_end = b.x1 + sx / 2
        g = 0.6 * (xc - b.x1 - sx * 1.5)
        draw_square_corner(
            pen,
            sx,
            sy,
            xc + sx / 2,
            y_arrow + 1,
            x_end,
            self.fork * dc.cap,
            gx=g,
            gy=g,
            orientation="bottom-left",
        )
        draw_polygon(
            pen, [(xc - aw / 2, y_arrow), (xc + aw / 2, y_arrow), (xc, dc.cap)]
        )


class PadlockGlyph(PowerlineGlyph):
    name = "powerline_readonly"
    unicode = "0xE0A2"
    italic_skew = True
    stroke_ratio = 1
    width_ratio = 0.85
    body_ratio = 0.55  # Height of the body, relative to the cap
    shackle_ratio = 0.75  # Width of the shackle, relative to the body
    keyhole_ratio = 0.07  # Radius of the keyhole, relative to the cap

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, height="cap", width_ratio=self.width_ratio)
        sx = self.stroke_ratio * dc.stroke_x
        sy = self.stroke_ratio * dc.stroke_y
        y_body = self.body_ratio * dc.cap
        draw_rect(pen, b.x1, 0, b.x2, y_body)
        draw_circle(
            pen, b.xmid, y_body / 2, self.keyhole_ratio * dc.cap, clockwise=True
        )

        r = self.shackle_ratio * b.width / 2
        y_arc = dc.cap - r
        draw_rect(pen, b.xmid - r, y_body, b.xmid - r + sx, y_arc)
        draw_rect(pen, b.xmid + r - sx, y_body, b.xmid + r, y_arc)
        shackle = TransformPen(pen, Transform(0, 1, -1, 0, b.xmid, y_arc))
        draw_half_ellipse(shackle, 0, 0, r, r, tx=sy, ty=sx)


class LineNumberGlyph(PowerlineGlyph):
    """Two capitals scaled down, one at the top left and one at the bottom right."""

    name = "powerline_line_number"
    unicode = "0xE0A1"
    italic_skew = True
    letters = (UppercaseLGlyph, UppercaseNGlyph)
    scale = 0.42
    stroke_ratio = 0.6
    spread = 0.22  # Horizontal shift of each letter from the centre, relative to the width

    def draw(self, pen, dc):
        cx = dc.window_width / 2
        dx = self.spread * dc.window_width
        top, bottom = self.letters
        draw_scaled(pen, dc, top, self.scale, self.stroke_ratio, cx - dx, dc.cap)
        draw_scaled(
            pen,
            dc,
            bottom,
            self.scale,
            self.stroke_ratio,
            cx + dx,
            self.scale * dc.cap,
        )


class ColumnNumberGlyph(LineNumberGlyph):
    name = "powerline_column_number"
    unicode = "0xE0A3"
    letters = (UppercaseCGlyph, UppercaseNGlyph)
