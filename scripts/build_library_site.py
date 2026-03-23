#!/usr/bin/env python3
"""
Build an ordered bitcoin bookshelf site with cover-driven navigation.
"""

from __future__ import annotations

import html
import json
import posixpath
import shutil
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(".")
BOOKS_DIR = ROOT / "books"
OUT_DIR = ROOT / "library-site"
ASSETS_DIR = OUT_DIR / "assets"
COVERS_DIR = ASSETS_DIR / "covers"
TEMPLATES = ROOT / "templates"
SCREENSHOT_DIR = ROOT / "screenshot"

DC_NS = {"dc": "http://purl.org/dc/elements/1.1/"}
CONTAINER_NS = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}

CURATED_BOOKS = [
    {
        "order": 1,
        "slug": "bitcoin-for-everyone",
        "title": "모두를 위한 비트코인",
        "original_title": "Bitcoin for Everyone",
        "source_note": "한국어 EPUB만 확보됨",
        "files": [
            {"kind": "ko", "format": "EPUB", "filename": "01_모두를 위한 비트코인(완성).epub"},
        ],
        "cover_source": "01_모두를 위한 비트코인(완성).epub",
    },
    {
        "order": 2,
        "slug": "blind-robbery",
        "title": "왜 그들만 부자가 되는가",
        "original_title": "Blind Robbery!",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "02_Blind Robbery!.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "02_왜 그들만 부자가 되는가.epub"},
        ],
        "cover_source": "02_왜 그들만 부자가 되는가.epub",
    },
    {
        "order": 3,
        "slug": "the-bitcoin-standard",
        "title": "달러는 왜 비트코인을 싫어하는가",
        "original_title": "The Bitcoin Standard",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "03. The Bitcoin Standard.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "03. 달러는 왜 비트코인을 싫어하는가.epub"},
        ],
        "cover_source": "03. 달러는 왜 비트코인을 싫어하는가.epub",
    },
    {
        "order": 4,
        "slug": "21-lessons",
        "title": "21가지 교훈",
        "original_title": "21 Lessons",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "04. 21 Lessons.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "04. 21가지 교훈.epub"},
        ],
        "cover_source": "04. 21가지 교훈.epub",
    },
    {
        "order": 5,
        "slug": "the-fiat-standard",
        "title": "피아트 스탠다드",
        "original_title": "The Fiat Standard",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "05. The Fiat Standard.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "05. fixed_피아트 스탠다드.epub"},
        ],
        "cover_source": "05. fixed_피아트 스탠다드.epub",
    },
    {
        "order": 6,
        "slug": "the-bullish-case-for-bitcoin",
        "title": "비트코인 낙관론",
        "original_title": "The Bullish Case for Bitcoin",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "06. The Bullish Case for Bitcoin.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "06. 비트코인 낙관론.epub"},
        ],
        "cover_source": "06. 비트코인 낙관론.epub",
    },
    {
        "order": 7,
        "slug": "layered-money",
        "title": "레이어드 머니",
        "original_title": "Layered Money",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "07. Layered Money.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "07. 레이어드 머니.epub"},
        ],
        "cover_source": "07. 레이어드 머니.epub",
    },
    {
        "order": 8,
        "slug": "bitcoin-diploma",
        "title": "비트코인 디플로마",
        "original_title": "Bitcoin Diploma",
        "source_note": "한국어 EPUB만 확보됨",
        "files": [
            {"kind": "ko", "format": "EPUB", "filename": "08. 비트코인 디플로마.epub"},
        ],
        "cover_source": "08. 비트코인 디플로마.epub",
    },
    {
        "order": 9,
        "slug": "bitcoin-whitepaper-guide",
        "title": "비트코인 백서 해설",
        "original_title": "Bitcoin Whitepaper Guide",
        "source_note": "한국어 EPUB만 확보됨",
        "files": [
            {"kind": "ko", "format": "EPUB", "filename": "09. 비트코인 백서 해설.epub"},
        ],
        "cover_source": "09. 비트코인 백서 해설.epub",
    },
    {
        "order": 10,
        "slug": "bitcoin-user-guide",
        "title": "비트코인 사용 가이드",
        "original_title": "Bitcoin User Guide",
        "source_note": "PDF 원본이라 EPUB보다 후순위 파이프라인이 필요함",
        "files": [
            {"kind": "ko", "format": "PDF", "filename": "10_비트코인 사용 가이드.pdf"},
        ],
        "cover_source": "10_비트코인 사용 가이드.pdf",
    },
    {
        "order": 11,
        "slug": "the-blocksize-war",
        "title": "비트코인 블록사이즈 전쟁",
        "original_title": "The Blocksize War",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "11. The Blocksize War.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "11. 블록사이즈 전쟁.epub"},
        ],
        "cover_source": "11. 블록사이즈 전쟁.epub",
    },
    {
        "order": 12,
        "slug": "bitcoin-handbook",
        "title": "비트코인 핸드북",
        "original_title": "The Bitcoin Handbook",
        "files": [
            {"kind": "en", "format": "EPUB", "filename": "12. Bitcoin Handbook.epub"},
            {"kind": "ko", "format": "EPUB", "filename": "12. 비트코인 핸드북.epub"},
        ],
        "cover_source": "12. 비트코인 핸드북.epub",
    },
]


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFC", value)


