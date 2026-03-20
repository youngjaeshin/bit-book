# The Big Print segmentation rules

## Decision

- Exclude front matter, back matter, and part-divider pages by default.
- Keep only the main author-defined chapters for the learning pipeline.
- Use the book TOC as the source of truth for chapter boundaries.

## Excluded by default

- COVER
- REVIEWS
- DEDICATION
- FOREWORD BY MAX KEISER
- INTRODUCTION
- OPENING SCENE
- PREFACE
- FUNDAMENTAL THESIS
- AUTHOR’S STORY
- HOW TO READ THIS BOOK
- PART I THE PROBLEM (group heading only)
- PART II THE SOLUTION (group heading only)
- ACKNOWLEDGEMENTS
- KEEP IN TOUCH
- SUGGESTED FURTHER READING
- APPENDIX A: LEPARD PERSONAL BACKGROUND
- ADDENDA

## Included chapters

- Part I chapters: TOC 12-22
- Part II chapters: TOC 24-36
- Total included chapters: 24

## Output path rules

- Source chapter markdown: `books/the-big-print/source/chapters/NN-slug.md`
- English markdown: `books/the-big-print/content/en/chapters/NN-slug.md`
- Korean markdown: `books/the-big-print/content/ko/chapters/NN-slug.md`
- Quiz JSON: `books/the-big-print/quiz/chapters/NN-slug.quiz.json`
- HTML: `books/the-big-print/site/chapters/NN-slug.html`

## Notes

- If the user later wants the Introduction/Fundamental Thesis block included, move those TOC entries from `excluded-sections.json` into `chapter-map.json`.
- PDF pipeline should target the same logical chapter outputs when chapter headings are detectable.
