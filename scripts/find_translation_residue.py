#!/usr/bin/env python3
"""
Detect suspicious English residue in translation bundles and/or translated XHTML.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TOKEN_RE = re.compile(r"__INLINE_\d+__")
ENGLISH_RUN_RE = re.compile(r"[A-Za-z][A-Za-z'\",;:()\-]+(?:\s+[A-Za-z][A-Za-z'\",;:()\-]+){3,}")

ALLOW_SUBSTRINGS = {
    "Bitcoin",
    "FRED",
    "MMT",
    "Fed",
    "Amazon",
    "Max Keiser",
    "Ludwig von Mises",
    "Carl Menger",
    "Hans-Hermann Hoppe",
    "Murray Rothbard",
    "Larry Summers",
    "Hank Paulson",
    "Tim Geithner",
    "Princeton",
    "Harvard",
    "MIT",
    "Goldman Sachs",
    "Morgan Stanley",
    "Lehman Brothers",
    "Merrill Lynch",
    "Fannie Mae",
    "Freddie Mac",
}


def suspicious_runs(text: str) -> list[str]:
    text = TOKEN_RE.sub(" ", text)
    found = []
    for match in ENGLISH_RUN_RE.findall(text):
        cleaned = re.sub(r"\s+", " ", match).strip()
        if any(allowed in cleaned for allowed in ALLOW_SUBSTRINGS):
            continue
        found.append(cleaned)
    return found


def scan_bundles(bundle_dir: Path) -> list[dict]:
    findings = []
    for bundle in sorted(bundle_dir.glob("*.translation.json")):
        data = json.loads(bundle.read_text())
        for index, entry in enumerate(data.get("entries", [])):
            translated = entry.get("translated_text", "")
            runs = suspicious_runs(translated)
            if not runs:
                continue
            findings.append(
                {
                    "kind": "bundle",
                    "file": str(bundle),
                    "chapter_id": data.get("chapter_id"),
                    "entry_index": index,
                    "node_path": entry.get("node_path"),
                    "tag": entry.get("tag"),
                    "matches": runs,
                    "excerpt": translated[:400],
                }
            )
    return findings


def scan_xhtml(xhtml_dir: Path) -> list[dict]:
    findings = []
    for path in sorted(xhtml_dir.glob("*.xhtml")):
        text = path.read_text()
        runs = suspicious_runs(text)
        if not runs:
            continue
        findings.append(
            {
                "kind": "xhtml",
                "file": str(path),
                "matches": runs[:20],
                "excerpt": text[:800],
            }
        )
    return findings


def write_markdown(report_path: Path, findings: list[dict]) -> None:
    lines = ["# Translation residue report", "", f"- Findings: {len(findings)}", ""]
    for finding in findings:
        lines.append(f"## {finding['kind']} — {finding['file']}")
        if finding.get("chapter_id"):
            lines.append(f"- chapter_id: `{finding['chapter_id']}`")
        if finding.get("entry_index") is not None:
            lines.append(f"- entry_index: `{finding['entry_index']}`")
        if finding.get("node_path"):
            lines.append(f"- node_path: `{finding['node_path']}`")
        if finding.get("tag"):
            lines.append(f"- tag: `{finding['tag']}`")
        lines.append("- matches:")
        for match in finding["matches"][:10]:
            lines.append(f"  - {match}")
        lines.append("")
        lines.append("```text")
        lines.append(finding["excerpt"])
        lines.append("```")
        lines.append("")
    report_path.write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle-dir")
    parser.add_argument("--xhtml-dir")
    parser.add_argument("--report-json", required=True)
    parser.add_argument("--report-md", required=True)
    args = parser.parse_args()

    findings = []
    if args.bundle_dir:
        findings.extend(scan_bundles(Path(args.bundle_dir)))
    if args.xhtml_dir:
        findings.extend(scan_xhtml(Path(args.xhtml_dir)))

    Path(args.report_json).write_text(json.dumps(findings, ensure_ascii=False, indent=2) + "\n")
    write_markdown(Path(args.report_md), findings)
    print(f"Findings: {len(findings)}")
    print(f"JSON: {args.report_json}")
    print(f"Markdown: {args.report_md}")


if __name__ == "__main__":
    main()
