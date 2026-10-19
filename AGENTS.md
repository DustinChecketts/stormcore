# AI development instructions

Shared guidance, not a runtime dependency. Each addon should have a short local AGENTS.md with essential rules and a link to StormCore. Do not assume agents automatically read instructions from another repository.

## Collaboration
- Use a dedicated development branch when authorized; keep main as the known-good release.
- Do not merge, tag, or publish without explicit maintainer approval. Avoid PRs during iteration unless requested.
- Report files changed, checks performed, known limitations, and focused in-game test steps.
- Prefer small, readable changes; do not refactor functioning code solely for conformity.

## Addon behavior
- Prefer Blizzard-native UI and APIs; extend before replacing, recreate only when necessary.
- Preserve SavedVariables, slash commands, and established behavior on supported clients.
- Detect capabilities where practical and isolate client-specific presentation. Forever is not Retail even if it reports WOW_PROJECT_MAINLINE.
- Treat API values from secure/secret-sensitive paths as potentially protected: verify readability before type checks, conversions, comparisons, arithmetic, string formatting, or table operations. Avoid substituting total inventory counts for individual stack counts.
- Replacing a Blizzard global function requires a documented reason, scope, and regression plan; prefer secure hooks where feasible.
- For integrations with other addons, preserve their existing presentation and test with the integration enabled and disabled.

## Quality and releases
- Check Lua 5.1 syntax and TOC references; supplement offline checks with in-game testing.
- Review TOC version, changelog, README, and supported-client claims for consistency before release.
- Exclude AGENTS.md, development documentation, tests, and GitHub infrastructure from player packages; inspect the actual ZIP.
- Follow standards/development.md, standards/compatibility.md, standards/packaging.md, and standards/release-readiness.md.
