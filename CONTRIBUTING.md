# Contributing to Nordwand Mono

Contributions are welcome: new glyphs, fixes to existing shapes, metrics or spacing, and improvements to the tooling. This guide describes how the project is organized and how to submit a change.

## Setup

Requirements: [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
make install     # install the Python dependencies
make build-font  # build TTF, WOFF and WOFF2 into ./fonts
```

## Project layout

| Path | Contents |
| --- | --- |
| `src/config.py` | Font metrics (`FontConfig`) and the per-weight drawing context (`DrawConfig`) |
| `src/glyphs/` | One Python class per glyph, grouped by script and case |
| `src/glyphs/accents/` | Accent marks, also usable as standalone glyphs |
| `src/glyphs/composed/` | Accented letters built from a base glyph and an accent, one file per accent |
| `src/draw/` | Reusable drawing primitives (arches, corners, rectangles, parallelograms, etc.) |
| `src/generate_font.py` | Font builder: discovers the glyphs and writes the font files |
| `src/visualize.py` | Glyph and text previewer |
| `src/scripts/` | Banner, specimen, samples, documentation and website generators |
| `lab/` | Browser page to test the built fonts on sample texts |

## How glyphs work

Each glyph is a subclass of `Glyph` (`src/glyphs/__init__.py`) that defines:

- `name`: a unique slug, e.g. `lowercase_turned_v`, used by the previewer and as the glyph name in the font;
- `unicode`: the code point as a hex string, e.g. `"0x28C"`;
- `draw(self, pen, dc)`: draws the outlines with `pen`, using the metrics and stroke widths of the drawing context `dc`.

Glyphs are discovered automatically: any non-abstract `Glyph` subclass in a module under `src/glyphs/` is included in the font, and no registration is needed. Classes that only serve as building blocks set `generated_only = True`.

Some guidelines:

- **Use the drawing context.** Derive every coordinate from `dc` (`dc.x_height`, `dc.cap`, `dc.stroke_x`, `dc.body_bounds()`, etc.) rather than from fixed values, so the glyph adapts to all weights and to custom configurations.
- **Reuse existing glyphs.** Subclass or transform a related glyph rather than redrawing it. For example, the turned v (`ʌ`) draws the `v` through a flipping pen.
- **Reuse the primitives** in `src/draw/` before writing new curve code.
- **Check every weight and the italic.** The font is built from Thin to Bold, upright and italic, and a shape that works at Regular may break at the extremes.

### Accented letters

Accented letters are `ComposedGlyph` subclasses (`src/glyphs/composed/`) that combine a `base_glyph_class`, an `accent_class` and an `accent_y` anchor height. Add a new letter to the file of its accent, next to the letters that already use it.

Lowercase and uppercase letters use separate accent classes where the sizing differs, e.g. `LowercaseBreveAcute` and `UppercaseBreveAcute`, so each case can be tuned independently. Stacked accents (Vietnamese `ấ`, Pinyin `ǘ`, etc.) are `StackedAccent` subclasses. Their positions and sizes are set by class attributes documented in `src/glyphs/accents/__init__.py`.

Accents on capitals must stay below the top of the cell (`window_ascent`), as terminals clip whatever is drawn above it.

### Alternate characters

Alternate designs set `font_feature`, e.g. `{"cv01": 1}`, and share the `unicode` of the default glyph. Add an `alternative_character_comment` when the alternate needs an explanation; it appears in the [alternative characters](doc/alternative_characters.md) documentation.

## Previewing

Preview a glyph by its slug:

```sh
uv run python -m visualize lowercase_a
```

Useful options:

| Option | Effect |
| --- | --- |
| `-s regular,bold,italic` | Overlay several styles |
| `-c` | Show the Bézier control points |
| `-t "text"` | Render a text string instead of a single glyph |
| `--ref FONT` | Overlay the same character from a reference font |

Run `uv run python -m visualize --help` for the full list.

To test the built fonts in context, build them and open the lab:

```sh
make build-font
make lab         # serves http://localhost:8001/lab/
```

When you add glyphs, add them to the matching sample in `lab/index.html` as well.

## Submitting a change

1. Fork the repository and create a branch from `main`.
2. Make the change, then check it in the previewer at several weights and in italic, and build the fonts with `make build-font` to make sure the build passes.
3. Keep each commit focused on one change. Commit messages start with a short type prefix, for example:
   - `add: latin iota and upsilon`
   - `fix: overflow of uppercase stacked accents`
   - `refactor: cyrillic descender glyphs`
4. Open a pull request that describes the change. For visual changes, include before and after screenshots from the previewer or the lab.

## License

By contributing, you agree that your contributions are licensed under the project licenses: the [SIL Open Font License 1.1](LICENSE-FONT.txt) for the font, and the [MIT License](LICENSE.txt) for the source code.
