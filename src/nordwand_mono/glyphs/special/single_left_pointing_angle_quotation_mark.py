from nordwand_mono.glyphs.special.single_right_pointing_angle_quotation_mark import (
    SingleRightPointingAngleQuotationMarkGlyph,
)


class SingleLeftPointingAngleQuotationMarkGlyph(
    SingleRightPointingAngleQuotationMarkGlyph
):
    name = "single_left_pointing_angle_quotation_mark"
    unicode = "0x2039"

    def chevrons(self, b):
        return [(b.x1, b.x2)]
