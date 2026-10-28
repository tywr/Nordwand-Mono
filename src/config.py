import dataclasses
from dataclasses import dataclass
from utils.bounds import BodyBounds


@dataclass
class FontConfig:
    """Default metrics used for the project, can be overwritten with a yaml file"""

    family_name: str = "Nordwand Mono"
    font_revision: float = 1.0

    units_per_em: int = 1000
    window_ascent: int = 1025
    window_descent: int = -300
    window_width: int = 600

    ascent: int = 750
    descent: int = -185
    cap: int = 710
    x_height: int = 540

    accent: int = 715
    accent_cap: int = 890

    math: int = 300

    parenthesis: int = 300
    parenthesis_length: int = 1060

    min_margin_lowercase: int = 26
    min_margin_uppercase: int = 38

    italic_angle: float = 9.4

    width: int = 360

    hx: int = 180
    hy: int = 240

    cap_hx: int = 180
    cap_hy: int = 250

    taper: float = 0.35

    default_stroke = 84
    stroke_x: int = 84
    stroke_y: int = 70
    stroke_alt: int = 66

    v_overshoot: int = 9
    v_overshoot_cap: int = 16
    h_overshoot: int = 10

    # Weights to export, as weight -> {name, stroke_x, stroke_y, stroke_alt}.
    # Every key is optional; strokes left out follow DrawConfig.weight().
    weights = {w: {} for w in (100, 200, 300, 375, 400, 425, 500, 600, 700)}


# Standard names, used when a weight in the config doesn't set its own.
WEIGHT_NAMES = {
    100: "Thin",
    200: "ExtraLight",
    300: "Light",
    350: "SemiLight",
    375: "Book",
    400: "Regular",
    450: "Retina",
    500: "Medium",
    600: "SemiBold",
    700: "Bold",
    800: "ExtraBold",
    900: "Black",
}

WEIGHT_KEYS = {"name", "stroke_x", "stroke_y", "stroke_alt"}


def weight_name(w):
    """Style name of weight `w`: its config `name`, else the standard one."""
    name = FontConfig.weights.get(w, {}).get("name") or WEIGHT_NAMES.get(w)
    if name is None:
        raise ValueError(f"Weight {w} needs a `name` in the config")
    return name


@dataclass
class DrawConfig(FontConfig):
    # Can be overwritten for bold / thinner fonts
    x_height: int = FontConfig.x_height
    cap: int = FontConfig.cap
    ascent: int = FontConfig.ascent
    descent: int = FontConfig.descent
    accent: int = FontConfig.accent
    accent_cap: int = FontConfig.accent_cap
    width: int = FontConfig.width
    hx: int = FontConfig.hx
    hy: int = FontConfig.hy
    cap_hx: int = FontConfig.cap_hx
    cap_hy: int = FontConfig.cap_hy
    taper: int = FontConfig.taper
    stroke_x: int = FontConfig.stroke_x
    stroke_y: int = FontConfig.stroke_y
    stroke_alt: int = FontConfig.stroke_alt
    v_overshoot: int = FontConfig.v_overshoot
    h_overshoot: int = FontConfig.h_overshoot

    italic: bool = False

    @classmethod
    def weight(cls, w=400):
        """Return a DrawConfig with heavier stroke weights for a bold variant.

        Each metric is tabulated at the weights in `ws`; weights in between
        are linearly interpolated.
        """
        from bisect import bisect_right

        ws = [100, 200, 300, 375, 400, 425, 500, 600, 700]
        # Multipliers of the 400 values
        ratio_x = [0.625, 0.731, 0.855, 0.962, 1, 1.04, 1.17, 1.368, 1.6]
        ratio_y = [0.667, 0.763, 0.874, 0.967, 1, 1.034, 1.145, 1.31, 1.5]
        ratio_alt = [0.833, 0.886, 0.941, 0.985, 1, 1.015, 1.063, 1.129, 1.2]
        ratio_hx = [0.909, 0.938, 0.969, 0.992, 1, 1.008, 1.032, 1.066, 1.1]
        ratio_hy = [1.0, 1.0, 1.0, 1.0, 1, 1.0, 1.0, 1.0, 1.0]
        # Absolute values
        tapers = [0.5, 0.5, 0.5, 0.5, 0.5, 0.479, 0.415, 0.33, 0.245]

        def at(values):
            i = min(max(bisect_right(ws, w), 1), len(ws) - 1)
            t = min(max((w - ws[i - 1]) / (ws[i] - ws[i - 1]), 0), 1)
            return values[i - 1] + t * (values[i] - values[i - 1])

        ratio_x, ratio_y, ratio_alt = at(ratio_x), at(ratio_y), at(ratio_alt)
        hx_ratio, hy_ratio = at(ratio_hx), at(ratio_hy)
        taper = at(tapers)

        return cls(
            stroke_x=int(cls.stroke_x * ratio_x),
            stroke_y=int(cls.stroke_y * ratio_y),
            stroke_alt=int(cls.stroke_alt * ratio_alt),
            x_height=cls.x_height,
            cap=cls.cap,
            accent=cls.cap,
            accent_cap=cls.accent_cap,
            ascent=cls.ascent,
            descent=cls.descent,
            taper=taper,
            hy=hy_ratio * cls.hy,
            hx=hx_ratio * cls.hx,
            cap_hy=hy_ratio * cls.cap_hy,
        )

    @classmethod
    def for_weight(cls, w=400, italic=False):
        """Return the DrawConfig of weight `w`, with its config stroke overrides."""
        if w != 400:
            dc = cls.weight(w=w)
        elif italic:
            dc = cls.for_italic()
        else:
            dc = cls()
        for key, value in FontConfig.weights.get(w, {}).items():
            if key != "name":
                setattr(dc, key, value)
        dc.italic = italic
        return dc

    @classmethod
    def for_italic(cls):
        return cls(
            stroke_x=int(cls.stroke_x),
            stroke_y=int(cls.stroke_y),
            stroke_alt=int(cls.stroke_alt),
            taper=cls.taper,
            italic=True,
        )

    def body_bounds(
        self,
        offset: int,
        width_ratio=1,
        height="x_height",
        overshoot_left=False,
        overshoot_right=False,
        overshoot_top=False,
        overshoot_bottom=False,
        number=False,
        uppercase=False,
        min_margin=None,
    ):
        """
        Abstraction for storing common metrics relative to the body
        of a character. For most lowercase, the boundaries are
        a centered rectangle of length `width` and of height `x-height`.
        For most capital letters, it's a centered rectangle of length
        `width` and height `ascent`.
        """
        width = self.width * width_ratio
        if height not in ["x_height", "ascent", "cap"]:
            raise ValueError(f"Value {height} should be `x_height`, `ascent` or `cap`")
        x1 = self.window_width / 2 - width / 2 - self.stroke_x / 2 + offset
        y1 = 0
        x2 = self.window_width / 2 + width / 2 + self.stroke_x / 2 + offset
        y2 = getattr(self, height)

        # For some wide characters (w, m, W, M) we fix a minimum margin
        # for bolder weights
        if min_margin:
            x1 = max(min_margin, x1)
            x2 = min(self.window_width - min_margin, x2)

        if uppercase or number:
            v_ov = self.v_overshoot_cap
        else:
            v_ov = self.v_overshoot
        h_ov = self.h_overshoot

        if overshoot_left:
            x1 -= h_ov / 2
            x2 += h_ov / 2
        if overshoot_right:
            x1 -= h_ov / 2
            x2 += h_ov / 2

        if overshoot_bottom:
            y1 -= v_ov
        if overshoot_top:
            y2 += v_ov

        # Rescale the hx and hy for the new box
        if uppercase or number:
            hx = self.cap_hx
            hy = self.cap_hy
        else:
            hx = self.hx
            hy = self.hy

        hx = hx * (x2 - x1 - self.stroke_x) / self.width
        hy = hy * (y2 - y1 - self.stroke_y) / self.x_height

        return BodyBounds(
            x1=x1, y1=y1, x2=x2, y2=y2, hx=hx, hy=hy, v_ov=v_ov, h_ov=h_ov
        )


