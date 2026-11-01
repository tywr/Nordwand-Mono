from draw.rect import draw_rect
from glyphs.blocks import BlockGlyph, block_glyph


class RectBlockGlyph(BlockGlyph):
    """Rectangles given as fractions (x1, y1, x2, y2) of the cell.

    Sides lying on the cell edge bleed into the neighbouring cell.
    """

    rects: tuple = ()

    def draw(self, pen, dc):
        cx1, cy1, cx2, cy2 = self.cell(dc)
        w, h, b = cx2 - cx1, cy2 - cy1, self.bleed
        for fx1, fy1, fx2, fy2 in self.rects:
            draw_rect(
                pen,
                cx1 + fx1 * w - (b if fx1 == 0 else 0),
                cy1 + fy1 * h - (b if fy1 == 0 else 0),
                cx1 + fx2 * w + (b if fx2 == 1 else 0),
                cy1 + fy2 * h + (b if fy2 == 1 else 0),
            )


# Quadrants
LL, LR, UL, UR = (0, 0, 0.5, 0.5), (0.5, 0, 1, 0.5), (0, 0.5, 0.5, 1), (0.5, 0.5, 1, 1)

GLYPHS = [
    block_glyph(RectBlockGlyph, code, rects=rects)
    for code, rects in [
        (0x2580, [(0, 1 / 2, 1, 1)]),  # ▀
        (0x2581, [(0, 0, 1, 1 / 8)]),  # ▁
        (0x2582, [(0, 0, 1, 2 / 8)]),  # ▂
        (0x2583, [(0, 0, 1, 3 / 8)]),  # ▃
        (0x2584, [(0, 0, 1, 4 / 8)]),  # ▄
        (0x2585, [(0, 0, 1, 5 / 8)]),  # ▅
        (0x2586, [(0, 0, 1, 6 / 8)]),  # ▆
        (0x2587, [(0, 0, 1, 7 / 8)]),  # ▇
        (0x2588, [(0, 0, 1, 1)]),  # █
        (0x2589, [(0, 0, 7 / 8, 1)]),  # ▉
        (0x258A, [(0, 0, 6 / 8, 1)]),  # ▊
        (0x258B, [(0, 0, 5 / 8, 1)]),  # ▋
        (0x258C, [(0, 0, 4 / 8, 1)]),  # ▌
        (0x258D, [(0, 0, 3 / 8, 1)]),  # ▍
        (0x258E, [(0, 0, 2 / 8, 1)]),  # ▎
        (0x258F, [(0, 0, 1 / 8, 1)]),  # ▏
        (0x2590, [(1 / 2, 0, 1, 1)]),  # ▐
        (0x2594, [(0, 7 / 8, 1, 1)]),  # ▔
        (0x2595, [(7 / 8, 0, 1, 1)]),  # ▕
        (0x2596, [LL]),  # ▖
        (0x2597, [LR]),  # ▗
        (0x2598, [UL]),  # ▘
        (0x2599, [UL, LL, LR]),  # ▙
        (0x259A, [UL, LR]),  # ▚
        (0x259B, [UL, UR, LL]),  # ▛
        (0x259C, [UL, UR, LR]),  # ▜
        (0x259D, [UR]),  # ▝
        (0x259E, [UR, LL]),  # ▞
        (0x259F, [UR, LL, LR]),  # ▟
    ]
]
