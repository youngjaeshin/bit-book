# KO EPUB workflow cheat sheet

Example for The Big Print:

```bash
python3 scripts/unpack_epub.py \
  --epub "epub/The Big Print.epub" \
  --output "books/the-big-print/translated_epub/work/source"

python3 scripts/translate_epub_xhtml.py export \
  --workdir "books/the-big-print/translated_epub/work/source" \
  --chapter-map "books/the-big-print/source/chapter-map.json" \
  --bundle-dir "books/the-big-print/translated_epub/bundles"

# Fill translated_text in bundle JSONs

python3 scripts/translate_epub_xhtml.py apply \
  --workdir "books/the-big-print/translated_epub/work/source" \
  --bundle-dir "books/the-big-print/translated_epub/bundles"

python3 scripts/localize_epub_toc.py \
  --workdir "books/the-big-print/translated_epub/work/source" \
  --bundle-dir "books/the-big-print/translated_epub/bundles" \
  --book-title-ko "더 빅 프린트"

python3 scripts/repack_epub.py \
  --workdir "books/the-big-print/translated_epub/work/source" \
  --output "books/the-big-print/translated_epub/output/the-big-print.ko.epub"

python3 scripts/validate_epub.py \
  --epub "books/the-big-print/translated_epub/output/the-big-print.ko.epub"
```
