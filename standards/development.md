# Development conventions

- Keep addons independently installable, lightweight, and focused. No shared runtime Lua dependency.
- Do not mandate Compat.lua or a fixed directory structure. Separate API compatibility, UI, and integrations when doing so genuinely improves clarity.
- Prefer local helpers, descriptive names, and comments for surprising API behavior, timing, or cross-addon interactions.
- Preserve SavedVariables, existing defaults, migrations, slash commands, and behavior during refactors. Initialize persistent data at a suitable lifecycle point (typically ADDON_LOADED); avoid replacing saved user choices.
- Prefer native Blizzard APIs and secure hooks. A replacement of a Blizzard global function must be justified in code or architecture notes, with documented affected clients, risks, and a targeted regression test. Do not mechanically remove proven legacy overrides.
- When integrating with another addon, preserve its normal UI and ordering; document any dependence on callback order, OnUpdate, tooltip identity, or asynchronous refresh. Test both with and without that addon.
- Develop on dedicated branches, avoid unsolicited PRs, and obtain approval before merging or publishing.
- Run Lua 5.1 syntax and TOC-reference checks in GitHub Actions. In-game validation is still required for UI, protected values, and third-party integrations.
- Do not add abstractions or rewrite stable functionality merely to pass a style preference.
