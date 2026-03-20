#!/usr/bin/env python3
"""
Unpack an EPUB into a working directory and write basic metadata.

Usage:
  python3 scripts/unpack_epub.py --epub path/to/book.epub --output books/<slug>/translated_epub/work/source
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


CONTAINER_NS = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
OPF_NS = {
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epub", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    epub_path = Path(args.epub)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Clear unpacked files but keep the directory itself.
    for child in out_dir.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    with zipfile.ZipFile(epub_path) as zf:
        zf.extractall(out_dir)
        container = ET.fromstring(zf.read("META-INF/container.xml"))
        opf_path = container.find(".//c:rootfile", CONTAINER_NS).attrib["full-path"]
        opf = ET.fromstring(zf.read(opf_path))
        title = opf.find(".//dc:title", OPF_NS)
        creator = opf.find(".//dc:creator", OPF_NS)
        language = opf.find(".//dc:language", OPF_NS)
        manifest = []
        for item in opf.findall(".//opf:manifest/opf:item", OPF_NS):
            manifest.append(item.attrib)

    meta = {
        "source_epub": str(epub_path),
        "opf_path": opf_path,
        "opf_dir": os.path.dirname(opf_path),
        "title": title.text if title is not None else None,
        "author": creator.text if creator is not None else None,
        "language": language.text if language is not None else None,
        "manifest_count": len(manifest),
    }
    (out_dir / "epub-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    print(f"Unpacked EPUB to {out_dir}")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
