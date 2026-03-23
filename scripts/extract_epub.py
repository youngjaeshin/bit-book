#!/usr/bin/env python3
"""
Extract chapter source markdown files from an EPUB using a repo chapter map.

Usage:
  python3 scripts/extract_epub.py \
    --epub "epub/The Big Print.epub" \
    --chapter-map "books/the-big-print/source/chapter-map.json"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import zipfile
from pathlib import Path
from typing import Iterable
import xml.etree.ElementTree as ET


XHTML_NS = {"x": "http://www.w3.org/1999/xhtml"}
CONTAINER_NS = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
OPF_NS = {
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def normalize_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_inline_text(node: ET.Element) -> str:
    parts: list[str] = []
    if node.text:
        parts.append(node.text)
    for child in node:
        child_tag = strip_ns(child.tag)
        if child_tag == "br":
            parts.append("\n")
        else:
            parts.append(extract_inline_text(child))
        if child.tail:
            parts.append(child.tail)
    text = "".join(parts)
    text = text.replace("\n", " ")
    return normalize_text(text)


def iter_body_blocks(body: ET.Element) -> Iterable[str]:
    for child in body:
        tag = strip_ns(child.tag)
        if tag in {"script", "style"}:
            continue

        if tag in {"h1", "h2"}:
            text = extract_inline_text(child)
            if text:
                yield f"## {text}"
            continue

        if tag in {"h3", "h4", "h5", "h6"}:
            text = extract_inline_text(child)
            if text:
                yield f"### {text}"
            continue

        if tag == "p":
            text = extract_inline_text(child)
            if text:
                yield text
            continue

        if tag in {"ul", "ol"}:
            for li in child.findall(".//x:li", XHTML_NS):
                text = extract_inline_text(li)
                if text:
                    yield f"- {text}"
            continue

        if tag == "blockquote":
            text = extract_inline_text(child)
            if text:
                yield f"> {text}"
            continue

        if tag == "figure":
            img = child.find(".//x:img", XHTML_NS)
            alt = ""
            if img is not None:
                alt = normalize_text(img.attrib.get("alt", ""))
            if alt:
                yield f"[Figure: {alt}]"
            else:
                yield "[Figure]"
            continue

        text = extract_inline_text(child)
        if text:
            yield text


def split_ref(relative_src: str) -> tuple[str, str | None]:
    if "#" in relative_src:
        src, fragment = relative_src.split("#", 1)
        return src, fragment
    return relative_src, None


def node_contains_id(node: ET.Element, target_id: str | None) -> bool:
    if not target_id:
        return False
    if node.attrib.get("id") == target_id:
        return True
    for child in node.iter():
        if child is not node and child.attrib.get("id") == target_id:
            return True
    return False


def iter_body_blocks_between(
    body: ET.Element,
    start_fragment: str | None,
    end_fragment: str | None,
) -> Iterable[str]:
    started = start_fragment is None
    for child in body:
        if not started:
            if node_contains_id(child, start_fragment):
                started = True
            else:
                continue

        if end_fragment and node_contains_id(child, end_fragment):
            break
        tag = strip_ns(child.tag)
        if tag in {"script", "style"}:
            continue

        if tag in {"h1", "h2"}:
            text = extract_inline_text(child)
            if text:
                yield f"## {text}"
            continue

        if tag in {"h3", "h4", "h5", "h6"}:
            text = extract_inline_text(child)
            if text:
                yield f"### {text}"
            continue

        if tag == "p":
            text = extract_inline_text(child)
            if text:
                yield text
            continue

        if tag in {"ul", "ol"}:
            for li in child.findall(".//x:li", XHTML_NS):
                text = extract_inline_text(li)
                if text:
                    yield f"- {text}"
            continue

        if tag == "blockquote":
            text = extract_inline_text(child)
            if text:
                yield f"> {text}"
            continue

        if tag == "figure":
            img = child.find(".//x:img", XHTML_NS)
            alt = ""
            if img is not None:
                alt = normalize_text(img.attrib.get("alt", ""))
            if alt:
                yield f"[Figure: {alt}]"
            else:
                yield "[Figure]"
            continue

        text = extract_inline_text(child)
        if text:
            yield text


def load_opf_path(epub: zipfile.ZipFile) -> str:
    container_xml = ET.fromstring(epub.read("META-INF/container.xml"))
    rootfile = container_xml.find(".//c:rootfile", CONTAINER_NS)
    if rootfile is None:
        raise RuntimeError("Could not find OPF path in container.xml")
    return rootfile.attrib["full-path"]


def read_xhtml(epub: zipfile.ZipFile, opf_path: str, relative_src: str) -> ET.Element:
    base = os.path.dirname(opf_path)
    inner_path = os.path.normpath(os.path.join(base, relative_src.split("#", 1)[0]))
    raw = epub.read(inner_path)
    return ET.fromstring(raw)


def spine_hrefs(epub: zipfile.ZipFile, opf_path: str) -> list[str]:
    package = ET.fromstring(epub.read(opf_path))
    manifest = package.find("{*}manifest")
    spine = package.find("{*}spine")
    if manifest is None or spine is None:
        raise RuntimeError("Could not read manifest/spine from OPF")

    href_by_id: dict[str, str] = {}
    for item in manifest.findall("{*}item"):
        item_id = item.attrib.get("id")
        href = item.attrib.get("href")
        if item_id and href:
            href_by_id[item_id] = href

    ordered: list[str] = []
    base = os.path.dirname(opf_path)
    for itemref in spine.findall("{*}itemref"):
        idref = itemref.attrib.get("idref")
        href = href_by_id.get(idref or "")
        if href:
            ordered.append(os.path.normpath(os.path.join(base, href)))
    return ordered


def source_path(opf_path: str, relative_src: str) -> str:
    base = os.path.dirname(opf_path)
    return os.path.normpath(os.path.join(base, relative_src.split("#", 1)[0]))


def build_markdown(chapter: dict, blocks: list[str]) -> str:
    title = chapter["title"]
    body_blocks = blocks[:]
    if body_blocks and body_blocks[0] == f"## {title}":
        body_blocks = body_blocks[1:]

    lines = [
        f"# {title}",
        "",
        "## Source Metadata",
        "",
        f"- Chapter number: {chapter['chapter_number']}",
        f"- TOC index: {chapter['toc_index']}",
        f"- Part: {chapter['part_slug']}",
        f"- EPUB src: {chapter['src']}",
        f"- Extraction mode: {chapter.get('extraction_mode', 'single-source')}",
        "",
        "## Extracted Text",
        "",
    ]

    for block in body_blocks:
        lines.append(block)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epub", required=True)
    parser.add_argument("--chapter-map", required=True)
    args = parser.parse_args()

    epub_path = Path(args.epub)
    chapter_map_path = Path(args.chapter_map)

    chapter_map = json.loads(chapter_map_path.read_text())
    written: list[str] = []

    with zipfile.ZipFile(epub_path) as epub:
        opf_path = load_opf_path(epub)
        ordered_spine = spine_hrefs(epub, opf_path)
        for chapter in chapter_map["included_chapters"]:
            current_src_ref = chapter["src"]
            current_src, current_fragment = split_ref(current_src_ref)
            current_src = source_path(opf_path, current_src)
            next_chapter = None
            current_index = chapter_map["included_chapters"].index(chapter)
            if current_index + 1 < len(chapter_map["included_chapters"]):
                next_chapter = chapter_map["included_chapters"][current_index + 1]

            next_src = None
            next_fragment = None
            if next_chapter:
                next_src_raw, next_fragment = split_ref(next_chapter["src"])
                next_src = source_path(opf_path, next_src_raw)
            if current_src not in ordered_spine:
                raise RuntimeError(f"Source {chapter['src']} not found in spine")

            start_idx = ordered_spine.index(current_src)
            if next_src and next_src in ordered_spine:
                next_idx = ordered_spine.index(next_src)
                end_idx = next_idx if next_idx > start_idx else start_idx + 1
            else:
                end_idx = len(ordered_spine)

            candidate_docs = ordered_spine[start_idx:end_idx]
            blocks: list[str] = []
            for doc_path in candidate_docs:
                raw = epub.read(doc_path)
                root = ET.fromstring(raw)
                body = root.find(".//x:body", XHTML_NS)
                if body is None:
                    continue
                start_fragment = current_fragment if doc_path == current_src else None
                end_fragment_here = next_fragment if next_src == doc_path else None
                blocks.extend(
                    [b for b in iter_body_blocks_between(body, start_fragment, end_fragment_here) if b]
                )

            if current_fragment or next_fragment:
                chapter["extraction_mode"] = "fragment-aware-spine-range"
            else:
                chapter["extraction_mode"] = "spine-range" if len(candidate_docs) > 1 else "single-source"
            output_path = Path(chapter["source_markdown_path"])
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(build_markdown(chapter, blocks))
            written.append(str(output_path))

    print(f"Extracted {len(written)} chapters")
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
