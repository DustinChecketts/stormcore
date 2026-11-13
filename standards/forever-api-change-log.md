# WoW Forever API and compatibility change log

Maintained as an evidence log, **not** a guarantee that an API is safe on every client build. Last researched: 2026-11-13.

## Maintenance rules

- For each finding, record **date, client build/interface, affected API or behavior, source, confidence, affected addons, and a follow-up test**.
- Labels: **Documented** = Blizzard/Warcraft Wiki patch notes; **Reported** = community/addon changelog; **Locally tested** = our own in-game diagnostics with build and context; **Unverified** = needs a new client test. A historical report is never automatically promoted to locally tested.
- On a new Forever patch, when a related addon breaks, or before implementing a sensitive API integration, review the relevant entries and rerun focused diagnostics. Do not promise continuous monitoring without a scheduled process.
- Avoid mass compatibility refactors. Apply confirmed changes only where needed; retain Classic Anniversary and Era behavior.

## Changes and findings

| Date / build | Area | Finding | Evidence / confidence | Our action |
| --- | --- | --- | --- | --- |
| 2026-09-15 / Forever beta | Architecture | Forever shares modern Mainline UI architecture and Midnight secret-value restrictions, but is a distinct game type. AuraContainer/AuraButton also apply. | Documented, [Warcraft Wiki notes](https://warcraft.wiki.gg/wiki/Patch_1.60.1/API_changes/notes), [Wowhead](https://www.wowhead.com/news/wow-forever-will-have-addon-changes-from-midnight-382921) | Use capability checks; never equate Mainline project ID with identical Retail behavior. |
| 2026-09 / 1.60.1.69893 (interface 16001) | Migration | GuildOS author reported legacy trade skill APIs absent; use C_TradeSkillUI; legacy tooltip callbacks replaced by TooltipDataProcessor and TooltipUtil; classic talent functions absent. | Reported, [GuildOS porting post](https://www.reddit.com/r/wowaddons/comments/1wm0l3v/porting_a_15kline_addon_from_anniversary_20506_to/) | Verify individually in current build before changing WideTradeSkillsPlus, tooltip addons or talent consumers. |
| 2026-09 / 1.60.1.69893 | Secrets | Author reported restricted chat payloads, unit identity and stats; readable values can change with context. | Reported, same GuildOS post; broad secret system documented above | Check readability before comparisons, indexing, formatting or arithmetic. Test grouped/combat/instance contexts. |
| 2026-09 / build 69913 | Combat log | Our earlier ForeverTest probe reported CombatLogGetCurrentEventInfo missing, whereas GuildOS author reported a compatibility shim in build 69893. | Conflicting historical reports; **unverified on current live build** | Probe actual function presence and event delivery separately; never assume either from a past report. |
| 2026-10-08 / 1.60.1.70291 | Game type and frame security | `_Forever` accepted as a TOC suffix alias; `GetFrameStrata` can return a secret value for affected frames; minimap rotation read restrictions tightened. | Documented, [Warcraft Wiki patch notes](https://warcraft.wiki.gg/wiki/Patch_1.60.1/API_changes/notes) | Avoid unguarded frame strata comparisons and minimap rotation reads. |
| 2026-10-16 / 1.60.1.70425 | GUIDs and UI | Creature/pet/game-object GUID server/spawn portions obfuscated; default player, target, pet, focus and minimap frame children reorganized. | Documented, [Warcraft Wiki patch notes](https://warcraft.wiki.gg/wiki/Patch_1.60.1/API_changes/notes) | Do not derive layer from GUIDs; recheck addon anchoring after UI patches (PetXPBarPlus, TargetHealthPlus, minimap addons). |
| 2026-11-08 / 1.60.1 | Minimap nodes | NodeSight 1.8.0 changelog says a Forever update broke its prior minimap reading technique; its new scan temporarily hides the minimap. It also reports losing reliable far-node elevation information. **Exact restricted API not established by this changelog.** | Reported, [NodeSight 1.8.1 CurseForge release notes](https://www.curseforge.com/wow/addons/node-sight/files/9506180/dependencies) | GatherIndicatorPlus: do not assume continuous minimap dot inspection is possible. First run narrow API/texture diagnostics; do not copy disruptive scan behavior without deliberate UX review. |
| 2026-11-13 / current research | SavedVariables identity | GuildOS author reported numeric realm folder and names containing spaces, while a commenter speculated that leading CRLF prevented SavedVariables loading; author disputed that interpretation. | Reported/disputed, [Reddit discussion](https://www.reddit.com/r/wowaddons/comments/1wm0l3v/porting_a_15kline_addon_from_anniversary_20506_to/) | Test stable player identity and persistence before changing Played Plus keys; **do not** add a CRLF workaround based on the thread. |

## Open verification queue

1. **GatherIndicatorPlus:** Determine what current minimap node data is actually readable, in/out of combat and while tracking changes; log exact build and failing operation. NodeSight's release notes establish breakage, **not** a specific newly secret API.
2. **PetXPBarPlus / TargetHealthPlus / TinyThreatPlus:** Verify relevant frame anchors and restricted unit values in actual gameplay contexts after October UI/security changes.
3. **WideTradeSkillsPlus and tooltip addons:** Confirm current C_TradeSkillUI and TooltipDataProcessor behavior before changing existing working implementations.
4. **Combat log and identity:** Resolve the conflicting CombatLogGetCurrentEventInfo reports, and test character/realm SavedVariables persistence.

## Reference links

- [Warcraft Wiki: Patch 1.60.1 API changes](https://warcraft.wiki.gg/wiki/Patch_1.60.1/API_changes)
- [Warcraft Wiki: dated API change notes](https://warcraft.wiki.gg/wiki/Patch_1.60.1/API_changes/notes)
- [GuildOS porting report (historical beta build)](https://www.reddit.com/r/wowaddons/comments/1wm0l3v/porting_a_15kline_addon_from_anniversary_20506_to/)
- [NodeSight CurseForge changelog](https://www.curseforge.com/wow/addons/node-sight/files/9506180/dependencies)

This file is documentation only. It does not change addon code, tests, or release packaging.
