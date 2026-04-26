# Advanced Features Reference

## Scroll View (5.0.0+)

Display any presentation as a scrollable page. All animations, fragments, and features work.

### Activation

```js
Reveal.initialize({
  view: 'scroll',
  scrollProgress: true, // 'auto' | true | false
});
```

Or via URL: append `?view=scroll` to the query string.

### Automatic Activation on Mobile

Enabled by default at mobile viewport widths via `scrollActivationWidth`. Disable with:

```js
Reveal.initialize({ scrollActivationWidth: null });
```

### Scrollbar

Custom scrollbar broken up by slides, shows fragment positions. Configure visibility:

```js
scrollProgress: 'auto' // auto (show while scrolling) | true (always) | false (never)
```

### Scroll Snapping

```js
scrollSnap: 'mandatory' // mandatory (default) | proximity | false
```

### Scroll Layout

```js
scrollLayout: 'full'    // full (default, viewport-height slides) | compact (aspect-ratio height)
```

### Vertical Slides in Scroll View

The scroll view flattens the deck — all slides appear in authored order with no horizontal/vertical distinction.

---

## PDF Export

Works in Chrome/Chromium only.

### Steps

1. Append `?print-pdf` to the URL (e.g., `http://localhost:8000/?print-pdf`)
2. Open print dialog (Ctrl/Cmd+P)
3. Destination: Save as PDF
4. Layout: Landscape
5. Margins: None
6. Enable "Background graphics"
7. Save

### Include Speaker Notes in PDF

```js
Reveal.configure({ showNotes: true });           // overlay on slide
Reveal.configure({ showNotes: 'separate-page' }); // separate page after slide
```

### Page Size

Inferred from presentation size. Limit pages per slide:

```js
Reveal.configure({ pdfMaxPagesPerSlide: 1 });
```

### Fragments in PDF

By default each fragment step is a separate page. Disable:

```js
Reveal.configure({ pdfSeparateFragments: false });
```

### Alternative

Use [decktape](https://github.com/astefanutti/decktape) for command-line PDF export.

---

## Speaker View

Press **S** to open. Shows current slide, next slide preview, speaker notes, and timers.

### Adding Notes

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Speaker notes here</aside>
</section>

<!-- Or via attribute -->
<section data-notes="Notes as attribute">...</section>
```

### In Markdown

```md
## Slide Title

Content here

Note:
Speaker notes after the Note: separator.
```

### Plugin Registration

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
<script>
  Reveal.initialize({ plugins: [RevealNotes] });
</script>
```

### Show Notes to All Viewers

```js
Reveal.initialize({ showNotes: true });
```

### Pacing Timer

Configure timing per slide:

```js
Reveal.initialize({ defaultTiming: 120 }); // seconds per slide
// or
Reveal.initialize({ totalTime: 3600 });    // total presentation time
```

Per-slide override: `<section data-timing="45">`.

### Server-side Speaker Notes

Use [reveal/notes-server](https://github.com/reveal/notes-server) for presenting from a different device.

---

## Lightbox (5.2.0+)

Modal overlay for images, videos, and iframes.

### Image Lightbox

```html
<img src="thumb.png" data-preview-image />
<!-- Or open a different image -->
<img src="thumb.png" data-preview-image="full-size.png" />
```

### Video Lightbox

```html
<video src="clip.mp4" data-preview-video></video>
<img src="thumb.png" data-preview-video="clip.mp4" />
```

### Iframe Lightbox

```html
<a href="https://example.com" data-preview-link>Open</a>
<img src="thumb.png" data-preview-link="https://example.com" />
```

### Media Size in Lightbox

```html
<img src="img.png" data-preview-image data-preview-fit="cover" />
```

Values: `scale-down` (default), `contain`, `cover`.

### Works on Any Element

```html
<button data-preview-video="clip.mp4">Play Video</button>
<a data-preview-image="photo.jpg">View Photo</a>
```

---

## Overview Mode

Press **O** or **Esc** to toggle a zoomed-out slide overview.

```js
Reveal.toggleOverview();
Reveal.isOverview(); // boolean
```

Events:

```js
Reveal.on('overviewshown', (event) => { /* ... */ });
Reveal.on('overviewhidden', (event) => { /* ... */ });
```

---

## Keyboard Shortcuts

| Key | Action |
|:--|:--|
| N, Space, → | Next slide |
| P, ← | Previous slide |
| ↑ | Navigate up (vertical) |
| ↓ | Navigate down (vertical) |
| Home | First slide |
| End | Last slide |
| F | Fullscreen |
| S | Speaker notes |
| O / Esc | Overview |
| B / . | Blackout (pause) |
| ? | Help overlay |
| A | Toggle auto-slide |

Disable keyboard: `Reveal.initialize({ keyboard: false })`.

Custom key bindings in plugins: `deck.addKeyBinding({ keyCode, key }, callback)`.

---

## Slide Visibility

Hide slides from the presentation flow while keeping them in the DOM:

```html
<section data-visibility="hidden">Hidden slide</section>
```

Uncounted slides (visible but excluded from progress/numbering):

```html
<section data-visibility="uncounted">Appendix slide</section>
```

---

## Jump-to-Slide

Press **G** to open a jump-to-slide dialog. Disable:

```js
Reveal.initialize({ jumpToSlide: false });
```

---

## Fullscreen

Press **F** to enter fullscreen mode. This uses the browser's native Fullscreen API.

---

## Touch Navigation

Swipe horizontally between horizontal slides, vertically between vertical slides. Disable:

```js
Reveal.initialize({ touch: false });
```

Prevent swiping on specific elements:

```html
<p data-prevent-swipe>Scrollable content here</p>
```