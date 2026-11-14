# AI development instructions

Shared guidance, not a runtime dependency. Each addon should have a short local AGENTS.md with essential rules and a link to StormCore. Do not assume agents automatically read instructions from another repository.

## Mandatory research-first workflow
1. Before unfamiliar features or bug fixes, search maintained WoW addons that solve the same or similar problem. Inspect their source code and Blizzard UI implementations when relevant; document the applicable APIs, compatibility constraints, and tradeoffs. Respect licenses and credit adaptations.
2. If no proven implementation exists, consult Blizzard UI source, API documentation, and reliable technical references. Separate facts from hypotheses; use minimal read-only diagnostics and targeted in-game tests to gather evidence. Do not cycle through speculative fixes.
3. Before substantial changes, define module responsibilities and preserve clear boundaries between compatibility, data, logic, UI, events, and options where useful. Prefer existing Blizzard APIs and simple reusable helpers over duplication or needless abstractions.
4. Review code for consistency, dead code, oversized modules, performance costs, and unintended client regressions. Run applicable StormCore lint, format, syntax, TOC, and packaging checks. Clearly distinguish offline checks from in-game verification.
5. Work on dedicated branches, preserve known-good behavior, and do not open PRs during iteration, merge, tag, or publish without maintainer approval. Report evidence, changes, checks, remaining uncertainty, and exact test instructions.

Priority: correctness and compatibility > architecture and maintainability > portfolio consistency > lightweight simplicity > optional visual polish.

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
