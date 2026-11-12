from abc import ABC
from dataclasses import replace

import ufoLib2
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph
from glyphs.composed import _italic_base


class JointGlyph(Glyph, ABC):
    """Two existing glyphs side by side in a single cell (digraphs such as
    ʧ). Each one is squeezed horizontally to fill its share of the body
    bounds: the left one the first `scale_left` of the body width (0.5 splits
    it 50/50), the right one the rest. They are drawn with a thicker vertical
    stroke beforehand, so their stems keep the stroke width of the font once
    squeezed. `overlap` extends the right one leftwards by that fraction of
    the body width, e.g. to join a bar of the left glyph to a stem of the
    right one."""

    left_class = None
    right_class = None
    offset = 0
    width_ratio = 1
    overlap = 0
    scale_left = 0.5

    def _outline(self, glyph_class, dc):
        if dc.italic:
            glyph_class = _italic_base(glyph_class)
        glyph = ufoLib2.objects.Glyph()
        glyph_class().draw(glyph.getPen(), dc)
        x1, _, x2, _ = glyph.getBounds()
        return glyph, x1, x2

    def _spans(self, b):
        """Horizontal extent (x1, x2) of the left and the right glyph."""
        xj = b.x1 + self.scale_left * b.width
        return (b.x1, xj), (xj - self.overlap * b.width, b.x2)

    def _scales(self, b, parts):
        return [
            (s2 - s1) / (x2 - x1)
            for (s1, s2), (_, x1, x2) in zip(self._spans(b), parts)
        ]

    def extra_draw(self, pen, dc): ...

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        classes = (self.left_class, self.right_class)
        scales = self._scales(b, [self._outline(c, dc) for c in classes])
        # Redraw with the stems thickened by the inverse of each squeeze
        parts = [
            self._outline(c, replace(dc, stroke_x=dc.stroke_x / scale))
            for c, scale in zip(classes, scales)
        ]
        scales = self._scales(b, parts)

        for (glyph, x1, _), scale, (s1, _) in zip(parts, scales, self._spans(b)):
            glyph.draw(TransformPen(pen, (scale, 0, 0, 1, s1 - scale * x1, 0)))

        self.extra_draw(pen, dc)
