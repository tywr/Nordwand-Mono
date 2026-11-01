from draw.rect import draw_rect
from glyphs.box import BoxGlyph, box_glyph


class DashedBoxGlyph(BoxGlyph):
    """Line across the cell, cut into `dashes` evenly spaced dashes.

    Dashes stop short of the cell edges, so they don't bleed.
    """

    # Gap between two dashes, relative to the length a dash and its gap span
    gap_ratio = 0.35

    def draw(self, pen, dc):
        (x1, y1, x2, y2), (cx, cy) = self.cell(dc)
        s = self.stroke(self.weight)
        start, end = (x1, x2) if self.horizontal else (y1, y2)
        step = (end - start) / self.dashes
        gap = self.gap_ratio * step
        for i in range(self.dashes):
            a1, a2 = start + i * step + gap / 2, start + (i + 1) * step - gap / 2
            if self.horizontal:
                draw_rect(pen, a1, cy - s / 2, a2, cy + s / 2)
            else:
                draw_rect(pen, cx - s / 2, a1, cx + s / 2, a2)


GLYPHS = [
    box_glyph(DashedBoxGlyph, code, weight=weight, horizontal=horizontal, dashes=dashes)
    for code, weight, horizontal, dashes in [
        (0x2504, "light", True, 3),
        (0x2505, "heavy", True, 3),
        (0x2506, "light", False, 3),
        (0x2507, "heavy", False, 3),
        (0x2508, "light", True, 4),
        (0x2509, "heavy", True, 4),
        (0x250A, "light", False, 4),
        (0x250B, "heavy", False, 4),
        (0x254C, "light", True, 2),
        (0x254D, "heavy", True, 2),
        (0x254E, "light", False, 2),
        (0x254F, "heavy", False, 2),
    ]
]
