# Code Highlighting & Markdown Reference

## Presenting Code

Powered by highlight.js. Requires the `RevealHighlight` plugin and a highlight theme CSS.

### Basic Code Block

```html
<section>
  <pre><code data-trim data-noescape>
    const greeting = 'Hello, world!';
    console.log(greeting);
  </code></pre>
</section>
```

- `data-trim`: removes surrounding whitespace.
- `data-noescape`: prevents HTML escaping.

### Syntax Highlight Theme

Include a theme CSS (e.g. monokai):

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css" />
```

### Line Numbers & Highlights

Add `data-line-numbers` to show line numbers. Specify lines to highlight:

```html
<pre><code data-line-numbers="3,8-10">
...code...
</code></pre>
```

### Line Number Offset (4.2.0+)

```html
<pre><code data-line-numbers data-ln-start-from="7">
...code starting from line 7...
</code></pre>
```

### Step-by-step Highlights

Delimit highlight steps with `|`:

```html
<pre><code data-line-numbers="3-5|8-10|13-15">
...code...
</code></pre>
```

Each step is a fragment — navigating forward highlights the next group.

### Language Selection

Override auto-detection with a class:

```html
<pre><code data-trim class="language-python">
>>> import antigravity
</code></pre>
```

### HTML Entities

Wrap code in `<script type="text/template">` to avoid manual escaping:

```html
<pre><code><script type="text/template">
sealed class Either<out A, out B> {
  data class Left<out A>(val a: A) : Either<A, Nothing>()
}
</script></code></pre>
```

### highlight.js API

```js
Reveal.initialize({
  highlight: {
    beforeHighlight: (hljs) => hljs.registerLanguage(/* ... */),
  },
  plugins: [RevealHighlight],
});
```

### Manual Highlighting

```js
Reveal.initialize({
  highlight: { highlightOnLoad: false },
  plugins: [RevealHighlight],
}).then(() => {
  const highlight = Reveal.getPlugin('highlight');
  highlight.highlightBlock(/* element */);
});
```

---

## Markdown

Write slides in Markdown by adding `data-markdown` to a `<section>` and wrapping content in `<textarea data-template>`.

### Inline Markdown

```html
<section data-markdown>
  <textarea data-template>
    ## Slide 1
    A paragraph with a [link](https://example.com).
    ---
    ## Slide 2
    ---
    ## Slide 3
  </textarea>
</section>
```

Slides are separated by `---` (horizontal rule on its own line).

### Markdown Plugin Registration

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/markdown/markdown.js"></script>
<script>
  Reveal.initialize({ plugins: [RevealMarkdown] });
</script>
```

### External Markdown

Load from a file at runtime (requires a web server):

```html
<section data-markdown="slides.md"
         data-separator="^\n\n\n"
         data-separator-vertical="^\n\n"
         data-separator-notes="^Note:"
         data-charset="iso-8859-15">
</section>
```

### Element Attributes in Markdown

```html
<section data-markdown>
  <script type="text/template">
    - Item 1 <!-- .element: class="fragment" data-fragment-index="2" -->
    - Item 2 <!-- .element: class="fragment" data-fragment-index="1" -->
  </script>
</section>
```

### Slide Attributes in Markdown

```html
<section data-markdown>
  <script type="text/template">
    <!-- .slide: data-background="#ff0000" -->
    Markdown content
  </script>
</section>
```

### Syntax Highlighting in Markdown

````html
<section data-markdown>
  <textarea data-template>
    ```js [1-2|3|4]
    let a = 1;
    let b = 2;
    let c = x => 1 + 2 + x;
    c(3);
    ```
  </textarea>
</section>
````

Line number offset in markdown:

````
```js [712: 1-2|3|4]
let a = 1;
let b = 2;
```
````

### Configuring marked

```js
Reveal.initialize({
  markdown: {
    smartypants: true,
  },
});
```