#!/usr/bin/env python3
"""
Build a static HTML site for The Big Print digests and quizzes.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path


BOOK_TITLE = "The Big Print"
BOOK_SUBTITLE = "Bilingual chapter digests and chapter quizzes"
ROOT = Path("books/the-big-print")
EN_DIR = ROOT / "content" / "en" / "chapters"
KO_DIR = ROOT / "content" / "ko" / "chapters"
QUIZ_DIR = ROOT / "quiz" / "chapters"
SITE_DIR = ROOT / "site"
SITE_CHAPTERS = SITE_DIR / "chapters"
SITE_ASSETS = SITE_DIR / "assets"
TEMPLATES = Path("templates")


def parse_markdown(path: Path) -> list[tuple[str, object]]:
    lines = path.read_text().splitlines()
    out: list[tuple[str, object]] = []
    paragraph: list[str] = []
    bullets: list[str] = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            out.append(("p", " ".join(paragraph).strip()))
            paragraph = []

    def flush_bullets():
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


def quiz_to_html(quiz: dict) -> str:
    options = []
    for idx, (en, ko) in enumerate(zip(quiz["choices_en"], quiz["choices_ko"])):
        label = f"{html.escape(en)} / {html.escape(ko)}"
        options.append(
            f'<button class="quiz-option" data-option-index="{idx}">{label}</button>'
        )
    result = html.escape(
        f"Answer: {quiz['choices_en'][quiz['answer_index']]} / {quiz['choices_ko'][quiz['answer_index']]} — {quiz['explanation_en']} / {quiz['explanation_ko']}"
    )
    return f"""
<div class="quiz-box" data-answer-index="{quiz['answer_index']}"
     data-correct-text="{result}"
     data-wrong-text="{result}">
  <h3>{html.escape(quiz['question_en'])}</h3>
  <p>{html.escape(quiz['question_ko'])}</p>
  <div class="quiz-options">
    {''.join(options)}
  </div>
  <div class="quiz-result" hidden></div>
</div>
""".strip()


def build() -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    SITE_CHAPTERS.mkdir(parents=True, exist_ok=True)
    SITE_ASSETS.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TEMPLATES / "styles.css", SITE_ASSETS / "styles.css")

    chapter_entries = []
    chapter_template = (TEMPLATES / "chapter.html").read_text()

    for en_path in sorted(EN_DIR.glob("*.md")):
        slug = en_path.stem
        ko_path = KO_DIR / en_path.name
        quiz_path = QUIZ_DIR / f"{slug}.quiz.json"

        en_html = markdown_to_html(en_path)
        ko_html = markdown_to_html(ko_path)
        quiz_html = quiz_to_html(json.loads(quiz_path.read_text()))
        title = chapter_title(en_path)
        out_html = (
            chapter_template.replace("{{BOOK_TITLE}}", BOOK_TITLE)
            .replace("{{CHAPTER_TITLE}}", title)
            .replace("{{EN_HTML}}", en_html)
            .replace("{{KO_HTML}}", ko_html)
            .replace("{{QUIZ_HTML}}", quiz_html)
        )
        out_path = SITE_CHAPTERS / f"{slug}.html"
        out_path.write_text(out_html)
        chapter_entries.append(
            f'<li><a href="./chapters/{slug}.html">{html.escape(title)}</a></li>'
        )

    index_template = (TEMPLATES / "book-index.html").read_text()
    index_html = (
        index_template.replace("{{BOOK_TITLE}}", BOOK_TITLE)
        .replace("{{BOOK_SUBTITLE}}", BOOK_SUBTITLE)
        .replace("{{CHAPTER_LIST}}", "\n".join(chapter_entries))
    )
    (SITE_DIR / "index.html").write_text(index_html)

    print(f"Built {len(chapter_entries)} chapter pages")


if __name__ == "__main__":
    build()
