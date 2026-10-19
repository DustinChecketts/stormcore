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

## Risk-based RC sign-off

The checklist is a decision aid, not a requirement for 100% test coverage.

- Identify the exact candidate commit/branch, intended version, and supported client targets.
- Record which checks and in-game scenarios were actually tested; do not label untested clients or paths as verified.
- Record known failures, remaining untested scenarios, and their likely user impact.
- The maintainer may explicitly approve a release with incomplete coverage when remaining risks are understood and acceptable. Never represent this as a full regression pass.
- Once an RC is accepted, freeze scope: avoid unrelated cleanup, architecture refactors, or feature additions. Re-run relevant tests for any narrowly scoped fix after sign-off.
- Capture deferred tests and known issues as post-release follow-ups; do not silently discard them.
- Approval of an RC is not authorization for an agent to merge, tag, or publish unless the maintainer explicitly authorizes those actions.

## Publishing provenance

- Before publishing, verify that the intended branch/ref exists and identify its exact commit SHA. Do not infer that a conversational branch name exists on GitHub.
- Ensure the packaged artifact and release tag derive from the approved commit, and that the TOC and release notes agree on the version.
- If the source ref cannot be verified, stop before publishing and ask for the correct ref.

## Engineering gates versus manual testing

- Mandatory automated engineering gates (when implemented): consistent Lua formatting, Lua 5.1 parsing, TOC references, static checks with reviewed exceptions, version/documentation consistency, and artifact-content validation. A documented standard is not proof that automation is already enforced.
- Manual testing is representative and risk-based, not an exhaustive cross-product of clients, settings, tooltip contexts, and third-party addons. Prioritize changed paths, high-impact regressions, secure/secret-sensitive behavior, and a few common combinations.
- Maintain a concise test matrix with tested, not tested, and known failing scenarios. Do not turn a maintainer's finite testing time into an arbitrary percentage-coverage gate.
- User-reported issues are a normal part of the feedback loop. Triage and reproduce reports, fix on a branch, and add an automated or focused manual regression case when feasible.
- Reliability goals such as 'works for 98% of users' are aspirations, not measured claims without supporting telemetry.
- Do not weaken formatting, static analysis, syntax, packaging, or release-integrity requirements merely because manual coverage is incomplete.
