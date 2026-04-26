# Auto-Animate Reference

Auto-Animate smoothly transitions matching elements between adjacent slides. Add `data-auto-animate` to two consecutive `<section>` elements.

## Basic Usage

```html
<section data-auto-animate>
  <h1>Auto-Animate</h1>
</section>
<section data-auto-animate>
  <h1 style="margin-top: 100px; color: red;">Auto-Animate</h1>
</section>
```

Internally reveal.js uses CSS transforms for smooth movement. Animatable properties include: `position`, `font-size`, `line-height`, `color`, `background-color`, `padding`, `margin`, `opacity`, `border-*`, `border-radius`, `outline`, `letter-spacing`.

## Movement Animations (implicit)

Elements automatically move to their new position when content is added, removed, or rearranged:

```html
<section data-auto-animate>
  <h1>Implicit</h1>
</section>
<section data-auto-animate>
  <h1>Implicit</h1>
  <h1>Animation</h1>
</section>
```

## Element Matching

- **Text**: matched by text content + node type.
- **Images/videos/iframes**: matched by `src` attribute.
- **DOM order**: also considered.
- **Explicit matching**: use `data-id` when automatic matching won't work:

```html
<section data-auto-animate>
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>
```

## Animation Settings

Per-slide or per-element attributes:

| Attribute | Default | Description |
|:--|--:|:--|
| `data-auto-animate-easing` | `ease` | CSS easing function |
| `data-auto-animate-unmatched` | `true` | Unmatched elements fade in (false = appear instantly) |
| `data-auto-animate-duration` | `1.0` | Duration in seconds |
| `data-auto-animate-delay` | `0` | Delay in seconds (element-level only) |
| `data-auto-animate-id` | absent | Groups auto-animate slides together |
| `data-auto-animate-restart` | absent | Breaks auto-animate between adjacent slides |

Global config:

```js
Reveal.initialize({
  autoAnimateEasing: 'ease-out',
  autoAnimateDuration: 0.8,
  autoAnimateUnmatched: false,
});
```

## Auto-Animate Id & Restart

Use `data-auto-animate-id` for separate groups of auto-animated slides. Use `data-auto-animate-restart` to prevent animation between the previous slide and the current one.

```html
<section data-auto-animate><h1>Group A</h1></section>
<section data-auto-animate><h1 style="color: #3B82F6;">Group A</h1></section>
<section data-auto-animate data-auto-animate-id="two"><h1>Group B</h1></section>
<section data-auto-animate data-auto-animate-id="two"><h1 style="color: #10B981;">Group B</h1></section>
<section data-auto-animate data-auto-animate-id="two" data-auto-animate-restart><h1>Group C</h1></section>
<section data-auto-animate data-auto-animate-id="two"><h1 style="color: #EC4899;">Group C</h1></section>
```

## Animating Code Blocks

Ensure `data-line-numbers` is on the `<code>` and both `<pre>` elements have matching `data-id`:

```html
<section data-auto-animate>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let planets = [
      { name: 'mars', diameter: 6779 },
    ]
  </code></pre>
</section>
<section data-auto-animate>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let planets = [
      { name: 'mars', diameter: 6779 },
      { name: 'earth', diameter: 12742 },
      { name: 'jupiter', diameter: 139820 }
    ]
  </code></pre>
</section>
```

## Animating Lists

List items are matched individually:

```html
<section data-auto-animate>
  <ul>
    <li>Mercury</li>
    <li>Jupiter</li>
    <li>Mars</li>
  </ul>
</section>
<section data-auto-animate>
  <ul>
    <li>Mercury</li>
    <li>Earth</li>
    <li>Jupiter</li>
    <li>Saturn</li>
    <li>Mars</li>
  </ul>
</section>
```

## Events

```js
Reveal.on('autoanimate', (event) => {
  // event.fromSlide, event.toSlide
});
```

## State Attributes

- Before animation starts: `data-auto-animate="pending"` on the incoming slide.
- During animation: `data-auto-animate="running"`.
- Each animated element gets `data-auto-animate-target` (unique ID or "unmatched").