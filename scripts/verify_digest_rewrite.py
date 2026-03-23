#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


SLUGS = [
    "bitcoin-for-everyone",
    "blind-robbery",
    "the-bitcoin-standard",
    "21-lessons",
    "the-fiat-standard",
    "the-bullish-case-for-bitcoin",
    "layered-money",
    "bitcoin-diploma",
    "bitcoin-whitepaper-guide",
    "bitcoin-user-guide",
    "the-blocksize-war",
    "bitcoin-handbook",
]

BANNED = [
    r"이 장은",
    r"이 단위는",
    r"이 서두는",
    r"서두는",
    r"장 후반부",
    r"The chapter",
    r"This chapter",
    r"The opening",
    r"This section",
]

EXTRA_SECTIONS = [
    "## 핵심 포인트",
    "## 중요 용어 / 주장",
    "## Key Takeaways",
    "## Notable Terms / Claims",
]


def main() -> None:
    all_ok = True
    for slug in SLUGS:
        root = Path("books") / slug
        src_dir = root / "source" / "chapters"
        ko_dir = root / "content" / "ko" / "chapters"
        en_dir = root / "content" / "en" / "chapters"
        src_total = sum(len(p.read_text()) for p in src_dir.glob("*.md"))
        ko_total = sum(len(p.read_text()) for p in ko_dir.glob("*.md"))
        en_total = sum(len(p.read_text()) for p in en_dir.glob("*.md"))
        ko_text = "\n".join(p.read_text() for p in ko_dir.glob("*.md"))
        en_text = "\n".join(p.read_text() for p in en_dir.glob("*.md"))
        bad = [pat for pat in BANNED if re.search(pat, ko_text) or re.search(pat, en_text)]
        extras = [sec for sec in EXTRA_SECTIONS if sec in ko_text or sec in en_text]
        ko_ratio = round(ko_total / src_total, 3) if src_total else 0
        en_ratio = round(en_total / src_total, 3) if src_total else 0
        ok = not bad and not extras
        all_ok &= ok
        print(
            f"{slug}: ok={ok} ko_ratio={ko_ratio} en_ratio={en_ratio}"
            + (f" banned={bad}" if bad else "")
            + (f" extra_sections={extras}" if extras else "")
        )
    print(f"ALL_OK={all_ok}")


if __name__ == "__main__":
    main()
