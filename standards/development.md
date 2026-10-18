# Development conventions

- Keep addons independent and focused on one purpose. No shared runtime Lua dependency is required.
- Do not mandate Compat.lua or a specific folder structure: add compatibility layers when they reduce complexity.
- Prefer local helpers, clear names, comments for non-obvious API behavior, and small targeted changes.
- Initialize SavedVariables after ADDON_LOADED; preserve existing settings and migrations.
- Develop on dedicated branches, avoid unnecessary PRs, and obtain approval before merging or releasing.
- Use GitHub Actions for automated checks; the maintainer should not need a local CLI.
- Pilot validation: Lua 5.1 syntax, TOC references, then focused in-game tests on supported clients.
- Only introduce shared reusable workflows after validating the pilot.
