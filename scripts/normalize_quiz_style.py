#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

from normalize_digest_style import CURATED_SLUGS, normalize_en, normalize_ko


def normalize_question_ko(text: str) -> str:
    replacements = [
        (r"^이 책의 서두는 ", ""),
        (r"^이 장은 ", ""),
        (r"^이 단위는 ", ""),
        (r"^이 서두는 ", ""),
        (r"^서두는 ", ""),
        (r"^장 후반부에는 ", ""),
        (r"^장 후반부는 ", ""),
        (r"^이 첫 단위는 ", ""),
        (r"^첫 단위는 ", ""),
        (r"^마지막 단위는 ", ""),
    ]
    for pat, repl in replacements:
        text = re.sub(pat, repl, text)
    return text


def normalize_question_en(text: str) -> str:
    replacements = [
        (r"^What does this chapter ", "What "),
        (r"^What does this unit ", "What "),
        (r"^In this chapter, what ", "What "),
        (r"^In this unit, what ", "What "),
        (r"^How does this chapter ", "How does "),
        (r"^How does this unit ", "How does "),
        (r"^Why does this chapter ", "Why does "),
        (r"^Why does this unit ", "Why does "),
        (r"^What is the role of .*? in this unit\\?", lambda m: m.group(0).replace(" in this unit", "")),
    ]
    for pat, repl in replacements:
        text = re.sub(pat, repl, text)
    return text


def process() -> None:
    root = Path("books")
    for slug in CURATED_SLUGS:
        for path in (root / slug / "quiz" / "chapters").glob("*.quiz.json"):
            data = json.loads(path.read_text())
            data["question_ko"] = normalize_question_ko(data["question_ko"])
            data["question_en"] = normalize_question_en(data["question_en"])
            data["explanation_ko"] = normalize_ko(data["explanation_ko"]).strip()
            data["explanation_en"] = normalize_en(data["explanation_en"]).strip()
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    process()
