#!/usr/bin/env python3
"""Build and inspect a local, non-publishing package preview.

This is a source-policy preview, NOT the output of the BigWigs packager.
"""
from pathlib import Path
import argparse
import re
import sys
import zipfile

BLOCKED = {".github", ".git", ".stormcore", "AGENTS.md", "ARCHITECTURE.md",
           ".gitignore", ".gitattributes", "tests", "Tests", "scripts", "standards",
           ".pkgmeta", ".luacheckrc", "stylua.toml", ".stylua.toml"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--output", default="/tmp/stormcore-package-preview.zip")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    toc_files = list(root.glob("*.toc"))
    if len(toc_files) != 1:
        sys.exit("Expected exactly one root .toc file for package preview")
    pkgmeta = root / ".pkgmeta"
    if not pkgmeta.exists():
        sys.exit("Missing .pkgmeta")
    meta = pkgmeta.read_text(encoding="utf-8")
    match = re.search(r"(?m)^package-as:\s*(\S+)", meta)
    package = match.group(1) if match else toc_files[0].stem
    ignore_match = re.search(r"(?ms)^ignore:\s*\n((?:[ \t]+-.*\n|[ \t]*\n)*)", meta + "\n")
    ignored = {s.strip()[1:].strip().strip("\"'").rstrip("/")
               for s in ignore_match.group(1).splitlines() if s.strip().startswith("-")} if ignore_match else set()
    files = [p for p in root.rglob("*") if p.is_file()
             and not any(part in ignored or part in BLOCKED for part in p.relative_to(root).parts)]
    out = Path(args.output)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, f"{package}/{p.relative_to(root).as_posix()}")
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
    problems = []
    for raw in toc_files[0].read_text(encoding="utf-8-sig").splitlines():
        entry = raw.strip()
        if not entry or entry.startswith("#"):
            continue
        expected = f"{package}/{entry.replace(chr(92), '/')}"
        if expected not in names:
            problems.append(f"Missing runtime file: {expected}")
    for name in names:
        parts = Path(name).parts[1:]
        if any(p in BLOCKED for p in parts):
            problems.append(f"Development file included: {name}")
    if not f"{package}/{toc_files[0].name}" in names:
        problems.append("TOC missing from package")
    print(f"PREVIEW ONLY (not BigWigs output): {out} with {len(names)} files")
    for item in names:
        print("  ", item)
    if problems:
        sys.exit("\n".join(problems))
    print("Preview ZIP policy checks passed; actual packager output remains unverified.")

if __name__ == "__main__":
    main()