def find_essentials_dir() -> Path:
    epub_root = ROOT / "epub"
    for child in epub_root.iterdir():
        if child.is_dir() and "비트코인 필수" in normalize_text(child.name):
            return child
    raise FileNotFoundError("Could not find epub/비트코인 필수 directory")


def find_named_file(directory: Path, filename: str) -> Path:
    target = normalize_text(filename)
    for child in directory.iterdir():
        if normalize_text(child.name) == target:
            return child
    raise FileNotFoundError(f"Could not find {filename} in {directory}")


def parse_markdown(path: Path) -> list[tuple[str, object]]:
    lines = path.read_text().splitlines()
    out: list[tuple[str, object]] = []
    paragraph: list[str] = []
    bullets: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(("p", " ".join(paragraph).strip()))
            paragraph = []

    def flush_bullets() -> None:
        nonlocal bullets
        if bullets:
            out.append(("ul", bullets[:]))
            bullets = []

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_paragraph()
            flush_bullets()
            continue
        if line.startswith("# "):
            flush_paragraph()
            flush_bullets()
            out.append(("h1", line[2:].strip()))
        elif line.startswith("## "):
            flush_paragraph()
            flush_bullets()
            out.append(("h2", line[3:].strip()))
        elif line.startswith("### "):
            flush_paragraph()
            flush_bullets()
            out.append(("h3", line[4:].strip()))
        elif line.startswith("- "):
            flush_paragraph()
            bullets.append(line[2:].strip())
        else:
            flush_bullets()
            paragraph.append(line)
    flush_paragraph()
    flush_bullets()
    return out


def markdown_to_html(path: Path) -> str:
    chunks = ['<div class="digest">']
    for kind, payload in parse_markdown(path):
        if kind == "h1":
            chunks.append(f"<h2>{html.escape(str(payload))}</h2>")
        elif kind == "h2":
            chunks.append(f"<h3>{html.escape(str(payload))}</h3>")
        elif kind == "h3":
            chunks.append(f"<h4>{html.escape(str(payload))}</h4>")
        elif kind == "p":
            chunks.append(f"<p>{html.escape(str(payload))}</p>")
        elif kind == "ul":
            chunks.append("<ul>" + "".join(f"<li>{html.escape(item)}</li>" for item in payload) + "</ul>")
    chunks.append("</div>")
    return "\n".join(chunks)


