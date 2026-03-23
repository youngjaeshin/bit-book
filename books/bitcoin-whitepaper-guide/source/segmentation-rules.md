# Bitcoin Whitepaper Guide segmentation rules

## Decision

- Use the Korean EPUB as source of truth.
- The EPUB has one main XHTML body with duplicated TOC markers and inline commentary.
- Split by the **last occurrence** of each numbered section marker, which aligns with the long-form chapter commentary body.
- Merge sections 7 and 8 into one web unit, and sections 9 and 10 into one web unit, to keep reading units balanced.
