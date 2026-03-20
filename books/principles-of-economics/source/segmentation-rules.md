# Principles of Economics segmentation rules

## Decision

- Exclude front matter, back matter, and part-divider pages by default.
- Keep only chapter-level entries (`Chapter N: ...`) as primary learning units.
- Collapse subsection anchors inside each chapter rather than promoting them to standalone chapters.

## Excluded by default

- Front Matter
- Copyright
- Dedication
- Table of Contents
- About the Author
- Introduction
- PART I. FUNDAMENTALS
- PART II. ECONOMY
- PART III. THE MARKET ORDER
- PART IV. MONETARY ECONOMICS
- PART V. CIVILIZATION
- Appendix 1
- Bibliography

## Included primary chapters

- Total included chapters: 18
- Range: Chapter 1 through Chapter 18

## Nested sections

- Subsection TOC anchors such as `Action, Purpose, and Reason` and `Utility and Value` stay within their parent chapter.
- They should shape chapter summaries, quiz questions, and section headings, but not become separate chapter pages by default.

## Output path rules

- Source chapter markdown: `books/principles-of-economics/source/chapters/NN-title.md`
- English markdown: `books/principles-of-economics/content/en/chapters/NN-title.md`
- Korean markdown: `books/principles-of-economics/content/ko/chapters/NN-title.md`
- Quiz JSON: `books/principles-of-economics/quiz/chapters/NN-title.quiz.json`
- HTML: `books/principles-of-economics/site/chapters/NN-title.html`
