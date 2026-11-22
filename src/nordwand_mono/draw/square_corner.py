import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from nordwand_mono.config import FontConfig
from nordwand_mono.draw.rect import draw_rect


def draw_square_corner(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    gx=150,
    gy=150,
    orientation="bottom-right",
):
    """Draw a solid quarter-curve corner using superellipse handles.

    (x1, y1) is the outer start of the curve, (x2, y2) is the outer end.
    The stroke always goes inward (away from the corner).

    The corner point is at (x1, y2) in every orientation, which names the
    side of the corner the arm and the stem leave from:
        bottom-right: the stem comes down to the corner, the arm goes right
        top-right:    the stem goes up to the corner, the arm goes right
        top-left:     the stem goes up to the corner, the arm goes left
        bottom-left:  the stem comes down to the corner, the arm goes left

    Curves longer than the corner are cut at its end, x2, and at its start,
    y1, so the corner never reaches past its box.
    """
    sx, sy = stroke_x, stroke_y
    # +1 when the bar leaves the stem to the right / the stem rises from the bar
    dx = 1 if orientation.endswith("right") else -1
    dy = 1 if orientation.startswith("bottom") else -1

    # The outer curve keeps the tension of the regular weight. The inner radius
    # absorbs the stroke change, so the corner stays as heavy as the stems:
    # the diagonal is 0.81 * stroke at every weight.
    sx0, sy0 = FontConfig.stroke_x, FontConfig.stroke_y
    hx, hy = sx0 / 2, sy0 / 2
    ix = max(gx - 1.5 * (sx - sx0), 0)
    iy = max(gy - 1.5 * (sy - sy0), 0)

    glyph = ufoLib2.objects.Glyph()
    cut_glyph = ufoLib2.objects.Glyph()
    gpen = glyph.getPen()
    cpen = cut_glyph.getPen()

    xi, yi = x1 + dx * sx, y2 + dy * sy
    gpen.moveTo((x1, y1))
    gpen.lineTo((x1, y2 + dy * gy))
    gpen.curveTo((x1, y2 + dy * hy), (x1 + dx * hx, y2), (x1 + dx * gx, y2))
    gpen.lineTo((x2, y2))
    gpen.lineTo((x2, yi))
    gpen.lineTo((xi + dx * ix, yi))
    gpen.curveTo((xi, yi), (xi, yi), (xi, yi + dy * iy))
    gpen.lineTo((xi, y1))
    gpen.closePath()

    # Past the end and past the start, as far as the longest curve reaches
    reach_x = abs(x2 - x1) + sx + max(gx, ix)
    reach_y = abs(y2 - y1) + sy + max(gy, iy)
    xe = x2 + dx * reach_x
    _cut(cpen, x2, y1, xe, y2)
    _cut(cpen, x1, y1, xe, y1 + dy * reach_y)

    res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
    res.draw(pen)


def _cut(pen, xa, ya, xb, yb):
    """A rectangle between two corners in any order, always wound alike."""
    draw_rect(pen, min(xa, xb), min(ya, yb), max(xa, xb), max(ya, yb))
