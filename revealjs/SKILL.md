---
name: revealjs
description: >
  Create reveal.js HTML presentations as single-file artifacts. Use this skill whenever the user asks to create a presentation, slide deck, or slides using reveal.js — or when they mention "reveal.js", "revealjs", or want an HTML-based presentation (as opposed to PowerPoint/PPTX). Also trigger when the user wants to convert content (outlines, markdown notes, topics) into a reveal.js deck, or asks to edit/improve an existing reveal.js presentation. This skill covers the full reveal.js feature set: slides, vertical slides, fragments, auto-animate, code highlighting, markdown slides, math (KaTeX/MathJax), backgrounds (color, gradient, image, video, iframe), themes, transitions, speaker notes, layout helpers, lightbox, scroll view, PDF export, the React wrapper (@revealjs/react), and plugin creation. If the user mentions any of these features in the context of presentations, use this skill.
---

# reveal.js Presentation Skill

This skill generates reveal.js presentations as **single-file HTML artifacts**. The output is a self-contained `.html` file that loads reveal.js and plugins from CDN, so it works by opening the file in any browser — no build step needed.

## When to Read Reference Files

Before generating a presentation, scan the user's request for advanced features. If any of the following are needed, read the corresponding reference file from `references/` for detailed syntax and examples:

| Feature requested | Reference file |
|:--|:--|
| Auto-Animate between slides | `references/auto-animate.md` |
| Code blocks with line highlights, step-by-step highlights | `references/code-and-markdown.md` |
| Math equations (KaTeX, MathJax) | `references/math-and-plugins.md` |
| React wrapper (`@revealjs/react`) | `references/react.md` |
| Scroll view, PDF export, speaker view | `references/advanced-features.md` |
| Custom plugins, creating plugins | `references/math-and-plugins.md` |
| Lightbox (image/video/iframe preview) | `references/advanced-features.md` |

For standard presentations (slides, fragments, backgrounds, transitions, themes, speaker notes), all the information you need is in this file.

---

## Output Format

Generate a single HTML file. The structure is always:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>[Presentation Title]</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/[THEME].css" />
    <!-- Plugin CSS if needed (e.g. highlight theme) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css" />
    <style>
      /* Custom styles go here */
    </style>
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
        <section><!-- Slide 1 --></section>
        <section><!-- Slide 2 --></section>
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
    <!-- Plugin scripts -->
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
    <script>
      Reveal.initialize({
        hash: true,
        plugins: [RevealHighlight, RevealMarkdown, RevealNotes],
        // Additional config options
      });
    </script>
  </body>
</html>
```

### CDN URLs

Always use the jsDelivr CDN with `reveal.js@5` (the latest stable major version):

- Core: `https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js`
- Core CSS: `https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css`
- Themes: `https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/[name].css`
- Plugins: `https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/[name]/[name].js`
- Highlight themes: `https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css`

---

## Slides

Each `<section>` is one slide. Nest `<section>` elements for vertical slides:

```html
<!-- Horizontal slide -->
<section><h1>Title</h1></section>

<!-- Vertical stack -->
<section>
  <section><h2>Vertical 1</h2></section>
  <section><h2>Vertical 2</h2></section>
</section>
```

The hierarchy is always: `.reveal > .slides > section`.

---

## Themes

Available built-in themes: `black` (default), `white`, `league`, `beige`, `night`, `serif`, `simple`, `solarized`, `moon`, `dracula`, `sky`, `blood`.

Choose the theme based on context — for technical talks `dracula` or `moon` work well; for corporate presentations `white` or `simple`; for creative decks `blood` or `league`.

---

## Fragments

Fragments reveal content step by step within a slide. Add the `fragment` class:

```html
<p class="fragment">Fades in (default)</p>
<p class="fragment fade-up">Slides up</p>
<p class="fragment highlight-red">Turns red</p>
```

Available fragment styles: `fade-out`, `fade-up`, `fade-down`, `fade-left`, `fade-right`, `fade-in-then-out`, `current-visible`, `fade-in-then-semi-out`, `grow`, `semi-fade-out`, `shrink`, `strike`, `highlight-red`, `highlight-green`, `highlight-blue`, `highlight-current-red`, `highlight-current-green`, `highlight-current-blue`.

Control the order with `data-fragment-index`:

```html
<p class="fragment" data-fragment-index="3">Last</p>
<p class="fragment" data-fragment-index="1">First</p>
<p class="fragment" data-fragment-index="2">Second</p>
```

Nest fragments for multi-step effects on the same element:

```html
<span class="fragment fade-in">
  <span class="fragment highlight-red">
    <span class="fragment fade-out">Fade in → Red → Fade out</span>
  </span>
