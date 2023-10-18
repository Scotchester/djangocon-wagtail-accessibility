# Best Practices for Making a Wagtail Website as Accessible as Possible

An online talk for DjangoCon US 2023 by Scott Cranfill


## Video

_[link to be added once it's made public]_


## Slides

The presentation was built using [Podium](https://github.com/beeware/podium) by BeeWare,
a Markdown-based tool for creating slide decks.

- [View PDF export](slides.pdf) (slide content only)
- [View in browser](https://scotchester.github.io/djangocon-wagtail-accessibility/) (slide content only)
  - Navigate the slide deck using the arrow keys
- [View source Markdown](slides.podium/slides.md) (slide content with notes)


## Sample code

I've cloned the [wagtail/bakerydemo](https://github.com/wagtail/bakerydemo) repository
into this repository's bakerydemo folder and applied the following commits,
which make the various changes described in the presentation:

1. Change header tag from `<div>` to `<header>` [6c9c672](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/6c9c672336a298166221611afd6639ebea18d38e)
1. Change listing card heading tag from `<h3>` to `<h2>` [c133814](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/c133814db5294786a225afae373314d3d198f67a)
1. Add StreamBlock heading level validation [3653544](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/3653544018f17f8e682899cf4f2d65f7b464dc81)
1. Add `alt_text` field to `ImageBlock` [dd11f81](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/dd11f81a63ebce9b5d0dbf165b1d174f7bff1a08)
1. Add LinkBlock with aria-label support [33bdd8f](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/33bdd8f1ff784f6c4fa80d3e0ae86121394d1b9b)
1. Add LinkBlock ARIA label validation [76cbc25](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/76cbc251e0e699f973963c5396d169d4405e00ac)
1. Add `help_text` for these scenarios [7b11faa](https://github.com/Scotchester/djangocon-wagtail-accessibility/commit/7b11faa2df40c55340d60f29e3032235ccf32d14)
