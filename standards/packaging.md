# Packaging and publishing

## Goal
Developer files stay on GitHub; only installable addon files belong in player ZIPs. StormCore itself never ships as a WoW addon.

## Expected contents
- Include the TOC, runtime Lua/XML, required textures/assets, localization, and required libraries.
- Exclude AGENTS.md, ARCHITECTURE.md, standards/, internal development notes, tests/fixtures, .github/, CI scripts, and git metadata/configuration.
- README.md and CHANGELOG.md are optional in the ZIP at maintainer discretion; CHANGELOG.md may still be read by the release tool to generate release notes.

## BigWigs/CurseForge packager
- Each addon should explicitly maintain its own .pkgmeta ignore list for development-only files. A recommended starting point is below; adapt it to actual paths and the packager's documented behavior.
- Do not assume .gitignore or GitHub Actions exclusions control release ZIP contents.
- Check that manual-changelog references still work when CHANGELOG.md is excluded from the packaged payload.
- Prefer a tested explicit allowlist when the packager supports it; otherwise use a maintained exclusion list.

Example .pkgmeta fragment (adapt before use):

```yaml
ignore:
  - .github
  - .gitignore
  - .gitattributes
  - AGENTS.md
  - ARCHITECTURE.md
  - standards
  - Tests
  - tests
  - scripts
```

## Release gate
- Inspect the built ZIP's contents, not just the source tree; fail the release validation if development-only paths are present.
- Verify the TOC and all referenced runtime files are present and that the ZIP installs in the expected addon directory.
- Validate the artifact before upload where supported. If the release action publishes immediately, use a separate dry-run or staged package inspection first.
- Keep secrets in GitHub Actions secrets, never in repository files.
- Do not change existing publishing automation without a tested plan and maintainer approval.