</span>
```

Custom fragments (since 4.5.0) — define `.fragment.effectname` and `.fragment.effectname.visible` CSS, and add the `custom` class:

```html
<style>
  .fragment.blur { filter: blur(5px); }
  .fragment.blur.visible { filter: none; }
</style>
<p class="fragment custom blur">Blurred until stepped</p>
```

---

## Backgrounds

Apply full-page backgrounds to individual slides using `data-background-*` attributes:

```html
<!-- Color -->
<section data-background-color="aquamarine">...</section>

<!-- Gradient -->
<section data-background-gradient="linear-gradient(to bottom, #283b95, #17b2c3)">...</section>

<!-- Image -->
<section data-background-image="https://example.com/bg.jpg"
         data-background-size="cover"
         data-background-position="center"
         data-background-opacity="0.5">...</section>

<!-- Video -->
<section data-background-video="video.mp4"
         data-background-video-loop
         data-background-video-muted>...</section>

<!-- Iframe -->
<section data-background-iframe="https://example.com"
         data-background-interactive>...</section>
```

### Parallax Background

Set globally in config:

```js
Reveal.initialize({
  parallaxBackgroundImage: 'https://example.com/bg.jpg',
  parallaxBackgroundSize: '2100px 900px',
  parallaxBackgroundHorizontal: 200,
  parallaxBackgroundVertical: 50,
});
```

---

## Transitions

Set globally or per-slide. Styles: `none`, `fade`, `slide` (default), `convex`, `concave`, `zoom`.

```html
<!-- Per-slide -->
<section data-transition="zoom">Zoom in!</section>
<section data-transition-speed="fast">Fast transition</section>

<!-- Separate in/out -->
<section data-transition="slide-in fade-out">Mixed</section>
```

Global config:

```js
Reveal.initialize({
  transition: 'slide',
  transitionSpeed: 'default', // default | fast | slow
  backgroundTransition: 'fade',
});
```

---

## Speaker Notes

Add notes inside an `<aside class="notes">` element, or use the `data-notes` attribute:

```html
<section>
  <h2>My Slide</h2>
  <aside class="notes">
    Speaker notes here — press S to open speaker view.
  </aside>
</section>

<!-- Or inline -->
<section data-notes="Quick note for this slide">
  <h2>Another Slide</h2>
</section>
```

The Notes plugin must be registered (`RevealNotes`). Speaker view opens with the `S` key.

---

## Layout Helpers

- **`r-stack`**: Stack elements on top of each other (use with fragments for incremental reveal).
- **`r-fit-text`**: Auto-size text to fill the slide width.
- **`r-stretch`**: Make one element fill remaining vertical space.
- **`r-frame`**: Add a border frame around an element.
- **`r-hstack`** / **`r-vstack`**: Horizontal/vertical flex layouts.

```html
<h2 class="r-fit-text">BIG TEXT</h2>

<div class="r-stack">
  <img class="fragment" src="img1.jpg" width="450" height="300" />
  <img class="fragment" src="img2.jpg" width="300" height="450" />
