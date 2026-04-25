from glyphs.accents import Accent


class Tilde(Accent):
    name = "accent_tilde"
    unicode = None
    rescale = 0.7

    def draw_at(self, pen, dc, x, y):
        from glyphs.special.tilde import TildeGlyph
        from fontTools.pens.recordingPen import RecordingPen
        from fontTools.pens.transformPen import TransformPen
        from fontTools.misc.transform import Transform

        r = self.rescale

        rec = RecordingPen()
        TildeGlyph().draw(rec, dc)

        # The base TildeGlyph is drawn centered at (dc.window_width/2, dc.math).
        # Scale around that point, then translate so it lands at (x, y).
        cx = dc.window_width / 2
        cy = dc.math
        t = Transform()
        t = t.translate(x, y)
        t = t.scale(r)
        t = t.translate(-cx, -cy)

        rec.replay(TransformPen(pen, t))
