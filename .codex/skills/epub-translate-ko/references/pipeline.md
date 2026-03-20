# EPUB → Korean EPUB pipeline

## Goal

영어 EPUB을 한국어 EPUB으로 변환하되,
원본 EPUB 구조를 최대한 유지해서 읽을 수 있는 `.ko.epub`를 만든다.

## Canonical flow

1. **Locate source**
   - 원본 EPUB
   - `chapter-map.json`
   - metadata/toc artifacts

2. **Unpack**
   - unzip to working directory
   - preserve `mimetype`, `META-INF`, `OEBPS` 구조

3. **Identify translatable XHTML**
   - chapter map 기준으로 chapter XHTML 선택
   - front matter / appendix는 정책에 따라 번역 여부 결정

4. **Translate content nodes**
   - `h1/h2/h3/p/li/blockquote/caption` 위주
   - id/href/src/class/style는 최대한 보존

5. **Update navigation**
   - 필요 시 nav / ncx title 한글화
   - href target은 유지

6. **Repack**
   - `mimetype` first, uncompressed
   - rest zipped normally
   - output: `<slug>.ko.epub`

7. **Validate**
   - zip structure
   - file open
   - toc jump
   - Korean rendering

## Node handling policy

- **Translate**
  - headings
  - paragraphs
  - list items
  - captions
- **Preserve**
  - ids
  - href/src
  - anchor structure
  - image files
  - CSS/stylesheet refs

## Default non-goals

- full visual redesign of the EPUB
- removing all original classes/styles
- re-authoring layout from scratch

Keep the book readable first.