</div>
```

---

## Slide States

Set `data-state` on a section to apply a CSS class to the viewport when that slide is active:

```html
<section data-state="make-it-pop">...</section>
```

```css
.make-it-pop { filter: drop-shadow(0 0 10px purple); }
```

---

## Media

- **Autoplay**: add `data-autoplay` to `<video>` or `<audio>`.
- **Lazy loading**: use `data-src` instead of `src` for images, video, audio, iframes.
- **Iframes**: Use `data-background-iframe` for full-page, or inline `<iframe>` for in-slide.

---

## Key Configuration Options

```js
Reveal.initialize({
  controls: true,           // Show navigation arrows
  progress: true,           // Show progress bar
  center: true,             // Vertically center slides
  hash: true,               // Update URL hash on slide change
  slideNumber: false,       // Show slide numbers (true, 'c/t', 'h.v', etc.)
  transition: 'slide',      // none | fade | slide | convex | concave | zoom
  width: 960,               // Presentation width
  height: 700,              // Presentation height
  margin: 0.04,             // Content margin
  autoSlide: 0,             // Auto-advance interval in ms (0 = disabled)
  loop: false,              // Loop the presentation
  mouseWheel: false,        // Navigate via mouse wheel
  fragments: true,          // Enable fragments
  embedded: false,          // Embedded mode (size from container)
  touch: true,              // Touch navigation
  previewLinks: false,      // Open links in iframe overlay
  view: 'default',          // 'default' | 'scroll'
});
```

---

## Built-in Plugins

| Plugin | Global Name | Purpose |
|:--|:--|:--|
| `plugin/highlight/highlight.js` | `RevealHighlight` | Syntax highlighting for `<code>` blocks |
| `plugin/markdown/markdown.js` | `RevealMarkdown` | Write slides in Markdown |
| `plugin/notes/notes.js` | `RevealNotes` | Speaker notes (press S) |
| `plugin/math/math.js` | `RevealMath` | Render LaTeX math (KaTeX/MathJax) |
| `plugin/search/search.js` | `RevealSearch` | Search slide content (Ctrl+Shift+F) |
| `plugin/zoom/zoom.js` | `RevealZoom` | Alt+click to zoom into elements |

Always include `RevealHighlight` and `RevealNotes` by default. Add others as needed.

---

## Best Practices for Generated Presentations

1. **One idea per slide.** Keep slides focused — if content overflows, split it.
2. **Use fragments for progressive disclosure.** Don't dump everything at once.
3. **Choose appropriate backgrounds.** Dark themes pair well with gradient or dark color backgrounds.
4. **Add speaker notes** for every content slide so the presenter has talking points.
5. **Use `r-fit-text`** for title slides and big statements.
6. **Use code highlighting** for technical talks — always include the highlight plugin and a highlight theme CSS.
7. **Keep custom CSS minimal.** Leverage built-in classes and themes.
8. **Set `hash: true`** so the URL reflects the current slide (useful for sharing).
9. **Use vertical slides** to group related subtopics under a main topic.
10. **Test the output.** The generated HTML should work by opening it directly in a browser.

---

## Auto-Slide

For kiosk-mode or timed presentations:

```js
Reveal.initialize({
  autoSlide: 5000, // advance every 5 seconds
  loop: true,
});
```

Override per-slide with `data-autoslide="2000"` or per-fragment.

---

## Presentation Size

```js
Reveal.initialize({
  width: 960,
  height: 700,
  margin: 0.04,
  minScale: 0.2,
  maxScale: 2.0,
});
```

Use `disableLayout: true` to bring your own CSS layout.

---

## PDF Export

Instruct users to: append `?print-pdf` to the URL, then Ctrl+P → Save as PDF (Chrome/Chromium only). Set landscape, no margins, enable background graphics.

---

## API (for interactive slides)

The `Reveal` object is available globally after initialization:

```js
Reveal.slide(2);          // Go to slide 3 (0-indexed)
Reveal.next();             // Next slide
Reveal.prev();             // Previous slide
Reveal.getTotalSlides();   // Total slide count
Reveal.getProgress();      // 0..1
Reveal.on('slidechanged', (e) => { /* e.currentSlide */ });
```