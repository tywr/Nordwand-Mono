"""Letters with a hook (Ɓ Ɗ Ƒ Ƙ Ʋ Ƴ Ɲ ɓ ɖ ɗ ƙ ʋ ƴ ɲ)."""

from draw.parallelogramm import parallelogramm_delta
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner
from glyphs.uppercase.bowl.b import UppercaseBGlyph
from glyphs.uppercase.bowl.d import UppercaseDGlyph
from glyphs.uppercase.f import UppercaseFGlyph
from glyphs.uppercase.k import UppercaseKGlyph
from glyphs.uppercase.stem_diagonal.n import UppercaseNGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.diagonal.y import UppercaseYGlyph
from glyphs.lowercase.k import LowercaseKGlyph
from glyphs.lowercase.single_story.b import LowercaseBGlyph
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.greek.lowercase.upsilon import GreekLowercaseUpsilonGlyph


class OuterHookedGlyph:
    """Mixin drawing the base letter narrowed by `hook_scale` and pushed away
    from `hook_side`, so the hook drawn by `draw_hook` fits in the cell.

    Narrowing goes through width_ratio and offset, so the strokes keep their
    weight. Put it before the base class: `class X(OuterHookedGlyph, BaseGlyph)`.
    """

    hook_side = "left"  # Side of the cell the hook needs room on
    hook_scale = 0.88  # Width of the base, relative to its normal width
    hook_length = 0.5  # Reach of the hook, relative to the body width
    hook_curve = 0.7  # Size of the curve of the hook, relative to its reach

    def draw(self, pen, dc):
        width_ratio, offset = self.width_ratio, self.offset
        shift = dc.width * width_ratio * (1 - self.hook_scale) / 2
        self.width_ratio = width_ratio * self.hook_scale
        self.offset = offset + (shift if self.hook_side == "left" else -shift)
        try:
            super().draw(pen, dc)
            self.draw_hook(pen, dc)
        finally:
            self.width_ratio, self.offset = width_ratio, offset

    def draw_hook(self, pen, dc): ...

    def cap_bounds(self, dc, **kwargs):
        return dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
            **kwargs,
        )


class EdgeHookedGlyph(OuterHookedGlyph):
    """A hook on the `hook_side` edge that fits in the body of the base, b.x1
    to b.x2: the hook reaches the edge, and the base is drawn on the rest,
    `hook_scale * b.width` away from it."""

    hook_scale = 0.25
    base_kwargs = {}  # Passed to the base draw, e.g. {"draw_stem": False}

    def hook_bounds(self, dc):
        return self.cap_bounds(dc)

    def draw(self, pen, dc):
        width_ratio, offset = self.width_ratio, self.offset
        b = self.hook_bounds(dc)
        room = self.hook_scale * b.width
        if self.hook_side == "left":
            x1, x2, edge = b.x1 + room, b.x2, b.x1
        else:
            x1, x2, edge = b.x1, b.x2 - room, b.x2
        self.width_ratio = (x2 - x1 - dc.stroke_x) / dc.width
        self.offset = offset + (x1 + x2 - b.x1 - b.x2) / 2
        try:
            super(OuterHookedGlyph, self).draw(pen, dc, **self.base_kwargs)
            self.draw_hook(pen, dc, edge)
        finally:
            self.width_ratio, self.offset = width_ratio, offset


class TopHookedGlyph(EdgeHookedGlyph):
    """The top of the stem runs out to the edge and curls down (Ɓ Ɗ ɗ)."""

    hook_drop = 0.33  # Height of the hook, relative to the body height

    def draw_hook(self, pen, dc, edge):
        b = self.hook_bounds(dc)
        sx = dc.stroke_x * getattr(self, "stroke_x_ratio", 1)
        sy = dc.stroke_y * getattr(self, "stroke_y_ratio", 1)
        sx = max(0, 0.3 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)
        y1 = b.y2 - self.hook_drop * b.height
        if self.hook_side == "left":
            x2, orientation = b.x1 + sx, "top-right"
        else:
            x2, orientation = b.x2 - sx, "top-left"
        draw_square_corner(pen, sx, sy, edge, y1, x2, b.y2, orientation=orientation)


