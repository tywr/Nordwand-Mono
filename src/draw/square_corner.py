import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from config import FontConfig
from draw.rect import draw_rect


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

    The corner point is at (x2, y1) or (x1, y2) depending on orientation:
        bottom-right: corner at (x2, y1) — curve goes right then up
        top-right:    corner at (x1, y2) — curve goes up then right
        top-left:     corner at (x2, y1) — curve goes left then down
        bottom-left:  corner at (x1, y2) — curve goes down then left
    """
    sx, sy = stroke_x, stroke_y
    ml = 2 * (max(x2, x1) - min(x2, x1))
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

    if dx > 0:
        draw_rect(cpen, x2, y1, x2 + ml, y2)
    else:
        draw_rect(cpen, x2 - ml, y1, x2, y2)
    if orientation == "bottom-left":
        draw_rect(cpen, x2, y1, x1, y1 + 100)
    elif orientation == "top-right":
        draw_rect(cpen, x1, y1 - 100, x2, y1)

    res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
    res.draw(pen)
