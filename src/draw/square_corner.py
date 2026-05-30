import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.rect import draw_rect


def draw_square_corner(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    gx=200,
    gy=200,
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
    ml = max(x2, x1) - min(x2, x1)

    glyph = ufoLib2.objects.Glyph()
    cut_glyph = ufoLib2.objects.Glyph()
    gpen = glyph.getPen()
    cpen = cut_glyph.getPen()
    if orientation == "bottom-left":
        gpen.moveTo((x1, y1))
        gpen.lineTo((x1, y2 + gy))
        gpen.curveTo((x1, y2 + sy / 2), (x1 - sx / 2, y2), (x1 - gx, y2))
        gpen.lineTo((x2, y2))
        gpen.lineTo((x2, y2 + sy))
        gpen.lineTo((x1 - sx - gx, y2 + sy))
        gpen.curveTo((x1 - sx, y2 + sy), (x1 - sx, y2 + sy), (x1 - sx, y2 + sy + gy))
        gpen.lineTo((x1 - sx, y1))
        gpen.closePath()
        draw_rect(cpen, x2 - ml, y1, x2, y2)

    elif orientation == "bottom-right":
        gpen.moveTo((x1, y1))
        gpen.lineTo((x1, y2 + gy))
        gpen.curveTo((x1, y2 + sy / 2), (x1 + sx / 2, y2), (x1 + gx, y2))
        gpen.lineTo((x2, y2))
        gpen.lineTo((x2, y2 + sy))
        gpen.lineTo((x1 + sx + gx, y2 + sy))
        gpen.curveTo((x1 + sx, y2 + sy), (x1 + sx, y2 + sy), (x1 + sx, y2 + sy + gy))
        gpen.lineTo((x1 + sx, y1))
        gpen.closePath()
        draw_rect(cpen, x2, y1, x2 + ml, y2)

    elif orientation == "top-left":
        gpen.moveTo((x1, y1))
        gpen.lineTo((x1, y2 - gy))
        gpen.curveTo((x1, y2 - sy / 2), (x1 - sx / 2, y2), (x1 - gx, y2))
        gpen.lineTo((x2, y2))
        gpen.lineTo((x2, y2 - sy))
        gpen.lineTo((x1 - sx - gx, y2 - sy))
        gpen.curveTo((x1 - sx, y2 - sy), (x1 - sx, y2 - sy), (x1 - sx, y2 - sy - gy))
        gpen.lineTo((x1 - sx, y1))
        gpen.closePath()
        draw_rect(cpen, x2 - ml, y1, x2, y2)

    elif orientation == "top-right":
        gpen.moveTo((x1, y1))
        gpen.lineTo((x1, y2 - gy))
        gpen.curveTo((x1, y2 - sy / 2), (x1 + sx / 2, y2), (x1 + gx, y2))
        gpen.lineTo((x2, y2))
        gpen.lineTo((x2, y2 - sy))
        gpen.lineTo((x1 + sx + gx, y2 - sy))
        gpen.curveTo((x1 + sx, y2 - sy), (x1 + sx, y2 - sy), (x1 + sx, y2 - sy - gy))
        gpen.lineTo((x1 + sx, y1))
        gpen.closePath()
        draw_rect(cpen, x2, y1, x2 + ml, y2)

    res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
    res.draw(pen)
