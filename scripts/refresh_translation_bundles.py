#!/usr/bin/env python3
"""
Re-export translation bundles from a fresh EPUB unpack while preserving any
existing translated_text values by bundle name + node_path.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from translate_epub_xhtml import export_bundles


def existing_translations(bundle_dir: Path) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for bundle in bundle_dir.glob("*.translation.json"):
        data = json.loads(bundle.read_text())
        out[bundle.name] = {
            entry["node_path"]: entry.get("translated_text", "")
            for entry in data["entries"]
        }
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epub", required=True)
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--bundle-dir", required=True)
    parser.add_argument("--chapter-map", action="append", required=True)
    args = parser.parse_args()

    epub = Path(args.epub)
    workdir = Path(args.workdir)
    bundle_dir = Path(args.bundle_dir)
    bundle_dir.mkdir(parents=True, exist_ok=True)
    old = existing_translations(bundle_dir)

    subprocess.run(
        ["python3", "scripts/unpack_epub.py", "--epub", str(epub), "--output", str(workdir)],
        check=True,
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for chapter_map in args.chapter_map:
            export_bundles(workdir, Path(chapter_map), tmp_dir)

        restored = 0
        total = 0
        for fresh in tmp_dir.glob("*.translation.json"):
            data = json.loads(fresh.read_text())
            old_map = old.get(fresh.name, {})
            for entry in data["entries"]:
                total += 1
                translated = old_map.get(entry["node_path"], "")
                if translated:
                    entry["translated_text"] = translated
                    restored += 1
            (bundle_dir / fresh.name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    print(f"Refreshed bundles in {bundle_dir}")
    print(f"Restored translated_text for {restored}/{total} entries")


if __name__ == "__main__":
    main()
