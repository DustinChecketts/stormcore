# StormCore

Shared development standards for independently installable World of Warcraft addons maintained by StormtrooperTK421.

StormCore provides AI guidance, development and compatibility conventions, and reusable validation. It is **not** a WoW addon, contains no shared runtime Lua, and is never installed by players.

## Principles

- Prefer Blizzard's native UI and APIs; extend rather than replace where practical.
- Prioritize WoW Forever, then Classic Anniversary and Classic Era, without regressing supported clients.
- Keep addons standalone, lightweight, and easy to maintain.
- Prefer verified API capabilities over client-family assumptions; handle secret values defensively.
- Develop on dedicated branches. Do not merge, tag, or publish without maintainer approval.
- Keep developer-only files out of distributed addon ZIPs.

## Standards

- [AI development instructions](AGENTS.md)
- [Development conventions](standards/development.md)
- [Client compatibility and protected values](standards/compatibility.md)
- [Packaging and publishing](standards/packaging.md)
- [Release readiness checklist](standards/release-readiness.md)

## Automation

The reusable GitHub Actions workflow at .github/workflows/validate-addon.yml checks Lua 5.1 syntax, TOC references, release metadata, and source-level packaging policy. It also runs StyLua and Luacheck in advisory mode by default; callers can opt into strict enforcement after reviewing their baseline. It does **not** inspect the actual BigWigs/CurseForge release ZIP yet, and it never automatically reformats addon code.

## Pilots

PetXPBarPlus has a validation integration on its stormcore-validation-pilot branch. A VendorPricePlus audit informed the protected-value, integration, documentation, and packaging standards. VendorPricePlus now has a separate stormcore-ci-trial branch with a caller workflow; no runtime addon files were changed.
