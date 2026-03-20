#!/usr/bin/env python3
"""
Lightweight EPUB validator for structure and key references.
"""

from __future__ import annotations

import argparse
import os
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


CONTAINER_NS = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
OPF_NS = {"opf": "http://www.idpf.org/2007/opf"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epub", required=True)
    args = parser.parse_args()

    epub_path = Path(args.epub)
    with zipfile.ZipFile(epub_path) as zf:
        names = zf.namelist()
        assert names[0] == "mimetype", "mimetype must be the first zip entry"
        assert "META-INF/container.xml" in names, "Missing META-INF/container.xml"
        container = ET.fromstring(zf.read("META-INF/container.xml"))
        opf_path = container.find(".//c:rootfile", CONTAINER_NS).attrib["full-path"]
        assert opf_path in names, f"Missing OPF file: {opf_path}"
        opf = ET.fromstring(zf.read(opf_path))
        base = os.path.dirname(opf_path)
        for item in opf.findall(".//opf:manifest/opf:item", OPF_NS):
            href = item.attrib.get("href")
            if not href:
                continue
            target = os.path.normpath(os.path.join(base, href))
            assert target in names, f"Manifest href missing: {target}"

    print(f"Validation passed: {epub_path}")


if __name__ == "__main__":
    main()
