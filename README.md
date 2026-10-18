# StormCore

Shared development standards for independently installable World of Warcraft addons maintained by StormtrooperTK421.

StormCore contains development guidance and, eventually, reusable GitHub validation and release workflows. It is **not** a WoW addon, ships no runtime Lua, and is never installed by players.

## Principles

- Prefer Blizzard's native UI and APIs; extend rather than replace them where practical.
- Prioritize WoW Forever, then Classic Anniversary and Classic Era; preserve tested behavior on every supported client.
- Keep addons independent, lightweight, readable, and straightforward to maintain.
- Prefer capability checks over assumptions based on client family.
- Work on dedicated development branches; do not merge, tag, or publish addon releases without the maintainer's approval.
- Keep developer-only files out of distributed addon ZIPs.

See AGENTS.md for AI collaboration rules and standards/ for compatibility, development, and packaging guidance.

## Pilot

PetXPBarPlus is the initial pilot. StormCore's first phase documents conventions; it does not alter PetXPBarPlus or its publishing workflow.
