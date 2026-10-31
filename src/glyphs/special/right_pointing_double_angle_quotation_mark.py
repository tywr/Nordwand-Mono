from glyphs.special.single_right_pointing_angle_quotation_mark import (
    SingleRightPointingAngleQuotationMarkGlyph,
)


class RightPointingDoubleAngleQuotationMarkGlyph(
    SingleRightPointingAngleQuotationMarkGlyph
):
    name = "right_pointing_double_angle_quotation_mark"
    unicode = "0xBB"
    width_ratio = 1
    stroke_ratio = 1
    # Width of each chevron, as a fraction of the body width
    chevron_ratio = 0.55

    def chevrons(self, b):
        w = (b.x2 - b.x1) * self.chevron_ratio
        return [(b.x1 + w, b.x1), (b.x2, b.x2 - w)]
