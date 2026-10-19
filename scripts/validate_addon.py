#!/usr/bin/env python3
"""Read-only checks for WoW addon metadata, release documentation and packaging policy."""
import argparse
import re
import sys
from pathlib import Path

EXCLUDED = {".github", ".git", "AGENTS.md", "ARCHITECTURE.md", "tests", "Tests", "scripts", "standards", ".gitignore", ".gitattributes"}

def check(root: Path):
    errors, warnings = [], []
    tocs = sorted(p for p in root.glob("*.toc") if p.is_file())
    if not tocs:
        errors.append("No root-level addon .toc file")
    versions = set()
    for toc in tocs:
        metadata = {}
        for number, raw in enumerate(toc.read_text(encoding="utf-8-sig").splitlines(), 1):
            line = raw.strip()
            if not line:
                continue
            if line.startswith("##"):
                m = re.match(r"##\s*([^:]+):\s*(.*)", line)
                if m:
                    metadata[m.group(1).strip().lower()] = m.group(2).strip()
                continue
            if line.startswith("#"):
                continue
            rel = line.replace("\\", "/")
            if rel.startswith("/") or ".." in Path(rel).parts or not (toc.parent / rel).is_file():
                errors.append(f"{toc.name}:{number}: invalid/missing file {line}")
        version = metadata.get("version")
        if not version:
            errors.append(f"{toc.name}: missing ## Version")
        else:
            versions.add(version)
    if len(versions) > 1:
        errors.append(f"TOC versions disagree: {sorted(versions)}")
    version = next(iter(versions)) if len(versions) == 1 else None
    changelog = root / "CHANGELOG.md"
    if version and changelog.exists() and not re.search(r"(?m)^#{1,4}\s*(?:\\[)?(?:v)?"+re.escape(version)+r"\b", changelog.read_text(encoding="utf-8")):
        errors.append(f"CHANGELOG.md has no heading for version {version}")
    readme = root / "README.md"
    if version and readme.exists():
        text = readme.read_text(encoding="utf-8")
        mentions = re.findall(r"(?i)\bversion\s+(\d+\.\d+\.\d+)\b", text)
        if mentions and any(v != version for v in mentions):
            warnings.append(f"README version references {mentions} differ from TOC {version}; review historical vs current wording")
    architecture = root / "ARCHITECTURE.md"
    if architecture.exists():
        text = architecture.read_text(encoding="utf-8")
        for file in ("Compat.lua", "Options.lua", "Integrations.lua"):
            if (root / file).exists() and file not in text:
                warnings.append(f"ARCHITECTURE.md does not mention {file}")
    pkgmeta = root / ".pkgmeta"
    if not pkgmeta.exists():
        warnings.append("No .pkgmeta; cannot check packager exclusions")
    else:
        raw = pkgmeta.read_text(encoding="utf-8")
        m = re.search(r"(?ms)^ignore:\s*\n((?:[ \t]+-.*\n|[ \t]*\n)*)", raw+"\n")
        ignored = set(re.findall(r"(?m)^\s*-\s*['\"]?([^'\\"#\n]+)", m.group(1))) if m else set()
        ignored = {s.strip().rstrip("/") for s in ignored}
        present = {p.name for p in root.iterdir() if p.name in EXCLUDED}
        missing = sorted(present - ignored - {".git"})
        if missing:
            warnings.append(f".pkgmeta does not explicitly exclude development paths: {', '.join(missing)}")
    return errors, warnings, version

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--strict", action="store_true", help="Treat advisory warnings as failures")
    args = ap.parse_args()
    errors, warnings, version = check(Path(args.root))
    print("TOC version:", version or "unknown")
    for e in errors:
        print("ERROR:", e)
    for w in warnings:
        print("WARNING:", w)
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors or (args.strict and warnings) else 0)
