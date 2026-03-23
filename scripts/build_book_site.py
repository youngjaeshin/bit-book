#!/usr/bin/env python3
"""
Build a static bilingual HTML site for a book slug.
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
from pathlib import Path


TEMPLATES = Path("templates")


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


def chapter_nav_link(href: str, label: str, direction: str) -> str:
    arrow = "←" if direction == "prev" else "→"
    extra_class = " next" if direction == "next" else ""
    return (
        f'<a class="chapter-nav-link{extra_class}" href="{html.escape(href)}">'
        f'{arrow} {html.escape(label)}</a>'
    )


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


def build(book_slug: str, book_title: str, book_subtitle: str) -> None:
    root = Path("books") / book_slug
    en_dir = root / "content" / "en" / "chapters"
    ko_dir = root / "content" / "ko" / "chapters"
    quiz_dir = root / "quiz" / "chapters"
    site_dir = root / "site"
    site_chapters = site_dir / "chapters"
    site_assets = site_dir / "assets"

    site_dir.mkdir(parents=True, exist_ok=True)
    site_chapters.mkdir(parents=True, exist_ok=True)
    site_assets.mkdir(parents=True, exist_ok=True)
    for old_html in site_chapters.glob("*.html"):
        old_html.unlink()
    shutil.copyfile(TEMPLATES / "styles.css", site_assets / "styles.css")
    (site_dir / ".gitignore").write_text(".vercel\n")

    chapter_entries = []
    chapter_template = (TEMPLATES / "chapter.html").read_text()
    chapter_files = sorted(en_dir.glob("*.md"))
    chapter_meta: list[dict[str, str]] = []
    for en_path in chapter_files:
        slug = en_path.stem
        ko_path = ko_dir / en_path.name
        chapter_meta.append(
            {
                "slug": slug,
                "en_title": chapter_title(en_path),
                "ko_title": chapter_title(ko_path),
            }
        )

    for idx, en_path in enumerate(chapter_files):
        slug = en_path.stem
        ko_path = ko_dir / en_path.name
        quiz_path = quiz_dir / f"{slug}.quiz.json"

        en_html = markdown_to_html(en_path)
        ko_html = markdown_to_html(ko_path)
        quiz = json.loads(quiz_path.read_text())
        quiz_en_html = quiz_to_html(quiz, "en")
        quiz_ko_html = quiz_to_html(quiz, "ko")
        title_en = chapter_title(en_path)
        title_ko = chapter_title(ko_path)
        prev_link = ""
        next_link = ""
        if idx > 0:
            prev_meta = chapter_meta[idx - 1]
            prev_link = chapter_nav_link(
                f"./{prev_meta['slug']}.html", f"이전 장 · {prev_meta['ko_title']}", "prev"
            )
        if idx < len(chapter_meta) - 1:
            next_meta = chapter_meta[idx + 1]
            next_link = chapter_nav_link(
                f"./{next_meta['slug']}.html", f"다음 장 · {next_meta['ko_title']}", "next"
            )
        out_html = (
            chapter_template.replace("{{BOOK_TITLE}}", book_title)
            .replace("{{BOOK_TITLE_KO}}", book_title)
            .replace("{{BOOK_TITLE_EN}}", book_subtitle)
            .replace("{{CHAPTER_TITLE_KO}}", title_ko)
            .replace("{{CHAPTER_TITLE_EN}}", title_en)
            .replace("{{EN_HTML}}", en_html)
            .replace("{{KO_HTML}}", ko_html)
            .replace("{{QUIZ_EN_HTML}}", quiz_en_html)
            .replace("{{QUIZ_KO_HTML}}", quiz_ko_html)
            .replace("{{PREV_LINK}}", prev_link)
            .replace("{{NEXT_LINK}}", next_link)
        )
        out_path = site_chapters / f"{slug}.html"
        out_path.write_text(out_html)
        chapter_entries.append(
            f'<li><a href="./chapters/{slug}.html">{html.escape(title_ko)}</a></li>'
        )

    index_template = (TEMPLATES / "book-index.html").read_text()
    index_html = (
        index_template.replace("{{BOOK_TITLE}}", book_title)
        .replace("{{BOOK_SUBTITLE}}", book_subtitle)
        .replace("{{CHAPTER_LIST}}", "\n".join(chapter_entries))
    )
    (site_dir / "index.html").write_text(index_html)
    print(f"Built {len(chapter_entries)} chapter pages for {book_slug}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-slug", required=True)
    parser.add_argument("--book-title", required=True)
    parser.add_argument("--book-subtitle", required=True)
    args = parser.parse_args()
    build(args.book_slug, args.book_title, args.book_subtitle)


if __name__ == "__main__":
    main()
