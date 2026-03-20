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
        for chapter in chapter_map["included_chapters"]:
            root = read_xhtml(epub, opf_path, chapter["src"])
            body = root.find(".//x:body", XHTML_NS)
            if body is None:
                raise RuntimeError(f"No body found for {chapter['src']}")
            blocks = [b for b in iter_body_blocks(body) if b]
            output_path = Path(chapter["source_markdown_path"])
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(build_markdown(chapter, blocks))
            written.append(str(output_path))

    print(f"Extracted {len(written)} chapters")
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
