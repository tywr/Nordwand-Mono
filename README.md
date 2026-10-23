![Nordwand Mono](assets/banner.png)

A compact neo-grotesk font designed for coding.

![Specimen](specimens/specimen.pdf)

## Philosophy

I'm very passionate about the font I am using for my terminal and overall neovim experience, and I couldn't find the "perfect" font. So I decided to design one from scratch using python. This font aims to bring some elements from the all time classic "Univers" font into the proportions of the "JetBrains Mono" font. The name "Nordwand" is a reference to switzerland and its iconic typography – bringing it into the stiff and cold atmosphere of the swiss north faces.

Amongst the inspirations for the design, you might identify:

- Univers from Adrian Frutiger
- SF Pro & SF Mono from Apple
- Alpes Mono from Sharp Type
- Ubuntu Mono from Dalton Maag

## Alternative characters

Some alternative character designs are available to tweak the vibe of the font to your liking. See the [alternative characters document](doc/alternative_characters.md) for a visual comparison and the corresponding OpenType feature tags.

## Stylistic sets

Stylistic sets switch groups of related glyphs at once: `ss02` enables the arrow ligatures and `ss03` uses wide-angled `<`, `>` and arrow heads. See the [stylistic sets document](doc/stylistic_sets.md) for details and how to enable them in common editors and terminals.

## Ligatures

The font includes minimal `->` and `=>` ligatures. Repeated `=`, `-`, `_`, and
`#` characters can use joining forms, allowing their horizontal bars to
connect across runs of any length. These are off by default; enable the `dlig`
feature to turn them on (see the [stylistic sets document](doc/stylistic_sets.md)).

## Nerdwand Mono

Nerdwand Mono is the [Nerd Font](https://www.nerdfonts.com) version of Nordwand Mono, patched with the complete set of icons. Icons are kept to a single cell, so the font stays strictly monospaced. It is not attached to releases; build it locally with `make build` then `make build-nerd-font`. This requires [uv](https://docs.astral.sh/uv/getting-started/installation/) and [fontforge](https://fontforge.org) (`brew install fontforge` on macOS, `fontforge python3-fontforge` on Debian and Ubuntu), and an internet connection on the first run to download the Nerd Fonts patcher. The patched fonts, with the font license and the licenses of the bundled icon sets, are generated inside `./fonts/nerd-font`.

## Compile your own custom version

This font is generated with python. Each glyph is drawn from a python glyph class, in which you can inject a drawing context object. You can for example modify some metrics like the x-height, the capital height etc.

To do so, override the config.example.yml with the values of your liking. Be sure to visualize the individual glyphs with `python -m visualize --config config.yml <glyph_id>`. Then you can geneate the full font with `python -m generate_font --config config.yml`. The font files will be generated inside `./custom-fonts`.

For inspiration, browse the [`./configs`](configs) folder to see the font with other metrics configurations. Each subfolder contains a `config.yml` and a `sample.png` showing a code sample rendered with that configuration. To add your own, create `configs/<name>/config.yml` and run `python -m scripts.config_sample <name>`: it builds the regular weight of the font (or another one with `--weight`) and writes the matching `configs/<name>/sample.png`.

### Adjusting the weight

The stroke weights in the config file set the Regular weight, and every other weight is scaled from them. To choose which weights are exported, or to give a weight its own stroke dimensions, add a `weights` section:

```yaml
weights:
  400:
  425:
    name: Book
    stroke_x: 90 # vertical strokes
    stroke_y: 84 # horizontal strokes
    stroke_alt: 72 # crossbars, like the middle of e
  700:
```

Only the listed weights are built. Strokes you leave out are scaled from the Regular ones as usual, and weights between the standard ones (like 425 here) need a `name`. The [LoDPI configuration](configs/LoDPI/config.yml) uses this to add a heavier Book weight for non-Retina screens. Some terminals can also thicken text on macOS without a custom build, like Ghostty with [`font-thicken`](https://ghostty.org/docs/config/reference#font-thicken).

> [!WARNING]
> There are no guarantees that the font might look good with different metrics, and some glyphs might require some tweaking if the metrics are altered !

## Characters

![characters](assets/samples/sample_char.png)

## Weights

![weights](assets/samples/sample_weights.png)

## Samples

![python](assets/samples/les_drus.png)

### Python

![python](assets/samples/sample_1.png)

### C++

![c++](assets/samples/sample_2.png)

### Haskell

![haskell](assets/samples/sample_3.png)

## Alternative Alphabets

### Cyrillic

![Cyrillic](assets/samples/sample_cyrillic.jpg)