def chapter_title(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def quiz_to_html(quiz: dict, lang: str) -> str:
    if lang == "en":
        question = quiz["question_en"]
        choices = quiz["choices_en"]
        explanation = quiz["explanation_en"]
        answer_label = quiz["choices_en"][quiz["answer_index"]]
    else:
        question = quiz["question_ko"]
        choices = quiz["choices_ko"]
        explanation = quiz["explanation_ko"]
        answer_label = quiz["choices_ko"][quiz["answer_index"]]

    options = [
        f'<button class="quiz-option" data-option-index="{idx}">{html.escape(label)}</button>'
        for idx, label in enumerate(choices)
    ]
    result = html.escape(f"Answer: {answer_label} — {explanation}")
    return f"""
<div class="quiz-box" data-answer-index="{quiz['answer_index']}"
     data-correct-text="{result}"
     data-wrong-text="{result}">
  <h3>{html.escape(question)}</h3>
  <div class="quiz-options">
    {''.join(options)}
  </div>
  <div class="quiz-result" hidden></div>
</div>
""".strip()


def load_epub_package(epub_path: Path) -> tuple[ET.Element, str, zipfile.ZipFile]:
    archive = zipfile.ZipFile(epub_path)
    container = ET.fromstring(archive.read("META-INF/container.xml"))
    opf_path = container.find(".//c:rootfile", CONTAINER_NS).attrib["full-path"]
    package = ET.fromstring(archive.read(opf_path))
    return package, opf_path, archive


def read_epub_metadata(epub_path: Path) -> dict[str, str]:
    package, _, archive = load_epub_package(epub_path)
    try:
        metadata = package.find("{*}metadata")
        if metadata is None:
            return {}
        def value(tag: str) -> str:
            node = metadata.find(f"dc:{tag}", DC_NS)
            return node.text.strip() if node is not None and node.text else ""
        return {
            "title": value("title"),
            "author": value("creator"),
            "language": value("language"),
        }
    finally:
        archive.close()


def cover_extension(media_type: str, href: str) -> str:
    suffix = Path(href).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        return suffix
    return {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
    }.get(media_type, ".img")


def extract_epub_cover(epub_path: Path, out_stem: Path) -> Path | None:
    package, opf_path, archive = load_epub_package(epub_path)
    try:
        manifest = package.find("{*}manifest")
        metadata = package.find("{*}metadata")
        if manifest is None:
            return None

        cover_id = None
        if metadata is not None:
            for meta in metadata.findall("{*}meta"):
                if meta.attrib.get("name") == "cover":
                    cover_id = meta.attrib.get("content")
                    break

        cover_item = None
        for item in manifest.findall("{*}item"):
            if item.attrib.get("properties") == "cover-image":
                cover_item = item
                break
            if cover_id and item.attrib.get("id") == cover_id:
                cover_item = item
                break

        if cover_item is None:
            for item in manifest.findall("{*}item"):
                media_type = item.attrib.get("media-type", "")
                item_id = item.attrib.get("id", "").lower()
                href = item.attrib.get("href", "").lower()
                if media_type.startswith("image/") and ("cover" in item_id or "cover" in href):
                    cover_item = item
                    break

        if cover_item is None:
            return None

        href = cover_item.attrib["href"]
        inner_path = posixpath.normpath(posixpath.join(posixpath.dirname(opf_path), href))
        media_type = cover_item.attrib.get("media-type", "")
        extension = cover_extension(media_type, href)
        out_path = out_stem.with_suffix(extension)
        out_path.write_bytes(archive.read(inner_path))
        return out_path
    finally:
        archive.close()


def copy_manual_cover(source_path: Path, out_stem: Path) -> Path:
    out_path = out_stem.with_suffix(source_path.suffix.lower())
    shutil.copyfile(source_path, out_path)
    return out_path


def load_manual_cover_paths() -> dict[int, Path]:
    if not SCREENSHOT_DIR.exists():
        return {}
    image_suffixes = {".png", ".jpg", ".jpeg", ".webp"}
    fixed = {}
    for index in range(1, 13):
        for suffix in (".png", ".jpg", ".jpeg", ".webp"):
            candidate = SCREENSHOT_DIR / f"{index:02d}{suffix}"
            if candidate.exists():
                fixed[index] = candidate
                break
    if fixed:
        return fixed
    screenshots = sorted(path for path in SCREENSHOT_DIR.iterdir() if path.is_file() and path.suffix.lower() in image_suffixes)
    return {index: path for index, path in enumerate(screenshots, start=1)}


def render_cover(book: dict, cover_href: str, relative_prefix: str) -> str:
    if cover_href:
        return (
            f'<div class="book-cover-frame">'
            f'<img src="{relative_prefix}{cover_href}" alt="{html.escape(book["title"])} cover" class="book-cover-image" />'
            f"</div>"
        )
    return f"""
<div class="book-cover-frame book-cover-placeholder">
  <div class="cover-placeholder-inner">
    <span class="cover-placeholder-format">{html.escape(book['primary_format'])}</span>
    <strong>{html.escape(book['title'])}</strong>
  </div>
</div>
""".strip()


def render_home(books: list[dict]) -> str:
    published_count = sum(1 for book in books if book["ready"])
    epub_pair_count = sum(1 for book in books if book["lang_label"] == "EN + KO")
    cards = []
    for book in books:
        cards.append(
            f"""
<li class="shelf-card">
  <a href="./books/{book['slug']}/index.html" class="shelf-link{' ready' if book['ready'] else ''}">
    <span class="sequence-badge">{book['order']}</span>
    {render_cover(book, book['cover_href'], "./")}
    <div class="shelf-copy">
      <p class="shelf-kicker">{html.escape(book['status_label'])}</p>
      <h2 class="shelf-title">{html.escape(book['title'])}</h2>
      <p class="shelf-subtitle">{html.escape(book['original_title'])}</p>
      <span class="book-cta">{'요약 읽기 →' if book['ready'] else '책 정보 보기 →'}</span>
    </div>
  </a>
</li>
""".strip()
        )

    return f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>btc-book</title>
    <link rel="stylesheet" href="./assets/styles.css" />
  </head>
  <body class="library-home">
    <main class="container">
      <header class="hero shelf-hero">
        <h1 class="brand-title">btc-book</h1>
        <nav class="library-tabs" aria-label="bookshelf categories">
          <button class="library-tab active" type="button" aria-current="page">비트코인 필수</button>
          <button class="library-tab disabled" type="button" disabled>자유주의 필수</button>
          <button class="library-tab disabled" type="button" disabled>비트코인 일반</button>
        </nav>
        <p class="subtitle">표지를 누르면 책 소개와 진행 상태를 보고, 준비된 책은 바로 챕터 요약으로 들어갈 수 있습니다.</p>
        <div class="hero-stats">
          <span class="hero-pill">총 12권</span>
          <span class="hero-pill">웹 공개 {published_count}권</span>
          <span class="hero-pill">영한 EPUB 쌍 {epub_pair_count}권</span>
        </div>
      </header>
      <section class="card shelf-card-shell">
        <div class="section-head">
          <h2>비트코인 필수</h2>
          <p class="section-copy">현재 열려 있는 서가입니다. 나머지 탭은 준비 후 활성화됩니다.</p>
        </div>
        <ol class="bookshelf-grid">
          {"".join(cards)}
        </ol>
      </section>
    </main>
  </body>
</html>"""


def render_book_index(book: dict, chapter_entries: list[str]) -> str:
    status_copy = (
        f"{book['chapter_count']}개 챕터 요약과 퀴즈를 바로 읽을 수 있습니다."
        if book["ready"]
        else "아직 요약/퀴즈/챕터 페이지를 생성하기 전 단계입니다."
    )
    chapter_section = f"""
<section class="card">
  <div class="section-head">
    <h2>챕터 목록</h2>
    <p class="section-copy">준비된 챕터 요약으로 바로 들어갑니다.</p>
  </div>
  <ol class="chapter-list">
    {"".join(chapter_entries)}
  </ol>
</section>
""".strip() if book["ready"] else f"""
<section class="card">
  <div class="section-head">
    <h2>진행 예정</h2>
    <p class="section-copy">이 책은 Big Print 때처럼 아래 순서로 붙일 예정입니다.</p>
  </div>
  <ol class="chapter-list roadmap-list">
    <li>EPUB/PDF 구조 점검 및 메타데이터 보정</li>
    <li>챕터 분리와 요약 포맷 고정</li>
    <li>퀴즈 생성 및 HTML 렌더링</li>
    <li>통합 라이브러리 반영 및 재배포</li>
  </ol>
</section>
""".strip()

    return f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(book['title'])}</title>
    <link rel="stylesheet" href="../../assets/styles.css" />
  </head>
  <body class="library-book-page">
    <main class="container">
      <nav class="topnav"><a href="../../index.html">← Back to library</a></nav>
      <header class="book-hero card">
        <div class="book-hero-cover">
          <span class="sequence-badge large">{book['order']}</span>
          {render_cover(book, book['cover_href'], "../../")}
        </div>
        <div class="book-hero-copy">
          <p class="eyebrow">{html.escape(book['status_label'])}</p>
          <h1>{html.escape(book['title'])}</h1>
          <p class="subtitle">{html.escape(book['original_title'])}</p>
          <p class="book-status-copy">{html.escape(status_copy)}</p>
        </div>
      </header>
      {chapter_section}
    </main>
  </body>
</html>"""


def render_chapter_page(
    book: dict,
    chapter: dict,
    en_html: str,
    ko_html: str,
    quiz_en: str,
    quiz_ko: str,
    prev_chapter: dict | None,
    next_chapter: dict | None,
) -> str:
    nav_links: list[str] = []
    if prev_chapter is not None:
        nav_links.append(
            f'<a class="chapter-nav-link prev" href="./{prev_chapter["slug"]}.html">← {html.escape(prev_chapter["title_ko"])}</a>'
        )
    if next_chapter is not None:
        nav_links.append(
            f'<a class="chapter-nav-link next" href="./{next_chapter["slug"]}.html">{html.escape(next_chapter["title_ko"])} →</a>'
        )
    pagination = f'<nav class="chapter-pagination">{"".join(nav_links)}</nav>' if nav_links else ""

    return f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(chapter['title_ko'])} · {html.escape(book['title'])}</title>
    <link rel="stylesheet" href="../../../assets/styles.css" />
  </head>
  <body class="library-book-page library-reading-page">
    <main class="container">
      <nav class="topnav">
        <a href="../index.html">← Back to book</a> · <a href="../../../index.html">Library</a>
      </nav>
      <header class="reading-hero card">
        <p class="eyebrow">{html.escape(book['title'])}</p>
        <h1>{html.escape(chapter['title_ko'])}</h1>
        <p class="subtitle reading-subtitle">{html.escape(chapter['title_en'])}</p>
      </header>
      <div class="lang-toggle reading-toggle">
        <button class="lang-btn" data-lang="en">English</button>
        <button class="lang-btn active" data-lang="ko">한국어</button>
      </div>
      <section class="grid reading-grid">
        <article class="card lang-panel" data-lang="en">{en_html}</article>
        <article class="card lang-panel active" data-lang="ko">{ko_html}</article>
      </section>
      <section class="card quiz-card">
        <div class="quiz-panel" data-lang="en">
          <h2>Quiz</h2>
          {quiz_en}
        </div>
        <div class="quiz-panel active" data-lang="ko">
          <h2>퀴즈</h2>
          {quiz_ko}
        </div>
      </section>
      {pagination}
    </main>
    <script>
      const buttons = document.querySelectorAll(".lang-btn");
      const panels = document.querySelectorAll(".lang-panel");
      const quizPanels = document.querySelectorAll(".quiz-panel");
      buttons.forEach((btn) => {{
        btn.addEventListener("click", () => {{
          const lang = btn.dataset.lang;
          buttons.forEach((b) => b.classList.toggle("active", b === btn));
          panels.forEach((p) => p.classList.toggle("active", p.dataset.lang === lang));
          quizPanels.forEach((p) => p.classList.toggle("active", p.dataset.lang === lang));
        }});
      }});
      document.querySelectorAll(".quiz-option").forEach((btn) => {{
        btn.addEventListener("click", () => {{
          const parent = btn.closest(".quiz-box");
          const answer = Number(parent.dataset.answerIndex);
          const idx = Number(btn.dataset.optionIndex);
          const result = parent.querySelector(".quiz-result");
          parent.querySelectorAll(".quiz-option").forEach((node) => {{
            node.classList.remove("correct", "wrong");
          }});
          if (idx === answer) {{
            btn.classList.add("correct");
            result.textContent = parent.dataset.correctText;
          }} else {{
            btn.classList.add("wrong");
            parent.querySelector(`[data-option-index="${{answer}}"]`).classList.add("correct");
            result.textContent = parent.dataset.wrongText;
          }}
          result.hidden = false;
        }});
      }});
    </script>
  </body>
