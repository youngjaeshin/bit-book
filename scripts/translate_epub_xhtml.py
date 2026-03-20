#!/usr/bin/env python3
"""
Export or apply XHTML translation bundles for an unpacked EPUB workdir.

Export mode writes per-chapter JSON bundle files containing translatable block nodes
with inline HTML placeholders preserved.

Apply mode reads the bundle files back and replaces XHTML block contents using
`translated_text` values while keeping attributes, links, anchors, and structure where possible.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET


XHTML_NS_URI = "http://www.w3.org/1999/xhtml"
XHTML_NS = {"x": XHTML_NS_URI}
TRANSLATABLE_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote", "figcaption"}


def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def node_path(elem: ET.Element, root: ET.Element) -> str:
    path: list[str] = []
    current = elem
    while current is not None and current is not root:
        parent = PARENT_MAP[id(current)]
        if parent is None:
            break
        current_tag = strip_ns(current.tag)
        siblings = [c for c in list(parent) if strip_ns(c.tag) == current_tag]
        index = siblings.index(current) + 1
        path.append(f"{current_tag}[{index}]")
        current = parent
    path.append(strip_ns(root.tag) + "[1]")
    return "/" + "/".join(reversed(path))


def build_parent_map(root: ET.Element) -> dict[int, ET.Element | None]:
    parent_map: dict[int, ET.Element | None] = {id(root): None}
    for parent in root.iter():
        for child in list(parent):
            parent_map[id(child)] = parent
    return parent_map


def find_by_path(root: ET.Element, path: str) -> ET.Element:
    segments = [seg for seg in path.split("/") if seg]
    current = root
    for seg in segments[1:]:
        tag, index = re.match(r"(.+)\[(\d+)\]$", seg).groups()
        index = int(index)
        children = [c for c in list(current) if strip_ns(c.tag) == tag]
        current = children[index - 1]
    return current


def serialize_inline(child: ET.Element) -> str:
    return ET.tostring(child, encoding="unicode")


def placeholderize_block(elem: ET.Element) -> tuple[str, dict[str, str]]:
    token_map: dict[str, str] = {}
    parts: list[str] = []
    if elem.text:
        parts.append(elem.text)
    for i, child in enumerate(list(elem), start=1):
        token = f"__INLINE_{i}__"
        token_map[token] = serialize_inline(child)
        parts.append(token)
        if child.tail:
            parts.append(child.tail)
    text = "".join(parts).strip()
    return text, token_map


def restore_placeholders(text: str, token_map: dict[str, str]) -> str:
    for token, fragment in token_map.items():
        text = text.replace(token, fragment)
    return text


def set_inner_xml(elem: ET.Element, fragment: str) -> None:
    for child in list(elem):
        elem.remove(child)
    elem.text = None
    wrapper = ET.fromstring(f'<wrapper xmlns="{XHTML_NS_URI}">{fragment}</wrapper>')
    elem.text = wrapper.text
    for child in list(wrapper):
        wrapper.remove(child)
        elem.append(child)


def load_work_meta(workdir: Path) -> dict:
    return json.loads((workdir / "epub-meta.json").read_text())


def export_bundles(workdir: Path, chapter_map_path: Path, bundle_dir: Path) -> None:
    meta = load_work_meta(workdir)
    chapter_map = json.loads(chapter_map_path.read_text())
    bundle_dir.mkdir(parents=True, exist_ok=True)
    opf_dir = meta["opf_dir"]

    for chapter in chapter_map["included_chapters"]:
        relative_src = chapter["src"].split("#", 1)[0]
        xhtml_path = workdir / opf_dir / relative_src
        root = ET.parse(xhtml_path).getroot()
        global PARENT_MAP
        PARENT_MAP = build_parent_map(root)
        body = root.find(".//x:body", XHTML_NS)
        entries = []
        for elem in body.iter():
            tag = strip_ns(elem.tag)
            if tag not in TRANSLATABLE_TAGS:
                continue
            source_text, token_map = placeholderize_block(elem)
            if not normalize_text(re.sub(r"__INLINE_\d+__", " ", source_text)):
                continue
            entries.append(
                {
                    "node_path": node_path(elem, root),
                    "tag": tag,
                    "source_text": source_text,
                    "translated_text": "",
                    "inline_tokens": token_map,
                }
            )
        bundle = {
            "chapter_id": chapter["chapter_id"],
            "title": chapter["title"],
            "src": chapter["src"],
            "xhtml_path": str(xhtml_path),
            "entries": entries,
        }
        out = bundle_dir / f"{chapter['chapter_id']}.translation.json"
        out.write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n")
        print(out)


def apply_bundles(workdir: Path, bundle_dir: Path) -> None:
    for bundle_path in sorted(bundle_dir.glob("*.translation.json")):
        bundle = json.loads(bundle_path.read_text())
        xhtml_path = Path(bundle["xhtml_path"])
        root = ET.parse(xhtml_path).getroot()
        for entry in bundle["entries"]:
            translated = entry.get("translated_text", "").strip()
            if not translated:
                continue
            elem = find_by_path(root, entry["node_path"])
            restored = restore_placeholders(translated, entry.get("inline_tokens", {}))
            set_inner_xml(elem, restored)
        ET.ElementTree(root).write(xhtml_path, encoding="utf-8", xml_declaration=True)
        print(f"Applied translations to {xhtml_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    export_parser = sub.add_parser("export")
    export_parser.add_argument("--workdir", required=True)
    export_parser.add_argument("--chapter-map", required=True)
    export_parser.add_argument("--bundle-dir", required=True)

    apply_parser = sub.add_parser("apply")
    apply_parser.add_argument("--workdir", required=True)
    apply_parser.add_argument("--bundle-dir", required=True)

    args = parser.parse_args()

    if args.command == "export":
        export_bundles(Path(args.workdir), Path(args.chapter_map), Path(args.bundle_dir))
    else:
        apply_bundles(Path(args.workdir), Path(args.bundle_dir))


if __name__ == "__main__":
    PARENT_MAP: dict[int, ET.Element | None] = {}
    main()
