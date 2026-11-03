# Stylistic Sets and Optional Ligatures

These OpenType features switch a group of related glyphs at once. They are off
by default and can be turned on independently.

| Feature | Affects | Effect |
| --- | --- | --- |
| `ss01` | `l` `m` | Uses the standard constructions of the `l` and the `m` |
| `ss02` | `->` `=>` | Turns on the arrow ligatures, even where standard ligatures (`liga`) are disabled |
| `ss03` | `<` `>` `->` `=>` | Uses a wide angle for the comparison signs and the arrow heads |
| `dlig` | `=` `-` `_` `#` | Joins the horizontal bars of repeated characters |

## `ss01` — classic flavour

For those who prefer more conventional letterforms, `ss01` switches the `l`
and the `m` to their standard constructions in one go. It is equivalent to
`cv03=1` and `cv12=1`. In the italic, only the `m` changes; the `l` keeps its
italic design so the two styles stay easy to tell apart.

| Character | Default | `ss01` |
| --- | --- | --- |
| `l` | ![lowercase_l](alternative_characters/lowercase_l.png) | ![lowercase_l_2](alternative_characters/lowercase_l_2.png) |
| `m` | ![lowercase_m](alternative_characters/lowercase_m.png) | ![lowercase_m_2](alternative_characters/lowercase_m_2.png) |

To get the classic `l` in the italic as well, use `cv03=2` together with
`cv12=1` instead.

## `ss02` — arrow ligatures

`->` and `=>` are drawn as single arrows spanning two cells. They belong to
both the standard ligatures (`liga`, on by default) and `ss02`. Many editors
and terminals turn off `liga` for code; enabling `ss02` brings the arrows back
without enabling any other ligature.

## `ss03` — wide comparison signs and arrows

By default, `<` and `>` use a narrow angle, close to most coding fonts. `ss03`
switches them to a taller, wider-angled design, and gives the `->` and `=>`
ligatures the matching arrow head.

| Character | Default | `ss03` |
| --- | --- | --- |
| `<` | ![less_than_sign](alternative_characters/less_than_sign.png) | ![less_than_sign_2](alternative_characters/less_than_sign_2.png) |
| `>` | ![greater_than_sign](alternative_characters/greater_than_sign.png) | ![greater_than_sign_2](alternative_characters/greater_than_sign_2.png) |

`ss03` works together with `ss02`: with both on, the arrows use the wide head.

## `dlig` — joined repeated characters

`dlig` (discretionary ligatures) joins runs of two or more `=`, `-`, `_` or
`#` into a continuous line, e.g. for `====`, `----` or `____` separators. The
run can be any length and every character keeps its own cell, so alignment and
cursor movement are unaffected. Mixed runs such as `=-` are not joined.

## Enabling a feature

CSS:

```css
code {
  font-family: "Nordwand Mono";
  font-feature-settings: "ss02", "ss03", "dlig";
}
```

kitty (`kitty.conf`), once per style you use, with the PostScript names listed
by `kitty +list-fonts --psnames`:

```
font_features <PostScript name> +ss02 +ss03 +dlig
```

Ghostty:

```
font-feature = ss02
font-feature = ss03
font-feature = dlig
```

WezTerm:

```lua
config.harfbuzz_features = { "ss02", "ss03", "dlig" }
```

The same mechanism enables the character variants listed in the
[alternative characters document](alternative_characters.md), e.g. `cv01` for
the slashed zero.
