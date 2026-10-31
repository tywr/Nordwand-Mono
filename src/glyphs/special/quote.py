from glyphs import Glyph
from glyphs.special.quotation_mark import QuotationMarkGlyph
from draw.dot import draw_dot, dot_size
from draw.parallelogramm import draw_parallelogramm, parallelogramm_delta


class QuoteGlyph(Glyph):
    """Base shape of the curly quotes: a wedge hanging from the ascent.

    Centered in the cell on its bounding box, so `offset` only nudges it
    away from the center. `turned` rotates it 180° for the opening quotes,
    `double` draws it twice, spaced like the bars of `"`. `low` drops it so
    the head sits on the baseline, with the tail below like a comma.

    Leaves `unicode` undefined so it stays abstract and isn't exported;
    each quote subclass sets its own.
    """

    name = "quote"
    offset = 0
    width_ratio = 1
    tail_ratio = 2
    foot_offset = 0.05
    stroke_ratio = 1
    head_ratio = 1.5
    tail_stroke_ratio = 0.75
    gap = QuotationMarkGlyph.gap
    turned = False
    double = False
    low = False

    def shape(self, dc):
        """Head dot center, and the tail's lower-left and upper-right corners,
        turned and centered in the cell."""
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sx = self.stroke_ratio * dc.stroke_x
        st = self.tail_stroke_ratio * dc.stroke_x
        fx = self.foot_offset * b.width
        w, h = dot_size(dc, self.head_ratio)
        top = h if self.low else dc.ascent
        bottom = top - h * self.tail_ratio
        xl, xr = b.xmid - w / 2, b.xmid + w / 2

        # Tail hanging from the right part of the head
        head = (b.xmid, top - h / 2)
        foot, joint = (b.xmid - sx / 2 - fx, bottom), (xr, top - h)
        d = parallelogramm_delta(st, *foot, *joint)
        xs = [xl, xr, foot[0], foot[0] + d]
        cx, cy = (min(xs) + max(xs)) / 2, (top + bottom) / 2
        pts = [head, foot, joint]
        if self.turned:
            # Rotating swaps the tail's ends: the joint becomes its lower-left
            pts = [(2 * cx - x, 2 * cy - y) for x, y in (head, joint, foot)]
        pts = [(x + b.xmid - cx, y) for x, y in pts]
        return pts[0], pts[1], pts[2]

    def draw(self, pen, dc):
        (hx, hy), (x1, y1), (x2, y2) = self.shape(dc)
        st = self.tail_stroke_ratio * dc.stroke_x
        offsets = (0,)
        if self.double:
            b = dc.body_bounds(
                offset=self.offset, height="x_height", width_ratio=self.width_ratio
            )
            d = (self.gap * b.width + self.stroke_ratio * dc.stroke_x) / 2
            offsets = (-d, d)
        for dx in offsets:
            draw_dot(pen, dc, hx + dx, hy, self.head_ratio)
            draw_parallelogramm(pen, st, x1 + dx, y1, x2 + dx, y2)
