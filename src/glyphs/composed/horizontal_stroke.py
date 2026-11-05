"""Composed glyphs with a horizontal stroke or bar (ħ Ħ đ Đ Ɖ ŧ Ŧ ɨ Ɨ)."""

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.uppercase.t import UppercaseTGlyph
from glyphs.uppercase.h import UppercaseHGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.square.h import LowercaseHGlyph
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.latin.uppercase.eth import UppercaseEthGlyph
from draw.rect import draw_rect


class LowercaseHStrokeGlyph(LowercaseHGlyph):
    name = "lowercase_hbar"
    unicode = "0x127"
    # Bar reach past the stem, as fractions of the body width
    bar_left = 0.15
    bar_right = 0.45

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(width_ratio=self.width_ratio, offset=self.offset)
        y = (dc.x_height + dc.ascent) / 2
        draw_rect(
            pen,
            b.x1 - self.bar_left * b.width,
            y - dc.stroke_alt / 2,
            b.x1 + dc.stroke_x + self.bar_right * b.width,
            y + dc.stroke_alt / 2,
        )


class UppercaseHStrokeGlyph(UppercaseHGlyph):
    name = "uppercase_hbar"
    unicode = "0x126"
    bar_y = 0.78  # Relative to the cap height
    bar_overhang = 0.15  # Past each stem, relative to the body width

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        s = dc.stroke_alt
        y = self.bar_y * b.height
        o = self.bar_overhang * b.width
        draw_rect(pen, b.x1 - o, y - s / 2, b.x2 + o, y + s / 2)


class UppercaseDStrokeGlyph(UppercaseEthGlyph):
    """Drawn exactly like the Icelandic eth `Ð`."""

    name = "uppercase_dcroat"
    unicode = "0x110"


class UppercaseDAfricanGlyph(UppercaseEthGlyph):
    """Drawn exactly like the Icelandic eth `Ð`."""

    name = "uppercase_dafrican"
    unicode = "0x189"


class LowercaseDStrokeGlyph(LowercaseDGlyph):
    """d with a bar across its ascender, at the height of the one on ħ."""

    name = "lowercase_dcroat"
    unicode = "0x111"
    # Bar reach past the stem, as fractions of the body width
    bar_left = 0.25
    bar_right = 0.2

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            width_ratio=self.width_ratio, offset=self.offset, height="ascent"
        )
        y = (dc.x_height + dc.ascent) / 2
        draw_rect(
            pen,
            b.x2 - dc.stroke_x - self.bar_left * b.width,
            y - dc.stroke_alt / 2,
            b.x2 + self.bar_right * b.width,
            y + dc.stroke_alt / 2,
        )


class TStrokeComposedGlyph(ComposedGlyph):
    """t/T with a horizontal bar crossing the stem."""

    bar_y = 0.5
    bar_width = 0.8
    rl_ratio = 0.5
    stroke = "stroke_y"

    def body(self, base, dc): ...

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b, _ = self.body(base, dc)
        s = getattr(dc, self.stroke)
        y = self.bar_y * b.height
        w = self.bar_width * b.width
        rw = w * self.rl_ratio
        lw = w * (1 - self.rl_ratio)
        draw_rect(pen, b.xmid - lw, y - s / 2, b.xmid + rw, y + s / 2)


class LowercaseTStrokeGlyph(TStrokeComposedGlyph):
    name = "lowercase_tbar"
    unicode = "0x167"
    base_glyph_class = LowercaseTGlyph
    bar_y = 0.56
    rl_ratio = 0.58
    stroke = "stroke_alt"

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset, height="x_height", width_ratio=base.width_ratio
        )
        return b, dc.stroke_y


class UppercaseTStrokeGlyph(TStrokeComposedGlyph):
    name = "uppercase_tbar"
    unicode = "0x166"
    base_glyph_class = UppercaseTGlyph

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset,
            height="cap",
            width_ratio=base.width_ratio,
            min_margin=dc.min_margin_uppercase,
        )
        return b, dc.stroke_y * base.stroke_y_ratio


class LowercaseIStrokeGlyph(TStrokeComposedGlyph):
    name = "lowercase_istroke"
    unicode = "0x268"
    base_glyph_class = LowercaseIGlyph
    bar_y = 0.5
    bar_width = 0.7
    stroke = "stroke_alt"

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset, height="x_height", width_ratio=base.width_ratio
        )
        return b, dc.stroke_y


class UppercaseIStrokeGlyph(TStrokeComposedGlyph):
    name = "uppercase_istroke"
    unicode = "0x197"
    base_glyph_class = UppercaseIGlyph
    stroke = "stroke_alt"

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset, height="cap", width_ratio=base.width_ratio
        )
        return b, dc.stroke_y
