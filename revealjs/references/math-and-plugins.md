# Math & Plugins Reference

## Math Plugin

Render LaTeX formulas using KaTeX or MathJax. Register the appropriate variant.

### KaTeX (recommended)

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/math/math.js"></script>
<script>
  Reveal.initialize({ plugins: [RevealMath.KaTeX] });
</script>
```

CDN URL for the plugin: `https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/math/math.js`

Usage in slides:

```html
<section>
  <h2>The Lorenz Equations</h2>
  \[\begin{aligned}
    \dot{x} &amp; = \sigma(y-x) \\
    \dot{y} &amp; = \rho x - y - xz \\
    \dot{z} &amp; = -\beta z + xy
  \end{aligned} \]
</section>
```

In Markdown slides, wrap with `$$`:

```html
<section data-markdown>$$ J(\theta_0,\theta_1) = \sum_{i=0} $$</section>
```

### KaTeX Configuration

```js
Reveal.initialize({
  katex: {
    version: 'latest',
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '$', right: '$', display: false },
      { left: '\\(', right: '\\)', display: false },
      { left: '\\[', right: '\\]', display: true },
    ],
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
  },
  plugins: [RevealMath.KaTeX],
});
```

For offline KaTeX:

```js
katex: { local: 'node_modules/katex' }
```

### MathJax Variants

| Library | Plugin | Config Key |
|:--|:--|:--|
| KaTeX | `RevealMath.KaTeX` | `katex` |
| MathJax 2 | `RevealMath.MathJax2` | `mathjax2` |
| MathJax 3 | `RevealMath.MathJax3` | `mathjax3` |
| MathJax 4 | `RevealMath.MathJax4` | `mathjax4` |

MathJax 3 example:

```js
Reveal.initialize({
  mathjax3: {
    mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    },
  },
  plugins: [RevealMath.MathJax3],
});
```

---

## Built-in Plugins Summary

| Plugin | Global Name | Script Path | Purpose |
|:--|:--|:--|:--|
| Highlight | `RevealHighlight` | `plugin/highlight/highlight.js` | Syntax-highlighted code |
| Markdown | `RevealMarkdown` | `plugin/markdown/markdown.js` | Markdown-authored slides |
| Notes | `RevealNotes` | `plugin/notes/notes.js` | Speaker view (S key) |
| Math | `RevealMath` | `plugin/math/math.js` | LaTeX math rendering |
| Search | `RevealSearch` | `plugin/search/search.js` | Search content (Ctrl+Shift+F) |
| Zoom | `RevealZoom` | `plugin/zoom/zoom.js` | Alt+click zoom |

All available as ES modules with `.mjs` extension.

### Plugin API

```js
Reveal.hasPlugin('markdown');    // true/false
Reveal.getPlugin('markdown');    // { id, init, ... }
Reveal.getPlugins();             // all registered plugins
```

---

## Creating Custom Plugins

A plugin is an object with `id`, optional `init(deck)`, and optional `destroy()`:

```js
// toaster.js
export default () => ({
  id: 'toaster',
  init: (deck) => {
    deck.addKeyBinding({ keyCode: 84, key: 'T' }, () => {
      deck.shuffle();
      console.log('🍻');
    });
  },
});
```

Register in config:

```js
import Toaster from 'toaster.js';
Reveal.initialize({ plugins: [Toaster] });
```

### Async Plugins

Return a Promise from `init` to delay reveal.js initialization:

```js
let WaitForIt = {
  id: 'wait-for-it',
  init: (deck) => new Promise((resolve) => setTimeout(resolve, 3000)),
};
```