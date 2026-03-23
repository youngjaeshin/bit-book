#!/usr/bin/env python3
"""
Update nav/ncx/metadata titles in an unpacked EPUB workdir using translated bundle files.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET


CONTAINER_NS = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
OPF_NS = {
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
}
XHTML_NS = {"x": "http://www.w3.org/1999/xhtml", "epub": "http://www.idpf.org/2007/ops"}
XHTML_NS_URI = "http://www.w3.org/1999/xhtml"
EPUB_NS_URI = "http://www.idpf.org/2007/ops"


def load_work_meta(workdir: Path) -> dict:
    return json.loads((workdir / "epub-meta.json").read_text())


def translated_title(bundle_path: Path) -> str | None:
    bundle = json.loads(bundle_path.read_text())
    for entry in bundle["entries"]:
        if entry["tag"] in {"h1", "h2"} and entry.get("translated_text", "").strip():
            title = re.sub(r"__INLINE_\d+__", " ", entry["translated_text"]).strip()
            title = re.sub(r"\s+", " ", title)
            return title
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--bundle-dir", required=True)
    parser.add_argument("--book-title-ko")
    parser.add_argument("--book-title")
    parser.add_argument("--language", default="ko")
    parser.add_argument("--identifier")
    args = parser.parse_args()

    workdir = Path(args.workdir)
    bundle_dir = Path(args.bundle_dir)
    meta = load_work_meta(workdir)
    opf_path = workdir / meta["opf_path"]
    opf_dir = opf_path.parent

    bundle_titles: dict[str, str] = {}
    for bundle in bundle_dir.glob("*.translation.json"):
        data = json.loads(bundle.read_text())
        title = translated_title(bundle)
        if title:
            src = data["src"].split("#", 1)[0]
            bundle_titles[src] = title

    tree = ET.parse(opf_path)
    root = tree.getroot()

    if args.book_title:
        dc_title = root.find(".//dc:title", OPF_NS)
        if dc_title is not None:
            dc_title.text = args.book_title

    dc_language = root.find(".//dc:language", OPF_NS)
    if dc_language is not None:
        dc_language.text = args.language

    if args.identifier:
        dc_identifier = root.find(".//dc:identifier", OPF_NS)
        if dc_identifier is not None:
            dc_identifier.text = args.identifier

    manifest = {item.attrib.get("id"): item.attrib for item in root.findall(".//opf:manifest/opf:item", OPF_NS)}

    nav_href = None
    ncx_href = None
    for attrs in manifest.values():
        if "nav" in attrs.get("properties", "").split():
            nav_href = attrs.get("href")
        if attrs.get("media-type") == "application/x-dtbncx+xml":
            ncx_href = attrs.get("href")

    if nav_href:
        nav_path = opf_dir / nav_href
        ET.register_namespace("", XHTML_NS_URI)
        ET.register_namespace("epub", EPUB_NS_URI)
        nav_tree = ET.parse(nav_path)
        nav_root = nav_tree.getroot()
        nav_root.set("{http://www.w3.org/XML/1998/namespace}lang", "ko")
        nav_root.set("lang", "ko")
        for a in nav_root.findall(".//x:a", XHTML_NS):
            href = a.attrib.get("href", "").split("#", 1)[0]
            if href in bundle_titles:
                a.text = bundle_titles[href]
        nav_tree.write(nav_path, encoding="utf-8", xml_declaration=True)

    if ncx_href:
        ncx_path = opf_dir / ncx_href
        ncx_tree = ET.parse(ncx_path)
        ncx_root = ncx_tree.getroot()
        if args.identifier:
            for meta in ncx_root.findall(".//{*}meta"):
                if meta.attrib.get("name") == "dtb:uid":
                    meta.set("content", args.identifier)
        for nav_point in ncx_root.findall(".//{*}navPoint"):
            content = nav_point.find(".//{*}content")
            label = nav_point.find(".//{*}text")
            if content is None or label is None:
                continue
            href = content.attrib.get("src", "").split("#", 1)[0]
            if href in bundle_titles:
                label.text = bundle_titles[href]
        ncx_tree.write(ncx_path, encoding="utf-8", xml_declaration=True)

    tree.write(opf_path, encoding="utf-8", xml_declaration=True)
    print(f"Localized TOC/title data using {len(bundle_titles)} translated chapter titles")


if __name__ == "__main__":
    main()
