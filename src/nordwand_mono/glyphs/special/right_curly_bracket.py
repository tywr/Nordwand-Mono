from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen

from nordwand_mono.glyphs import Glyph


def _draw_segments(pen, points, reverse=False):
    """Trace one half of an edge, starting at the pen's current position."""
    if reverse:
        segments = reversed([
            (*segment[-2::-1], previous[-1])
            for previous, segment in zip(points, points[1:])
        ])
    else:
        segments = points[1:]
    for segment in segments:
        if len(segment) == 1:
            pen.lineTo(segment[0])
        else:
            pen.curveTo(*segment)


class RightCurlyBracketGlyph(Glyph):
    name = "right_curly_bracket"
    unicode = "0x7D"
    offset = 0
    mirrored = True

    def draw(self, pen, dc):
        body = dc.body_bounds(offset=self.offset)
        sx, sy = dc.stroke_x, dc.stroke_y
        half_height = dc.parenthesis_length / 2
        # The approved outline uses a 340-unit body and a 980-unit bracket.
        wx = dc.width / 340
        hy = half_height / 490
        tip = body.x1 + 13 * wx
        end = body.x2 - 13 * wx
        shoulder = body.xmid - 61 * wx - (sx - 82) * 0.34
        waist = shoulder + 16 * wx
        shoulder_y = 366 * hy
        inner_shoulder_y = shoulder_y - (sy - 70) * 0.36
        tip_y = sy * 0.60

        # Upper halves of the outer and inner edges, in the left brace.
        outer = (
            ((end, half_height),),
            ((end - 108 * wx, half_height),),
            ((end - 202 * wx, half_height), (shoulder - 7 * wx, 458 * hy), (shoulder, shoulder_y)),
            ((waist, 176 * hy),),
            ((waist + 6 * wx, 106 * hy), (tip + 97 * wx, tip_y), (tip + 25 * wx, tip_y)),
            ((tip, tip_y),),
        )
        inner = (
            ((end, half_height - sy),),
            ((end - 108 * wx, half_height - sy),),
            (
                (end - 160 * wx, half_height - sy),
                (shoulder + sx - 4 * wx, inner_shoulder_y + 40 * hy),
                (shoulder + sx, inner_shoulder_y),
            ),
            ((waist + sx, 176 * hy),),
            ((waist + sx + 8 * wx, 86 * hy), (tip + 167 * wx, 15 * hy), (tip + 104 * wx, 0)),
        )

        if self.mirrored:
            mirror = (-1, 0, 0, 1, dc.window_width, 0)
            pen = TransformPen(ReverseContourPen(pen), mirror)
        upper = TransformPen(pen, (1, 0, 0, 1, 0, dc.parenthesis))
        lower = TransformPen(pen, (1, 0, 0, -1, 0, dc.parenthesis))

        upper.moveTo(outer[0][0])
        _draw_segments(upper, outer)
        lower.lineTo(outer[-1][-1])
        _draw_segments(lower, outer, reverse=True)
        lower.lineTo(inner[0][0])
        _draw_segments(lower, inner)
        _draw_segments(upper, inner, reverse=True)
        upper.closePath()
