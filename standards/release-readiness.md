# Release readiness checklist

Apply proportionately to each addon. A simple addon should not need a complex release process.

## Source and documentation
- [ ] Lua 5.1 syntax and TOC file-reference checks pass.
- [ ] TOC Version matches the intended release tag/version.
- [ ] CHANGELOG.md describes user-visible changes and compatibility findings.
- [ ] README.md describes current behavior and terminology, not an older release.
- [ ] ARCHITECTURE.md, if present, accurately lists important file responsibilities.
- [ ] Client compatibility claims distinguish tested from untested clients.
- [ ] No unexpected changes to SavedVariables, defaults, or slash commands.

## In-game regression
- [ ] Verify changed behavior on the target client; check older supported clients when affected.
- [ ] For Forever, test secret/protected-value paths, including secure action-bar and tooltip contexts where relevant.
- [ ] For third-party integrations, test with and without the other addon; check duplicate rows, ordering, and stale tooltip data.
- [ ] If Blizzard globals are overridden, confirm documented justification and regression coverage.

## Package and approval
- [ ] Inspect a built ZIP for required runtime files and absence of development-only files.
- [ ] Confirm CurseForge metadata and release notes are appropriate.
- [ ] Obtain maintainer approval before merging, tagging, or publishing.
