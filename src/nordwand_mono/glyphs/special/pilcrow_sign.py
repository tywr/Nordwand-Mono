from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.shapes.superellipse import Superellipse


class PilcrowSignGlyph(Glyph):
    """Two stems on the right, joined at the top to a solid half-round bowl."""

    name = "pilcrow_sign"
    unicode = "0xB6"
    offset = 0
    width_ratio = 1
    gap = 0.2  # Between the two stems, relative to the body width
    bowl_ratio = 0.55  # Bowl height, relative to the cap height
    width_ratio = 1.05

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        x_inner = b.x2 - 2 * sx - self.gap * b.width  # Left edge of the inner stem

        # Stems
        draw_rect(pen, b.x2 - sx, 0, b.x2, dc.cap)
        draw_rect(pen, x_inner, 0, x_inner + sx, dc.cap)

        # Solid bowl: the left half of a superellipse ending at the inner stem
        h = self.bowl_ratio * dc.cap
        w = x_inner - b.x1
        Superellipse(
            x1=b.x1,
            y1=dc.cap - h,
            x2=x_inner + w,
            y2=dc.cap,
            hx=dc.cap_hx * w / dc.width,
            hy=dc.cap_hy * h / dc.x_height,
        ).draw(pen, cut="right")

        # Top bar joining the bowl to the outer stem
        draw_rect(pen, x_inner, dc.cap - sy, b.x2, dc.cap)
