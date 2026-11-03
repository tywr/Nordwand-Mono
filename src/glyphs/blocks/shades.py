from draw.rect import draw_rect
from glyphs.blocks import BlockGlyph, block_glyph


class ShadeBlockGlyph(BlockGlyph):
    """Grid of square dots filling the cell.

    The grid is split into 2x2 tiles; `dots` lists the (column, row) of the
    tile filled in. With `inverted`, the cell is filled and those dots are
    holes instead. The grid has an even number of columns and rows, so the
    pattern tiles across cells; dots don't bleed.
    """

    columns = 8  # Even
    dots: tuple = ()
    inverted = False

    def draw(self, pen, dc):
        x1, y1, x2, y2 = self.cell(dc)
        dw = (x2 - x1) / self.columns
        rows = 2 * round((y2 - y1) / dw / 2)  # Even, with dots close to square
        dh = (y2 - y1) / rows
        if self.inverted:
            draw_rect(pen, x1, y1, x2, y2)
        for i in range(self.columns):
            for j in range(rows):
                if (i % 2, j % 2) in self.dots:
                    draw_rect(
                        pen,
                        x1 + i * dw,
                        y1 + j * dh,
                        x1 + (i + 1) * dw,
                        y1 + (j + 1) * dh,
                        clockwise=self.inverted,
                    )


GLYPHS = [
    block_glyph(ShadeBlockGlyph, 0x2591, dots=((0, 0),)),  # ░
    block_glyph(ShadeBlockGlyph, 0x2592, dots=((0, 0), (1, 1))),  # ▒
    block_glyph(ShadeBlockGlyph, 0x2593, dots=((0, 0),), inverted=True),  # ▓
]
