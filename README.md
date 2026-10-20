![Nordwand Mono](assets/banner.png)

A compact neo-grotesk font designed for coding.

> [!NOTE]
> This is a fork of [tywr/Nordwand-Mono](https://github.com/tywr/Nordwand-Mono) by Tanguy Vivier, patched with [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) icons (OS logos, Powerline, devicons, Font Awesome, Octicons, Material Design, …) for use in terminals. All credit for the font design goes to the original author.

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

## Nerd Font

Each release includes `NordwandMono-NerdFont.zip`, containing every weight patched with the complete Nerd Fonts glyph set. The family is named **NordwandMono Nerd Font Mono**, and icons are constrained to a single cell so the terminal grid stays intact.

To build it locally (requires [FontForge](https://fontforge.org), e.g. `brew install fontforge`):

```sh
make build-nerd        # patched fonts are written to ./fonts/nerd
make install-nerd-mac  # copy them to ~/Library/Fonts
```

## Compile your own custom version

This font is generated with python. Each glyph is drawn from a python glyph class, in which you can inject a drawing context object. You can for example modify some metrics like the x-height, the capital height etc.

To do so, override the config.example.yml with the values of your liking. Be sure to visualize the individual glyphs with `python -m visualize --config config.yml <glyph_id>`. Then you can geneate the full font with `python -m generate_font --config config.yml`. The font files will be generated inside `./custom-fonts`.

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
