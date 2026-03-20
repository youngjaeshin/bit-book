#!/usr/bin/env python3
"""
Build one integrated static site containing multiple books.
"""

from __future__ import annotations

import html
import json
import shutil
from pathlib import Path


ROOT = Path(".")
BOOKS_DIR = ROOT / "books"
OUT_DIR = ROOT / "library-site"
ASSETS_DIR = OUT_DIR / "assets"
TEMPLATES = ROOT / "templates"


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


def render_home(books: list[dict]) -> str:
    cards = []
    for book in books:
        badge = "Bitcoin / Sound Money" if "bitcoin" in book["title"].lower() or "print" in book["title"].lower() else "Economics / Theory"
        cards.append(
            f"""
<li class="book-card">
  <a href="./books/{book['slug']}/index.html" class="book-link">
    <div class="book-card-top">
      <span class="badge">{html.escape(badge)}</span>
      <span class="book-author">{html.escape(book['author'])}</span>
    </div>
    <h2 class="book-title">{html.escape(book['title'])}</h2>
    <p class="book-copy">{html.escape(book['subtitle'])}</p>
    <div class="book-meta-row">
      <span class="meta-pill">{book['chapter_count']} chapters</span>
      <span class="meta-pill">EN / KO</span>
      <span class="meta-pill">Quiz included</span>
    </div>
    <span class="book-cta">Open book →</span>
  </a>
</li>
""".strip()
        )
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bit Book Library</title>
    <link rel="stylesheet" href="./assets/styles.css" />
  </head>
  <body>
    <main class="container">
      <header class="hero">
        <p class="eyebrow">Bit Book Library</p>
        <h1>Library</h1>
      </header>
      <section class="card" id="library-grid">
        <div class="section-head">
          <h2>Available books</h2>
          <div class="view-toggle" role="group" aria-label="Library layout">
            <button class="view-btn active" data-view="card">Cards</button>
            <button class="view-btn" data-view="list">List</button>
          </div>
        </div>
        <ul class="book-grid" id="library-books">
          {"".join(cards)}
        </ul>
      </section>
    </main>
    <script>
      const list = document.getElementById("library-books");
      const viewButtons = document.querySelectorAll(".view-btn");
      const applyView = (view) => {{
        list.classList.toggle("list-mode", view === "list");
        viewButtons.forEach((btn) => btn.classList.toggle("active", btn.dataset.view === view));
        window.localStorage.setItem("bit-book-library-view", view);
      }};
      const savedView = window.localStorage.getItem("bit-book-library-view");
      if (savedView === "list" || savedView === "card") {{
        applyView(savedView);
      }}
      viewButtons.forEach((btn) => {{
        btn.addEventListener("click", () => applyView(btn.dataset.view));
      }});
    </script>
  </body>
</html>"""


def render_book_index(book: dict, chapter_entries: list[str]) -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(book['title'])}</title>
    <link rel="stylesheet" href="../../assets/styles.css" />
  </head>
  <body>
    <main class="container">
      <nav class="topnav"><a href="../../index.html">← Back to library</a></nav>
      <header class="hero">
        <p class="eyebrow">{html.escape(book['author'])}</p>
        <h1>{html.escape(book['title'])}</h1>
        <p class="subtitle">{html.escape(book['subtitle'])}</p>
      </header>
      <section class="card">
        <h2>Chapters</h2>
        <ol class="chapter-list">
          {"".join(chapter_entries)}
        </ol>
      </section>
    </main>
  </body>
</html>"""


def render_chapter_page(book: dict, chapter: dict, en_html: str, ko_html: str, quiz_en: str, quiz_ko: str) -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(chapter['title'])} · {html.escape(book['title'])}</title>
    <link rel="stylesheet" href="../../assets/styles.css" />
  </head>
  <body>
    <main class="container">
      <nav class="topnav">
        <a href="../index.html">← Back to book</a> · <a href="../../index.html">Library</a>
      </nav>
      <header class="hero compact">
        <p class="eyebrow">{html.escape(book['title'])}</p>
        <h1>{html.escape(chapter['title'])}</h1>
      </header>
      <div class="lang-toggle">
        <button class="lang-btn active" data-lang="en">English</button>
        <button class="lang-btn" data-lang="ko">한국어</button>
      </div>
      <section class="grid">
        <article class="card lang-panel active" data-lang="en">{en_html}</article>
        <article class="card lang-panel" data-lang="ko">{ko_html}</article>
      </section>
      <section class="card quiz-card">
        <h2>Quiz / 퀴즈</h2>
        <div class="quiz-panel active" data-lang="en">{quiz_en}</div>
        <div class="quiz-panel" data-lang="ko">{quiz_ko}</div>
      </section>
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


def gather_books() -> list[dict]:
    books = []
    for metadata_path in sorted(BOOKS_DIR.glob("*/source/metadata.json")):
        slug = metadata_path.parent.parent.name
        meta = json.loads(metadata_path.read_text())
        en_dir = BOOKS_DIR / slug / "content" / "en" / "chapters"
        ko_dir = BOOKS_DIR / slug / "content" / "ko" / "chapters"
        quiz_dir = BOOKS_DIR / slug / "quiz" / "chapters"
        if not en_dir.exists() or not ko_dir.exists() or not quiz_dir.exists():
            continue
        books.append(
            {
                "slug": slug,
                "title": meta.get("title", slug),
                "author": meta.get("author", "Unknown"),
                "subtitle": "Bilingual chapter digests and quizzes",
                "chapter_count": len(list(en_dir.glob("*.md"))),
            }
        )
    return books


def build() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TEMPLATES / "styles.css", ASSETS_DIR / "styles.css")
    (OUT_DIR / ".gitignore").write_text(".vercel\n")

    books = gather_books()
    (OUT_DIR / "index.html").write_text(render_home(books))

    for book in books:
        slug = book["slug"]
        en_dir = BOOKS_DIR / slug / "content" / "en" / "chapters"
        ko_dir = BOOKS_DIR / slug / "content" / "ko" / "chapters"
        quiz_dir = BOOKS_DIR / slug / "quiz" / "chapters"
        book_out = OUT_DIR / "books" / slug
        chapters_out = book_out / "chapters"
        chapters_out.mkdir(parents=True, exist_ok=True)

        chapter_entries = []
        for en_path in sorted(en_dir.glob("*.md")):
            chapter_slug = en_path.stem
            ko_path = ko_dir / en_path.name
            quiz_path = quiz_dir / f"{chapter_slug}.quiz.json"
            if not ko_path.exists() or not quiz_path.exists():
                continue
            chapter_name = chapter_title(en_path)
            chapter_entries.append(f'<li><a href="./chapters/{chapter_slug}.html">{html.escape(chapter_name)}</a></li>')

            en_html = markdown_to_html(en_path)
            ko_html = markdown_to_html(ko_path)
            quiz = json.loads(quiz_path.read_text())
            quiz_en = quiz_to_html(quiz, "en")
            quiz_ko = quiz_to_html(quiz, "ko")
            chapter_page = render_chapter_page(
                book,
                {"title": chapter_name},
                en_html,
                ko_html,
                quiz_en,
                quiz_ko,
            )
            (chapters_out / f"{chapter_slug}.html").write_text(chapter_page)

        (book_out / "index.html").write_text(render_book_index(book, chapter_entries))

    print(f"Built library site for {len(books)} books")


if __name__ == "__main__":
    build()
