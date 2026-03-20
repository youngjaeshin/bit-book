# Reassembly quality checklist

## Minimum pass criteria

- [ ] `.ko.epub` file is created successfully
- [ ] EPUB opens in a standard reader
- [ ] TOC displays
- [ ] TOC links jump to correct chapters
- [ ] Korean text does not appear garbled
- [ ] Major chapter headings render correctly
- [ ] Images still load where expected
- [ ] Footnote/backlinks are not obviously broken

## Structural checks

- [ ] `mimetype` exists and is the first zip entry
- [ ] `META-INF/container.xml` still points to valid OPF
- [ ] OPF manifest/spine references valid files
- [ ] nav/ncx href targets exist

## Content checks

- [ ] No untranslated chapter bodies where translation was expected
- [ ] No obvious tag corruption
- [ ] No duplicated paragraphs from reinsertion bugs
- [ ] Chapter order preserved

## Translation checks

- [ ] Austrian economics terms consistent
- [ ] Bitcoin-native terms consistent
- [ ] Author viewpoint preserved
- [ ] Korean phrasing readable as ebook prose

## Nice-to-have checks

- [ ] Chapter titles in nav are localized
- [ ] Captions translated cleanly
- [ ] Long emphasis/blockquote formatting preserved
