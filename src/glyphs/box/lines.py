import unicodedata

from draw.rect import draw_rect
from glyphs.box import BoxGlyph, box_glyph

# Arms perpendicular to each arm: the one on the negative side first
PERPENDICULARS = {
    "left": ("down", "up"),
    "right": ("down", "up"),
    "down": ("left", "right"),
    "up": ("left", "right"),
}


class LineBoxGlyph(BoxGlyph):
    """Lines running from the centre of the cell to some of its edges.

    `arms` maps each direction (up, right, down, left) to its weight:
    light, heavy or double.
    """

    arms: dict = {}

    def extent(self, weight):
        """Half the thickness of an arm, across its direction."""
        if weight is None:
            return 0
        if weight == "double":
            return self.double_offset() + self.double_stroke / 2
        return self.stroke(weight) / 2

    def draw(self, pen, dc):
        (x1, y1, x2, y2), (cx, cy) = self.cell(dc)
        b = self.bleed
        edges = {"left": cx - x1 + b, "right": x2 - cx + b, "down": cy - y1 + b, "up": y2 - cy + b}

        for arm, weight in self.arms.items():
            perps = [self.arms.get(p) for p in PERPENDICULARS[arm]]
            # Each line as (across offset, stroke, start), where `start` is
            # how far the line reaches back past the centre
            if weight == "double":
                o, s = self.double_offset(), self.double_stroke
                lines = []
                for side, perp in zip((-1, 1), perps):
                    if perp == "double":
                        start = s / 2 - o  # Inner corner
                    elif "double" in perps:
                        start = o + s / 2  # Outer corner
                    else:
                        start = max(self.extent(p) for p in perps)
                    lines.append((side * o, s, start))
            else:
                if perps == ["double", "double"]:
                    # Stop at the nearest of the two lines it meets
                    start = self.double_stroke / 2 - self.double_offset()
                else:
                    start = max(self.extent(p) for p in perps)
                lines = [(0, self.stroke(weight), start)]

            sign = 1 if arm in ("right", "up") else -1
            for across, s, start in lines:
                a1, a2 = cx + sign * -start, cx + sign * edges[arm]
                if arm in ("left", "right"):
                    draw_rect(pen, min(a1, a2), cy + across - s / 2, max(a1, a2), cy + across + s / 2)
                else:
                    a1, a2 = cy + sign * -start, cy + sign * edges[arm]
                    draw_rect(pen, cx + across - s / 2, min(a1, a2), cx + across + s / 2, max(a1, a2))


class DoubleLineBoxGlyph(LineBoxGlyph):
    # In units, the same for every weight
    double_stroke = 58
    double_gap = 84

    def double_offset(self):
        """Distance from the centre of the arm to the centre of each line."""
        return (self.double_gap + self.double_stroke) / 2


def parse_arms(name):
    """Arms and weights from a Unicode name, e.g.
    "BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY" -> {down: light, left: heavy, up: heavy}.

    A weight applies to the directions right before it, or else to the ones
    following it ("LIGHT DOWN AND RIGHT").
    """
    weights = {"LIGHT": "light", "SINGLE": "light", "HEAVY": "heavy", "DOUBLE": "double"}
    directions = {
        "UP": ["up"],
        "DOWN": ["down"],
        "LEFT": ["left"],
        "RIGHT": ["right"],
        "HORIZONTAL": ["left", "right"],
        "VERTICAL": ["up", "down"],
    }
    arms, pending, prefix = {}, [], None
    for word in name.removeprefix("BOX DRAWINGS ").split():
        if word in weights:
            if pending:
                arms.update({d: weights[word] for d in pending})
                pending, prefix = [], None
            else:
                prefix = weights[word]
        elif word in directions:
            if prefix:
                arms.update({d: prefix for d in directions[word]})
            else:
                pending += directions[word]
    assert arms and not pending, name
    return arms


GLYPHS = []
for code in range(0x2500, 0x2580):
    uname = unicodedata.name(chr(code))
    if any(word in uname for word in ("DASH", "ARC", "DIAGONAL")):
        continue
    arms = parse_arms(uname)
    base = DoubleLineBoxGlyph if "double" in arms.values() else LineBoxGlyph
    GLYPHS.append(box_glyph(base, code, arms=arms))


if __name__ == "__main__":
    assert parse_arms("BOX DRAWINGS LIGHT DOWN AND RIGHT") == {"down": "light", "right": "light"}
    assert parse_arms("BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT") == {"left": "light", "right": "heavy"}
    assert parse_arms("BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT") == {
        "up": "heavy", "down": "light", "left": "light", "right": "light"
    }
    assert parse_arms("BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE") == {
        "up": "light", "down": "light", "right": "double"
    }
    assert len(GLYPHS) == 128 - 4 - 12 - 3
    print("ok")
