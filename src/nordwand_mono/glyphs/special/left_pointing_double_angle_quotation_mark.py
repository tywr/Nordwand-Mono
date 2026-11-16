from nordwand_mono.glyphs.special.right_pointing_double_angle_quotation_mark import (
    RightPointingDoubleAngleQuotationMarkGlyph,
)


class LeftPointingDoubleAngleQuotationMarkGlyph(
    RightPointingDoubleAngleQuotationMarkGlyph
):
    name = "left_pointing_double_angle_quotation_mark"
    unicode = "0xAB"

    def chevrons(self, b):
        w = (b.x2 - b.x1) * self.chevron_ratio
        return [(b.x1, b.x1 + w), (b.x2 - w, b.x2)]
