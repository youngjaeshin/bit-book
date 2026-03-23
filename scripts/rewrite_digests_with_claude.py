#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def source_title(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def target_instructions(lang: str, source_chars: int) -> str:
    if source_chars < 8_000:
        para_hint = "3-4 paragraphs"
    elif source_chars < 18_000:
        para_hint = "4-5 paragraphs"
    elif source_chars < 35_000:
        para_hint = "5-7 paragraphs"
    else:
        para_hint = "7-10 paragraphs"

    if lang == "ko":
        return (
            f"출력 언어는 한국어. 요약은 {para_hint}의 연결형 문단으로 길게 쓴다. "
            "짧은 개요가 아니라 저자의 핵심 논지와 전개를 충분히 담는다. "
            "메타 문장 금지: `이 장은`, `이 단위는`, `서두는`, `장 후반부`, `저자는 여기서`, `원문 추출 기준으로 보면`. "
            "독후감/감상 금지. 내용 자체를 직접 압축 서술. "
            "절대 `## 핵심 포인트`, `## 중요 용어 / 주장`, 불릿 목록을 넣지 않는다. "
            "추출된 반복 머리말/쪽수/잡음은 버리고 실제 내용만 살린다. "
            "반드시 아래 형식만 출력:\n"
            "# <제목>\n\n## 요약\n\n<문단들>\n"
        )
    return (
        f"Write in English. Produce {para_hint} of connected prose. "
        "Preserve the author's argument flow and substantive content. "
        "Do not use meta-summary framing such as `The chapter`, `This chapter`, `The opening`, `This section`, or reader-response language. "
        "Do not add `## Key Takeaways`, `## Notable Terms / Claims`, or bullet lists. "
        "Ignore repeated headers, page junk, or extraction noise. "
        "Output only this format:\n"
        "# <Title>\n\n## Chapter Digest\n\n<paragraphs>\n"
    )


def call_claude(prompt: str) -> str:
    result = subprocess.run(
        ["claude", "-p", prompt],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() + "\n"


def is_valid_output(text: str, lang: str, source_chars: int) -> tuple[bool, str]:
    if not text.startswith("# "):
        return False, "missing title heading"
    required = "## 요약" if lang == "ko" else "## Chapter Digest"
    if required not in text:
        return False, "missing summary heading"
    banned_sections = [
        "## 핵심 포인트",
        "## 중요 용어 / 주장",
        "## Key Takeaways",
        "## Notable Terms / Claims",
    ]
    for section in banned_sections:
        if section in text:
            return False, f"contains banned section {section}"
    body = text.split(required, 1)[-1].strip()
    min_chars = max(600, int(source_chars * (0.035 if lang == "ko" else 0.05)))
    if len(body) < min_chars:
        return False, f"body too short ({len(body)} < {min_chars})"
    banned_phrases = [
        "이 장은",
        "이 단위는",
        "이 서두는",
        "서두는",
        "원문 추출 기준으로 보면",
        "The chapter",
        "This chapter",
        "The opening",
        "This section",
    ]
    for phrase in banned_phrases:
        if phrase in body:
            return False, f"contains banned phrase {phrase}"
    return True, "ok"


def rewrite_slug(slug: str, lang: str) -> None:
    root = Path("books") / slug
    src_dir = root / "source" / "chapters"
    out_dir = root / "content" / lang / "chapters"
    out_dir.mkdir(parents=True, exist_ok=True)
    for src_path in sorted(src_dir.glob("*.md")):
        chapter_id = src_path.stem
        existing_path = out_dir / f"{chapter_id}.md"
        title = source_title(existing_path if existing_path.exists() else src_path)
        source_text = src_path.read_text()
        prompt = (
            "You are rewriting a book digest in a local book-summary project.\n\n"
            f"Book slug: {slug}\n"
            f"Chapter id: {chapter_id}\n"
            f"Preferred title: {title}\n"
            f"Source length: {len(source_text)} characters\n\n"
            + target_instructions(lang, len(source_text))
            + "\nSource chapter markdown:\n\n"
            + source_text
        )
        rewritten = ""
        reason = "no output"
        for attempt in range(3):
            candidate = call_claude(prompt if attempt == 0 else prompt + f"\n\nPrevious output failed validation: {reason}. Rewrite fully and obey format exactly.")
            ok, reason = is_valid_output(candidate, lang, len(source_text))
            if ok:
                rewritten = candidate
                break
        if not rewritten:
            raise RuntimeError(f"Failed to produce valid output for {slug}/{chapter_id} ({lang}): {reason}")
        existing_path.write_text(rewritten)
        print(f"rewrote {lang} {slug}/{chapter_id}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=["ko", "en"], required=True)
    parser.add_argument("--slug", action="append", required=True)
    args = parser.parse_args()
    for slug in args.slug:
        rewrite_slug(slug, args.lang)


if __name__ == "__main__":
    main()
