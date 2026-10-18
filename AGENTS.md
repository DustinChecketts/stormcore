# AI development instructions

These are shared guidelines, not a runtime dependency. Individual addon repositories should retain a short local AGENTS.md containing essential rules and a link to StormCore; do not assume AI tooling automatically reads another repository.

## Collaboration
- Work autonomously on a dedicated branch when authorized; keep main as the known-good release.
- Never merge to main, create release tags, or publish to CurseForge without explicit maintainer approval.
- Avoid opening pull requests during active iteration unless requested.
- Report changed files, rationale, checks performed, and focused in-game test steps.
- Prefer simple, readable Lua and minimal changes over speculative abstraction.

## Addon behavior
- Preserve Blizzard-native appearance and interaction where practical.
- Extend Blizzard frames rather than replace them; faithfully recreate only when required.
- Protect SavedVariables, slash commands, and behavior on previously supported clients.
- Use capability checks for differing APIs; isolate genuinely client-specific presentation.
- Treat WoW Forever as its own client; do not infer Retail compatibility from WOW_PROJECT_MAINLINE.

## Quality
- Check Lua 5.1 syntax and TOC file references before handing off changes.
- Treat offline checks as supplements, not substitutes, for in-game tests.
- Never bundle AGENTS.md, development documentation, tests, or GitHub infrastructure into player packages.
- Follow standards/development.md, standards/compatibility.md, and standards/packaging.md.