</html>"""


def book_build_data(slug: str) -> dict | None:
    book_root = BOOKS_DIR / slug
    metadata_path = book_root / "source" / "metadata.json"
    en_dir = book_root / "content" / "en" / "chapters"
    ko_dir = book_root / "content" / "ko" / "chapters"
    quiz_dir = book_root / "quiz" / "chapters"
    if not metadata_path.exists() or not en_dir.exists() or not ko_dir.exists() or not quiz_dir.exists():
        return None
    en_count = len(list(en_dir.glob("*.md")))
    ko_count = len(list(ko_dir.glob("*.md")))
    quiz_count = len(list(quiz_dir.glob("*.json")))
    if not en_count or not ko_count or not quiz_count:
        return None
    metadata = json.loads(metadata_path.read_text())
    return {
        "metadata": metadata,
        "en_dir": en_dir,
        "ko_dir": ko_dir,
        "quiz_dir": quiz_dir,
        "chapter_count": min(en_count, ko_count, quiz_count),
    }


def build_catalog() -> list[dict]:
    essentials_dir = find_essentials_dir()
    manual_covers = load_manual_cover_paths()
    books: list[dict] = []
    for entry in CURATED_BOOKS:
        book = dict(entry)
        source_files = []
        for source in book["files"]:
            resolved = find_named_file(essentials_dir, source["filename"])
            source_files.append(
                {
                    "label": f'{source["kind"].upper()} {source["format"]}',
                    "filename": resolved.name,
                    "path": resolved,
                }
            )
        book["source_files"] = source_files
        book["primary_format"] = source_files[0]["filename"].split(".")[-1].upper()
        book["lang_label"] = "EN + KO" if any(f["label"].startswith("EN") for f in source_files) and any(f["label"].startswith("KO") for f in source_files) else "KO only"
        book["source_note"] = book.get("source_note", "영문 원서와 한국어 번역 EPUB이 함께 있음" if book["lang_label"] == "EN + KO" else "한국어본만 확보됨")
        meta_source = next((item["path"] for item in source_files if item["path"].suffix.lower() == ".epub" and item["label"].startswith("EN")), None)
        if meta_source is None:
            meta_source = next((item["path"] for item in source_files if item["path"].suffix.lower() == ".epub"), None)
        source_meta = read_epub_metadata(meta_source) if meta_source else {}
        book["author"] = source_meta.get("author") or book.get("author", "")
        build_data = book_build_data(book["slug"])
        book["ready"] = build_data is not None
        book["chapter_count"] = build_data["chapter_count"] if build_data else 0
        book["status_label"] = "웹에서 읽기 가능" if build_data else "요약 준비 중"
        book["home_tags"] = [f'{book["order"]}번', book["primary_format"], book["lang_label"], "Published" if book["ready"] else "Queue"]
        book["detail_tags"] = [book["primary_format"], book["lang_label"], "요약 공개됨" if book["ready"] else "준비 중"]

        cover_href = ""
        manual_cover_path = manual_covers.get(book["order"])
        if manual_cover_path is not None:
            copied = copy_manual_cover(manual_cover_path, COVERS_DIR / book["slug"])
            cover_href = f"assets/covers/{copied.name}"
        else:
            cover_source_path = find_named_file(essentials_dir, book["cover_source"])
            if cover_source_path.suffix.lower() == ".epub":
                extracted = extract_epub_cover(cover_source_path, COVERS_DIR / book["slug"])
                if extracted is not None:
                    cover_href = f"assets/covers/{extracted.name}"
        book["cover_href"] = cover_href
        book["build_data"] = build_data
        books.append(book)
    return books


def build() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    COVERS_DIR.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(COVERS_DIR, ignore_errors=True)
    COVERS_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TEMPLATES / "styles.css", ASSETS_DIR / "styles.css")
    (OUT_DIR / ".gitignore").write_text(".vercel\n")

    books = build_catalog()
    (OUT_DIR / "index.html").write_text(render_home(books))

    for book in books:
        book_out = OUT_DIR / "books" / book["slug"]
        chapters_out = book_out / "chapters"
        chapters_out.mkdir(parents=True, exist_ok=True)

        chapter_entries: list[str] = []
        chapter_records: list[dict] = []
        build_data = book["build_data"]
        if build_data is not None:
            for en_path in sorted(build_data["en_dir"].glob("*.md")):
                chapter_slug = en_path.stem
                ko_path = build_data["ko_dir"] / en_path.name
                quiz_path = build_data["quiz_dir"] / f"{chapter_slug}.quiz.json"
                if not ko_path.exists() or not quiz_path.exists():
                    continue
                chapter_name_en = chapter_title(en_path)
                chapter_name_ko = chapter_title(ko_path)
                chapter_entries.append(f'<li><a href="./chapters/{chapter_slug}.html">{html.escape(chapter_name_ko)}</a></li>')
                chapter_records.append(
                    {
                        "slug": chapter_slug,
                        "title_en": chapter_name_en,
                        "title_ko": chapter_name_ko,
                        "en_path": en_path,
                        "ko_path": ko_path,
                        "quiz_path": quiz_path,
                    }
                )

            for idx, chapter_rec in enumerate(chapter_records):
                en_html = markdown_to_html(chapter_rec["en_path"])
                ko_html = markdown_to_html(chapter_rec["ko_path"])
                quiz = json.loads(chapter_rec["quiz_path"].read_text())
                quiz_en = quiz_to_html(quiz, "en")
                quiz_ko = quiz_to_html(quiz, "ko")
                prev_chapter = chapter_records[idx - 1] if idx > 0 else None
                next_chapter = chapter_records[idx + 1] if idx + 1 < len(chapter_records) else None
                chapter_page = render_chapter_page(
                    book,
                    {"title_en": chapter_rec["title_en"], "title_ko": chapter_rec["title_ko"]},
                    en_html,
                    ko_html,
                    quiz_en,
                    quiz_ko,
                    prev_chapter,
                    next_chapter,
                )
                (chapters_out / f'{chapter_rec["slug"]}.html').write_text(chapter_page)

        (book_out / "index.html").write_text(render_book_index(book, chapter_entries))

    published = sum(1 for book in books if book["ready"])
    print(f"Built curated library site for {len(books)} books ({published} published)")


if __name__ == "__main__":
    build()
