#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def source_title(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def extracted_body(text: str) -> str:
    marker = "## Extracted Text"
    if marker in text:
        text = text.split(marker, 1)[1]
    lines = []
    for line in text.splitlines():
        raw = line
        line = line.strip()
        if not line:
            lines.append("")
            continue
        if line.startswith("## Source Metadata"):
            continue
        if line.startswith("- Chapter number:") or line.startswith("- TOC index:") or line.startswith("- Part:") or line.startswith("- EPUB src:") or line.startswith("- Extraction mode:"):
            continue
        if "................................................................" in line:
            continue
        if line.isdigit():
            continue
        if line.startswith("■ "):
            continue
        if line.startswith("| 목차 |"):
            continue
        if line.count("·") > 8:
            continue
        if line.startswith("비트코인 사용 가이드") and len(line) < 40:
            continue
        if "부록 1." in line or "부록 2." in line:
            continue
        lines.append(raw.strip())
    return "\n".join(lines).strip()


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


def chunk_source_text(text: str, max_chars: int = 6500) -> list[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for para in paras:
        para_len = len(para) + 2
        if current and current_len + para_len > max_chars:
            chunks.append("\n\n".join(current))
            current = [para]
            current_len = para_len
        else:
            current.append(para)
            current_len += para_len
    if current:
        chunks.append("\n\n".join(current))
    return chunks or [text]


def call_claude(prompt: str, timeout: int) -> str:
    result = subprocess.run(
        ["claude", "-p", prompt],
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return result.stdout.strip() + "\n"


def summarize_chunk_with_claude(lang: str, title: str, chunk: str, idx: int, total: int) -> str:
    if lang == "ko":
        prompt = (
            f"아래는 책 한 장의 일부({idx}/{total})다. 제목은 {title}.\n"
            "한국어로, 메타 문장 없이, 이 부분의 핵심 내용만 2-4개 연결형 문단으로 압축하라. "
            "금지: `이 장은`, `이 단위는`, `서두는`, 불릿, 추가 제목.\n\n"
            + chunk
        )
    else:
        prompt = (
            f"Below is part {idx}/{total} of one book section titled '{title}'.\n"
            "Write in English. Summarize only the substantive content of this part in 2-4 connected paragraphs. "
            "Do not use meta framing like 'The chapter', 'This section', bullet lists, or extra headings.\n\n"
            + chunk
        )
    return call_claude(prompt, timeout=180).strip()


def final_prompt_from_chunks(lang: str, title: str, source_chars: int, chunk_summaries: list[str]) -> str:
    combined = "\n\n".join(
        f"[Chunk {idx+1} summary]\n{summary}" for idx, summary in enumerate(chunk_summaries)
    )
    return (
        "You are rewriting a book digest in a local book-summary project.\n\n"
        f"Preferred title: {title}\n"
        f"Approximate original source length: {source_chars} characters\n\n"
        + target_instructions(lang, source_chars)
        + "\nUse these chunk summaries, preserving the author's argument flow across the whole section:\n\n"
        + combined
    )


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
        source_text = extracted_body(src_path.read_text())
        chunks = chunk_source_text(source_text, max_chars=5500 if lang == "ko" else 6500)
        if len(chunks) == 1:
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
        else:
            print(f"chunking {lang} {slug}/{chapter_id} into {len(chunks)} parts", flush=True)
            chunk_summaries = [
                summarize_chunk_with_claude(lang, title, chunk, idx + 1, len(chunks))
                for idx, chunk in enumerate(chunks)
            ]
            prompt = final_prompt_from_chunks(lang, title, len(source_text), chunk_summaries)
        rewritten = ""
        reason = "no output"
        timeout = 180 if len(source_text) < 18000 else 240
        for attempt in range(3):
            print(f"start {lang} {slug}/{chapter_id} attempt={attempt+1}", flush=True)
            candidate = call_claude(
                prompt if attempt == 0 else prompt + f"\n\nPrevious output failed validation: {reason}. Rewrite fully and obey format exactly.",
                timeout=timeout,
            )
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
