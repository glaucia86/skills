# React Wrapper Reference (@revealjs/react)

Official React wrapper for reveal.js (v6.0.0+). Package: `@revealjs/react`.

## Installation

```bash
npm i @revealjs/react reveal.js react react-dom
```

## Basic Deck

```tsx
import { Deck, Slide } from '@revealjs/react';
import 'reveal.js/reveal.css';
import 'reveal.js/theme/black.css';

export function Presentation() {
  return (
    <Deck>
      <Slide><h1>Hello</h1></Slide>
      <Slide background="#111827"><h2>Second slide</h2></Slide>
    </Deck>
  );
}
```

## Vertical Slides (Stack)

```tsx
import { Deck, Slide, Stack } from '@revealjs/react';

<Deck>
  <Slide>Intro</Slide>
  <Stack>
    <Slide>Vertical 1</Slide>
    <Slide>Vertical 2</Slide>
  </Stack>
</Deck>
```

## Fragments

```tsx
import { Fragment } from '@revealjs/react';

<Fragment as="p">First point</Fragment>
<Fragment animation="fade-up">Fades up</Fragment>
<Fragment animation="highlight-red" index={2}>Highlighted last</Fragment>
<Fragment asChild><p>Merged onto child</p></Fragment>
```

## Code

```tsx
import { Code } from '@revealjs/react';
import 'reveal.js/plugin/highlight/monokai.css';
import RevealHighlight from 'reveal.js/plugin/highlight';

<Deck plugins={[RevealHighlight]}>
  <Slide>
    <Code language="javascript" lineNumbers="1|2-3">
      {`const a = 1;\nconst b = 2;\nconst c = a + b;`}
    </Code>
  </Slide>
</Deck>
```

Props: `language`, `lineNumbers` (string for step-through), `startFrom` (number), `noEscape`, `trim` (default true), `code` (alternative to children).

## Markdown

```tsx
import { Markdown } from '@revealjs/react';

<Deck>
  <Markdown separator="^\n---\n$" verticalSeparator="^\n--\n$">
    {`
      ## Slide 1
      --
      ## Slide 1.1 (vertical)
      ---
      ## Slide 2
    `}
  </Markdown>
</Deck>
```

- `notesSeparator`: default `Notes:` — lines after it become speaker notes.
- `src` prop: load from external file.
- `options`: `{ animateLists: true, smartypants: true }` and any Marked options.
- Accepts same slide props as `Slide`.

## Configuration

```tsx
<Deck
  config={{ width: 1280, height: 720, hash: true, transition: 'slide' }}
  plugins={[RevealHighlight]}
>
  <Slide>Configured deck</Slide>
</Deck>
```

## Slide Props

- **Background**: `background`, `backgroundColor`, `backgroundImage`, `backgroundVideo`, `backgroundVideoLoop`, `backgroundVideoMuted`, `backgroundIframe`, `backgroundGradient`, `backgroundSize`, `backgroundPosition`, `backgroundRepeat`, `backgroundOpacity`, `backgroundTransition`
- **Auto-animate**: `autoAnimate`, `autoAnimateId`, `autoAnimateRestart`, `autoAnimateUnmatched`, `autoAnimateEasing`, `autoAnimateDuration`, `autoAnimateDelay`
- **Slide options**: `transition`, `transitionSpeed`, `autoSlide`, `visibility`, `notes`, `backgroundInteractive`, `preload`

## Events

```tsx
<Deck
  onReady={(deck) => console.log('Ready', deck)}
  onSlideChange={(event) => console.log(event.indexh)}
  onFragmentShown={(event) => console.log(event.fragment)}
>
```

Available: `onReady`, `onSync`, `onSlideSync`, `onSlideChange`, `onSlideTransitionEnd`, `onFragmentShown`, `onFragmentHidden`, `onOverviewShown`, `onOverviewHidden`, `onPaused`, `onResumed`.

## useReveal() Hook

```tsx
import { useReveal } from '@revealjs/react';

function NextButton() {
  const deck = useReveal();
  return <button onClick={() => deck?.next()}>Next</button>;
}
```

## deckRef (external access)

```tsx
const deckRef = useRef<RevealApi | null>(null);
<Deck deckRef={deckRef}>...</Deck>
```

## How It Works

- `Deck` creates one reveal.js instance on mount, destroys on unmount.
- `deck.sync()` called when slide structure changes.
- `config` is shallow-compared, `configure()` called only on changes.
- `plugins` are initialization-only (captured once on mount).
- Event props are auto-wired/cleaned with `deck.on()`/`deck.off()`.