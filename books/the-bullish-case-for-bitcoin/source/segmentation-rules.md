# The Bullish Case for Bitcoin segmentation rules

## Decision

- Use the English original EPUB as the source of truth.
- Convert the original 11 TOC entries into 8 web-summary units.
- Merge `Foreword` + `Prologue` into one opening unit.
- Keep Chapters 1-4 as standalone units.
- Split Chapter 5 (`A New Monetary Base`) into two units using the EPUB spine break between `Common Misconceptions` and `Real Risks`.
- Merge `Epilogue` + `Acknowledgments` + `Disclaimer` + `About the Author` into one closing unit.

## Notes

- Chapter 5 begins with an image-only opener file (`text/part0015.html`) followed by three split XHTML files.
- Web unit 6 should capture the `Common Misconceptions` cluster.
- Web unit 7 should capture `Real Risks` and `Conclusion`.
- Extraction should follow the EPUB spine range between one unit start and the next unit start.