class BottomLeftHookedGlyph(EdgeHookedGlyph):
    """The left stem goes below the baseline and curls to the left (Ɲ ɲ)."""

    def draw_hook(self, pen, dc, edge):
        b = self.hook_bounds(dc)
        sx = dc.stroke_x * getattr(self, "stroke_x_ratio", 1)
        sy = dc.stroke_y * getattr(self, "stroke_y_ratio", 1)
        draw_square_corner(
            pen,
            sx,
            sy,
            b.x1 + sx,
            b.y1,
            edge,
            dc.descent,
            orientation="bottom-left",
        )


class FlagHookedGlyph(OuterHookedGlyph):
    """A branch ending in a flag to the right (Ƙ Ƴ ƴ)."""

    hook_side = "right"

    def branch_top(self, dc):
        """(x, delta, y, width): right end, section and height of the top of
        the branch, and the body width."""
        ...

    def draw_hook(self, pen, dc):
        x, d, y, width = self.branch_top(dc)
        sy = dc.stroke_y * getattr(self, "stroke_y_ratio", 1)
        draw_rect(pen, x - d, y - sy, x + self.hook_length * width, y)


class InnerHookedGlyph:
    """Mixin drawing the base letter at its normal size, its ascender stem
    replaced by one whose top curls to the right over the letter (ɓ ƙ). The
    base draw must take `draw_stem`.
    Put it before the base class: `class X(InnerHookedGlyph, BaseGlyph)`.
    """

    hook_length = 0.4  # Reach of the hook, relative to the body width
    hook_y = 0.5  # Where the curl starts, between the x-height and the ascent

    def stem_x(self, dc):
        """Left edge of the ascender stem."""
        ...

    def draw(self, pen, dc):
        super().draw(pen, dc, draw_stem=False)
        x = self.stem_x(dc)
        reach = self.hook_length * dc.width
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x,
            0,
            x + dc.stroke_x + reach,
            dc.ascent,
            orientation="top-right",
        )


class UppercaseBHookGlyph(TopHookedGlyph, UppercaseBGlyph):
    name = "uppercase_bhook"
    unicode = "0x181"
    offset = -7
    width_ratio = 1.26


class UppercaseDHookGlyph(TopHookedGlyph, UppercaseDGlyph):
    name = "uppercase_dhook"
    unicode = "0x18A"
    offset = -7
    width_ratio = 1.26


class UppercaseNLeftHookGlyph(BottomLeftHookedGlyph, UppercaseNGlyph):
    name = "uppercase_nlefthook"
    unicode = "0x19D"
    hook_scale = 0.15
    offset = -20
    width_ratio = 1.2

    def hook_bounds(self, dc):
        return self.body(dc)


class UppercaseFHookGlyph(BottomLeftHookedGlyph, UppercaseFGlyph):
    """The stem goes below the baseline and curls to the left (Ƒ)."""

    name = "uppercase_fhook"
    unicode = "0x191"
    hook_scale = 0.2
    offset = 0
    width_ratio = 1.1


class UppercaseKHookGlyph(FlagHookedGlyph, UppercaseKGlyph):
    """The upper branch ends in a flag to the right (Ƙ)."""

    name = "uppercase_khook"
    unicode = "0x198"
    hook_scale = 0.82
    hook_length = 0.18

    def branch_top(self, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
            height="cap",
        )
        xtop = b.x2 - self.upper_branch_offset * b.width
        # Section of the upper branch, shared with the lower one
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        ymid = b.y1 + self.mid_ratio * b.height
        d = parallelogramm_delta(
            self.lower_stroke_ratio * dc.stroke_x, xb, ymid, b.x2, b.y1
        )
        return xtop, d, b.y2, b.width