def config_keys():
    """Names of all overridable configuration values."""
    keys = {f.name for f in dataclasses.fields(DrawConfig)}
    # `default_stroke` and `weights` are plain class attributes, not fields.
    keys.update({"default_stroke", "weights"})
    return keys


def parse_weights(value):
    """Normalise the `weights` config value to {weight: {key: value}}.

    Accepts a list of weights (`[400, 425, 700]`) or a mapping of weight to
    its settings (`{425: {name: Book, stroke_y: 84}}`, `{700: null}`).
    """
    if isinstance(value, list):
        value = {w: {} for w in value}
    if not isinstance(value, dict) or not value:
        raise ValueError("`weights` must be a non-empty list or mapping of weights")

    weights = {}
    for w, settings in value.items():
        if not isinstance(w, int) or not 1 <= w <= 1000:
            raise ValueError(f"Weight {w!r} must be an integer from 1 to 1000")
        settings = settings or {}
        unknown = set(settings) - WEIGHT_KEYS
        if unknown:
            raise ValueError(
                f"Unknown keys for weight {w}: {sorted(unknown)}. "
                f"Valid keys: {sorted(WEIGHT_KEYS)}"
            )
        if "name" not in settings and w not in WEIGHT_NAMES:
            raise ValueError(f"Weight {w} needs a `name` in the config")
        weights[w] = dict(settings)
    return dict(sorted(weights.items()))


def apply_config_overrides(overrides):
    """Overwrite the default FontConfig / DrawConfig values in place.

    `overrides` is a mapping of config name -> value. The values are written
    onto both classes so that:
      * static access (`fc.window_width`, `fc.accent`, ...) sees them, and
      * instantiation (`DrawConfig()`, `.weight()`, `.for_italic()`) sees them,
        which requires rebuilding the dataclass `__init__` defaults.

    Raises ValueError on unknown keys so typos fail loudly.
    """
    valid = config_keys()
    unknown = set(overrides) - valid
    if unknown:
        raise ValueError(
            f"Unknown config keys: {sorted(unknown)}. Valid keys: {sorted(valid)}"
        )

    if "weights" in overrides:
        overrides = {**overrides, "weights": parse_weights(overrides["weights"])}

    for key, value in overrides.items():
        for cls in (FontConfig, DrawConfig):
            if hasattr(cls, key):
                setattr(cls, key, value)

    # Reassigning a class attribute does not change the dataclass `__init__`
    # default (which is baked in at class creation), so rebuild it from the
    # current class attributes, in field order.
    DrawConfig.__init__.__defaults__ = tuple(
        getattr(DrawConfig, f.name) for f in dataclasses.fields(DrawConfig)
    )

    return overrides


def load_config(path):
    """Load a YAML file and apply it as overrides to the font configuration.

    Returns the dict of applied overrides.
    """
    import yaml

    with open(path) as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(
            f"Config file {path!r} must contain a top-level mapping of "
            f"config name -> value"
        )
    return apply_config_overrides(data)
