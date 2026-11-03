"""The topo figure: the bold lowercase a filled with mountain terrain, like a
massif cut out of a topographic map, from the built font, so the outline
follows every change to the glyph.

The terrain is a height map: a few broad summits standing on the glyph,
with ridged fractal noise over them for crests and valleys, seeded so it
never changes between builds. Its contour lines are
traced with contourpy and clipped to the glyph, every fifth one heavier like
an index contour.
"""

import contourpy
import numpy as np
import pathops
from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

SCALE = 1.4
BASELINE = 880  # svg y of the baseline
CENTER = 950  # svg x of the middle of the a's cell
RESOLUTION = 3  # Font units between the height map's samples
LEVELS = 22  # Contour lines from the lowest to the highest point
INDEX = 5  # Every fifth contour is an index contour, drawn heavier
SEED = 4478
SUMMITS = 5  # Broad peaks placed on the glyph
RIDGES = 0.35  # Weight of the ridged noise against the summits


def outline(font, char):
    """The glyph as one overlap-free path, in font units."""
    glyph = font.getGlyphSet()[font.getBestCmap()[ord(char)]]
    path = pathops.Path()
    glyph.draw(path.getPen())
    path.simplify()
    return path


def grow(path, d):
    """The path grown by `d` font units."""
    band = pathops.Path(path)
    band.stroke(2 * d, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
    band.convertConicsToQuads()
    return pathops.op(path, band, pathops.PathOp.UNION)


def to_svg(x, y):
    return CENTER + SCALE * (x - 300), BASELINE - SCALE * y


def svg_path(path):
    """Path data in svg units."""
    pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    path.draw(TransformPen(pen, Transform(SCALE, 0, 0, -SCALE, CENTER - 300 * SCALE, BASELINE)))
    return pen.getCommands()


def value_noise(lattice, u, v):
    """Smooth noise at the lattice coordinates (u, v), from a random lattice."""
    i, j = np.floor(u).astype(int), np.floor(v).astype(int)
    fu, fv = u - i, v - j
    fu, fv = fu * fu * (3 - 2 * fu), fv * fv * (3 - 2 * fv)  # Smoothstep
    n = len(lattice)
    i, j = i % n, j % n
    i1, j1 = (i + 1) % n, (j + 1) % n
    top = lattice[j, i] * (1 - fu) + lattice[j, i1] * fu
    bottom = lattice[j1, i] * (1 - fu) + lattice[j1, i1] * fu
    return top * (1 - fv) + bottom * fv


def terrain(a, xs, ys):
    """A few summits inside the glyph, with ridged noise over them for crests
    and valleys. Each noise octave is turned, so no grid direction shows."""
    rng = np.random.default_rng(SEED)
    x, y = np.meshgrid(xs, ys)
    size = max(np.ptp(xs), np.ptp(ys))
    height = np.zeros_like(x)

    # Summits: broad peaks, only where they stand on the glyph
    x1, y1, x2, y2 = a.bounds
    placed = 0
    while placed < SUMMITS:
        px, py = rng.uniform(x1, x2), rng.uniform(y1, y2)
        if not a.contains((px, py)):
            continue
        sigma = rng.uniform(0.12, 0.22) * size
        height += rng.uniform(0.6, 1) * np.exp(-((x - px) ** 2 + (y - py) ** 2) / (2 * sigma**2))
        placed += 1

    # Ridges
    for octave in range(4):
        lattice = rng.random((64, 64))
        angle = rng.uniform(0, np.pi)
        freq = 2.5 * 2**octave / size
        u = (x * np.cos(angle) - y * np.sin(angle)) * freq + rng.uniform(0, 64)
        v = (x * np.sin(angle) + y * np.cos(angle)) * freq + rng.uniform(0, 64)
        ridge = (1 - np.abs(2 * value_noise(lattice, u, v) - 1)) ** 2
        height += RIDGES * 0.5**octave * ridge
    return height


def topo(font):
    """The figure's drawing, everything inside its <svg>."""
    a = outline(font, "a")
    x1, y1, x2, y2 = a.bounds
    xs = np.arange(x1 - 12, x2 + 12, RESOLUTION)
    ys = np.arange(y1 - 12, y2 + 12, RESOLUTION)
    height = terrain(a, xs, ys)
    # A light blur rounds off the kinks the noise lattice leaves in the lines
    kernel = np.exp(-np.linspace(-2, 2, 9) ** 2)
    kernel /= kernel.sum()
    for axis in (0, 1):
        height = np.apply_along_axis(np.convolve, axis, height, kernel, mode="same")

    # Trace only over the glyph (and a little past it, for the clip to cut)
    margin = grow(a, 2 * RESOLUTION)
    inside = np.array([[margin.contains((x, y)) for x in xs] for y in ys])
    heights = np.ma.masked_where(~inside, height)
    lines = contourpy.contour_generator(xs, ys, heights, line_type="Separate")
    lo, hi = heights.min(), heights.max()

    parts = [
        f'<defs><clipPath id="glyph-clip"><path clip-rule="evenodd" d="{svg_path(a)}"/></clipPath></defs>',
        f'<path class="ice" fill-rule="evenodd" d="{svg_path(a)}"/>',
        '<g clip-path="url(#glyph-clip)">',
    ]
    for k in range(1, LEVELS):
        d = " ".join(
            "M" + " L".join(f"{sx:.0f} {sy:.0f}" for sx, sy in (to_svg(x, y) for x, y in line))
            for line in lines.lines(lo + (hi - lo) * k / LEVELS)
        )
        if d:
            cls = "contour index" if k % INDEX == 0 else "contour"
            parts.append(f'<path class="{cls}" d="{d}"/>')
    parts += ["</g>", f'<path class="glyph" fill-rule="evenodd" d="{svg_path(a)}"/>']
    return "\n        ".join(parts)
