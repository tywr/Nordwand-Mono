from fontTools.pens.transformPen import TransformPen
from config import FontConfig as fc
from glyphs.accents.acute import Acute
from glyphs.accents.dialytika_tonos import DialytikaTonos
from glyphs.accents.dieresis import Dieresis
from glyphs.composed import ComposedGlyph
from glyphs.greek.lowercase.alpha import GreekLowercaseAlphaGlyph
from glyphs.greek.lowercase.epsilon import GreekLowercaseEpsilonGlyph
from glyphs.greek.lowercase.eta import GreekLowercaseEtaGlyph
from glyphs.greek.lowercase.iota import GreekLowercaseIotaGlyph
from glyphs.greek.lowercase.omega import GreekLowercaseOmegaGlyph
from glyphs.greek.lowercase.omicron import GreekLowercaseOmicronGlyph
from glyphs.greek.lowercase.upsilon import GreekLowercaseUpsilonGlyph
from glyphs.greek.uppercase.alpha import GreekUppercaseAlphaGlyph
from glyphs.greek.uppercase.epsilon import GreekUppercaseEpsilonGlyph
from glyphs.greek.uppercase.eta import GreekUppercaseEtaGlyph
from glyphs.greek.uppercase.iota import GreekUppercaseIotaGlyph
from glyphs.greek.uppercase.omega import GreekUppercaseOmegaGlyph
from glyphs.greek.uppercase.omicron import GreekUppercaseOmicronGlyph
from glyphs.greek.uppercase.upsilon import GreekUppercaseUpsilonGlyph


class IotaComposedGlyph(ComposedGlyph):
    """The stem of the iota is not centered on its body"""

    def accent_x(self, dc, base, b):
        return base.stem_center(dc) + base.accent_x_offset


class UppercaseTonosGlyph(ComposedGlyph):
    """Capital with the tonos on its top-left side: the capital is shifted
    to the right, as a fraction of its width, to make room for it"""

    accent_class = Acute
    shift = 0.0
    tonos_scale = 0.75
    tonos_height = 1.25
    tonos_stroke = 1.15
    tonos_shift = 0.0

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        base = base_class()
        b = dc.body_bounds(offset=base_class.offset, height="cap", uppercase=True)

        dx = self.shift * (b.x2 - b.x1)
        base.draw(TransformPen(pen, (1, 0, 0, 1, dx, 0)), dc)

        # Tonos ending a gap away from the left of the shifted capital
        tonos = self.accent_class()
        tonos.stroke_ratio *= self.tonos_stroke
        tonos.scaled(dc, self.tonos_scale)
        tonos.height *= self.tonos_height
        h = tonos.height * dc.x_height
        tdx = self.tonos_shift * dc.window_width
        tonos.draw_at(pen, dc, b.x1 + tdx, dc.cap - h / 2)


class GreekLowercaseAlphaTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_alpha_tonos"
    unicode = "0x03AC"
    base_glyph_class = GreekLowercaseAlphaGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseEpsilonTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_epsilon_tonos"
    unicode = "0x03AD"
    base_glyph_class = GreekLowercaseEpsilonGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseEtaTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_eta_tonos"
    unicode = "0x03AE"
    base_glyph_class = GreekLowercaseEtaGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseIotaTonosGlyph(IotaComposedGlyph):
    name = "greek_lowercase_iota_tonos"
    unicode = "0x03AF"
    base_glyph_class = GreekLowercaseIotaGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseOmicronTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_omicron_tonos"
    unicode = "0x03CC"
    base_glyph_class = GreekLowercaseOmicronGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseUpsilonTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_upsilon_tonos"
    unicode = "0x03CD"
    base_glyph_class = GreekLowercaseUpsilonGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseOmegaTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_omega_tonos"
    unicode = "0x03CE"
    base_glyph_class = GreekLowercaseOmegaGlyph
    accent_class = Acute
    accent_y = fc.accent


class GreekLowercaseIotaDialytikaGlyph(IotaComposedGlyph):
    name = "greek_lowercase_iota_dialytika"
    unicode = "0x03CA"
    base_glyph_class = GreekLowercaseIotaGlyph
    accent_class = Dieresis
    accent_y = fc.accent


class GreekLowercaseUpsilonDialytikaGlyph(ComposedGlyph):
    name = "greek_lowercase_upsilon_dialytika"
    unicode = "0x03CB"
    base_glyph_class = GreekLowercaseUpsilonGlyph
    accent_class = Dieresis
    accent_y = fc.accent


class GreekUppercaseIotaDialytikaGlyph(ComposedGlyph):
    name = "greek_uppercase_iota_dialytika"
    unicode = "0x03AA"
    base_glyph_class = GreekUppercaseIotaGlyph
    accent_class = Dieresis
    accent_y = fc.accent_cap


class GreekUppercaseUpsilonDialytikaGlyph(ComposedGlyph):
    name = "greek_uppercase_upsilon_dialytika"
    unicode = "0x03AB"
    base_glyph_class = GreekUppercaseUpsilonGlyph
    accent_class = Dieresis
    accent_y = fc.accent_cap


class GreekLowercaseIotaDialytikaTonosGlyph(IotaComposedGlyph):
    name = "greek_lowercase_iota_dialytika_tonos"
    unicode = "0x0390"
    base_glyph_class = GreekLowercaseIotaGlyph
    accent_class = DialytikaTonos
    accent_y = fc.accent


class GreekLowercaseUpsilonDialytikaTonosGlyph(ComposedGlyph):
    name = "greek_lowercase_upsilon_dialytika_tonos"
    unicode = "0x03B0"
    base_glyph_class = GreekLowercaseUpsilonGlyph
    accent_class = DialytikaTonos
    accent_y = fc.accent


class GreekUppercaseAlphaTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_alpha_tonos"
    unicode = "0x0386"
    base_glyph_class = GreekUppercaseAlphaGlyph
    shift = 0.05


class GreekUppercaseEpsilonTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_epsilon_tonos"
    unicode = "0x0388"
    base_glyph_class = GreekUppercaseEpsilonGlyph
    tonos_shift = -0.15
    shift = 0.15


class GreekUppercaseEtaTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_eta_tonos"
    unicode = "0x0389"
    base_glyph_class = GreekUppercaseEtaGlyph
    tonos_shift = -0.15
    shift = 0.15


class GreekUppercaseIotaTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_iota_tonos"
    unicode = "0x038A"
    base_glyph_class = GreekUppercaseIotaGlyph
    tonos_shift = -0.15
    shift = 0.15


class GreekUppercaseOmicronTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_omicron_tonos"
    unicode = "0x038C"
    base_glyph_class = GreekUppercaseOmicronGlyph
    tonos_shift = -0.15
    shift = 0.15


class GreekUppercaseUpsilonTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_upsilon_tonos"
    unicode = "0x038E"
    base_glyph_class = GreekUppercaseUpsilonGlyph
    tonos_shift = -0.15
    shift = 0.15


class GreekUppercaseOmegaTonosGlyph(UppercaseTonosGlyph):
    name = "greek_uppercase_omega_tonos"
    unicode = "0x038F"
    base_glyph_class = GreekUppercaseOmegaGlyph
    tonos_shift = -0.15
    shift = 0.15
