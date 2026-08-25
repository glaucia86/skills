---
name: eli5
description: Create a dead-simple visual explanation of any topic as a self-contained HTML artifact with big visuals, plain language, and very few words. Use when the user invokes eli5, says "explain like I'm five," asks for a beginner-friendly picture explainer, or wants to understand how something works without assuming prior knowledge. Do not use for a normal detailed tutorial, code-only implementation, or text-only summary unless the user explicitly requests the ELI5 treatment.
---

# ELI5 Visual Explainer

Turn the requested topic into a compact visual story that a complete beginner can understand. Treat “like I’m five” as a request for clarity, not permission to be patronizing or inaccurate.

## Resolve the request

1. Derive the topic, audience, language, and any constraints from the current user request.
2. Do not depend on host-specific placeholders such as `$ARGUMENTS`. The invocation message is the input.
3. Ask a question only when the missing information would materially change the explanation. Otherwise choose sensible defaults and proceed.
4. Default to the user’s language and a complete-beginner audience.

## Establish the truth

1. Identify the one idea the learner should remember.
2. Reduce the topic to three to six causal steps or relationships.
3. Choose one familiar visual analogy, then map each analogy element to the real concept.
4. Preserve essential caveats. Never make an explanation simple by making it false.
5. For current or high-stakes topics, verify important facts with authoritative sources when the host provides research tools. Add a tiny sources section only when sources were actually used.
6. For personalized medical, legal, or financial requests, explain the general concept and clearly avoid presenting the artifact as individualized professional advice.

## Design the visual story

Use this narrative order unless the topic calls for a better one:

1. **Big answer:** one plain-language sentence.
2. **Familiar analogy:** show the learner something they already know.
3. **How it works:** three to six visual scenes connected by an obvious flow.
4. **Real names:** reveal the proper terms after the intuition is established.
5. **Tiny recap:** restate the idea in one memorable sentence.

Prefer diagrams made from layout, shapes, arrows, icons, emoji, and inline SVG. Use generated or retrieved imagery only when the host supports it and the image materially improves understanding; the explainer must still work without remote assets.

## Create the HTML artifact

Produce one standalone `.html` file with these properties:

- Embed all CSS and JavaScript in the file.
- Avoid CDNs, remote fonts, tracking, network requests, build steps, and framework dependencies.
- Use responsive layout that works from a narrow phone to a desktop.
- Make the visual hierarchy unmistakable: large title, large central visuals, short labels, generous spacing.
- Keep each scene focused on one idea and use few words. Prefer a short phrase over a paragraph.
- Use semantic HTML, readable contrast, visible focus states, descriptive labels, and reduced-motion support.
- Do not rely on color alone to communicate meaning.
- Keep motion optional, subtle, and explanatory. The page must remain understandable with JavaScript disabled.
- Escape user-provided text before placing it into HTML.
- Include a print-friendly style.

Use the host’s native artifact or file-writing capability. Unless the user explicitly provides a full filename, name the file `eli5-<topic-slug>.html`, including when the user provides only a destination directory. If the host cannot create files or artifacts, return the complete standalone HTML in one fenced `html` block and state the intended filename.

## Keep the explanation genuinely simple

- Introduce at most one new term per scene.
- Define every necessary technical term in ordinary language.
- Prefer concrete nouns and active verbs.
- Avoid jargon, unexplained acronyms, walls of text, decorative dashboards, and UI controls that do not teach anything.
- Never use lorem ipsum or placeholder copy.
- Keep the analogy visually consistent from beginning to end.
- When an analogy has an important limitation, add one short “where the analogy stops” note.

## Validate before delivery

Check the final artifact against all of the following:

- A beginner can state the main idea after one scan.
- The causal direction and reading order are visually obvious.
- Every visual has a teaching purpose.
- The analogy and the real-world terms agree.
- The file is self-contained and opens without a server.
- The layout remains readable at approximately 375 px and 1440 px widths.
- There are no broken tags, placeholders, external dependencies, or fabricated facts.

Deliver the artifact and summarize its central explanation in one sentence. Do not bury the file behind a long process report.
