#!/usr/bin/env python3
"""
Repack an unpacked EPUB work directory into a .epub file.
Ensures `mimetype` is the first entry and uncompressed.
"""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    workdir = Path(args.workdir)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w") as zf:
        mimetype = workdir / "mimetype"
        if mimetype.exists():
            zf.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(workdir.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(workdir).as_posix()
            if rel == "mimetype":
                continue
            zf.write(path, rel, compress_type=zipfile.ZIP_DEFLATED)

    print(f"Repacked EPUB to {output}")


if __name__ == "__main__":
    main()
