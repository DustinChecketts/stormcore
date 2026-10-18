# Packaging and publishing

## Goal
Developer files belong in GitHub, not in player-installable ZIPs. StormCore itself is never packaged as an addon.

## Exclude from addon ZIPs
- AGENTS.md, ARCHITECTURE.md, development standards and internal notes
- .github/, CI scripts, test fixtures, .gitignore and .gitattributes
- README and CHANGELOG unless the maintainer deliberately chooses to ship them

## Include
- The addon TOC, runtime Lua and assets, and any required libraries or localization files.

## Implementation
- Prefer an explicit package file allowlist when the packager supports it.
- With BigWigs/CurseForge packager, use .pkgmeta ignore entries as appropriate; confirm its exact behavior before changing a live workflow.
- Inspect the produced ZIP before publishing; verify it installs correctly and contains no developer-only files.
- Do not modify existing release automation until the maintainer approves a tested replacement.
- Never expose publishing tokens in repository files; use GitHub Actions secrets.
