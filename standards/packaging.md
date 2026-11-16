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

## CurseForge release file naming

- Use `AddonName-Version.zip` for the distributable archive and `AddonName-Version` for the CurseForge file display name, for example `WideQuestLogPlus-1.2.1.zip` and `WideQuestLogPlus-1.2.1`.
- Keep Git tags in the existing `vMAJOR.MINOR.PATCH` format. Strip the leading `v` when constructing filenames and labels.
- BigWigs uses separate defaults for the archive filename and the upload label. Its `-n` argument accepts `filename-template:upload-label-template`; setting only the filename template does **not** rename the CurseForge entry.
- In each addon release workflow, derive the normalized version from the manually supplied release version or the tag name, then pass `-n "AddonName-Version:AddonName-Version"` to the pinned BigWigs packager. Use the addon's `.pkgmeta` `package-as` value or TOC basename as the canonical addon name.
- Do not rename the addon folder inside the ZIP or change the TOC filename to include a version. Verify the uploaded label and actual ZIP name on the next release.
- StormCore's `preview_package.py` is a validation preview, not the publishing tool; changing its output filename alone cannot change CurseForge file labels.