class UppercaseYHookGlyph(FlagHookedGlyph, UppercaseYGlyph):
    """The right branch ends in a flag to the right (Ƴ)."""

    name = "uppercase_yhook"
    unicode = "0x1B3"
    hook_scale = 0.8
    hook_length = 0.15

    def branch_top(self, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        sx = dc.stroke_x * self.stroke_x_ratio
        yj = b.x1 + self.junction_ratio * b.height
        s = self.branch_stroke_ratio * sx
        d = parallelogramm_delta(s, b.xmid - sx / 2, yj, b.x2, b.y2)
        return b.x2, d, b.y2, b.width


class LowercaseBHookGlyph(InnerHookedGlyph, LowercaseBGlyph):
    name = "lowercase_bhook"
    unicode = "0x253"

    def stem_x(self, dc):
        return dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            overshoot_right=True,
        ).x1


class LowercaseKHookGlyph(InnerHookedGlyph, LowercaseKGlyph):
    name = "lowercase_khook"
    unicode = "0x199"

    def stem_x(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
        ).x1


class LowercaseDHookGlyph(EdgeHookedGlyph, LowercaseDGlyph):
    """The stem is drawn curling to the right edge, as in ɓ ƙ."""

    name = "lowercase_dhook"
    unicode = "0x257"
    hook_side = "right"
    hook_scale = 0.2
    base_kwargs = {"draw_stem": False}

    def hook_bounds(self, dc):
        return dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            overshoot_left=True,
            height="ascent",
        )

    def draw_hook(self, pen, dc, edge):
        b = self.hook_bounds(dc)
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2 - dc.stroke_x,
            0,
            edge,
            dc.ascent,
            orientation="top-right",
        )


class LowercaseDTailGlyph(LowercaseDHookGlyph):
    """The stem goes below the baseline and curls to the right (ɖ)."""

    name = "lowercase_dtail"
    unicode = "0x256"

    def draw_hook(self, pen, dc, edge):
        b = self.hook_bounds(dc)
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2 - dc.stroke_x,
            dc.ascent,
            edge,
            dc.descent,
            orientation="bottom-right",
        )


class LowercaseNLeftHookGlyph(BottomLeftHookedGlyph, LowercaseNGlyph):
    name = "lowercase_nlefthook"
    unicode = "0x272"
    hook_scale = 0.15

    def hook_bounds(self, dc):
        return dc.body_bounds(
            offset=self.offset, overshoot_top=True, width_ratio=self.width_ratio
        )


class LowercaseYHookGlyph(FlagHookedGlyph, LowercaseYGlyph):
    name = "lowercase_yhook"
    unicode = "0x1B4"
    hook_scale = 0.85
    hook_length = 0.12

    def branch_top(self, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        d = parallelogramm_delta(s, b.xmid - self.overlap * s, b.y1, b.x2, b.y2)
        return b.x2, d, b.y2, b.width


class UppercaseVHookGlyph(UppercaseUGlyph):
    """U whose right side curls in to the middle at the top (Ʋ)."""

    name = "uppercase_vhook"
    unicode = "0x1B2"

    def draw(self, pen, dc):
        super().draw(pen, dc, draw_right_side=False)
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ym = (b.y1 + self.loop_ratio * b.height) / 2
        draw_square_corner(pen, sx, sy, b.x2, ym, b.xmid, b.y2, orientation="top-left")


class LowercaseVHookGlyph(GreekLowercaseUpsilonGlyph):
    """υ whose right side curls in to the middle at the top (ʋ)."""

    name = "lowercase_vhook"
    unicode = "0x28B"

    def draw(self, pen, dc):
        super().draw(pen, dc, draw_right_side=False)
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        ym = (b.y1 + self.loop_ratio * b.height + b.y1) / 2
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            ym,
            b.xmid,
            dc.x_height,
            orientation="top-left",
        )
