# Client compatibility policy

Priority: (1) WoW Forever, (2) Classic Anniversary, (3) Classic Era including Hardcore and seasonal variants, (4) other clients case-by-case.

- Preserve previously supported clients; distinguish tested, expected, and unsupported compatibility in release notes.
- Prefer capability checks over assumptions based on WOW_PROJECT_ID. WoW Forever must not be treated as Retail even when it reports WOW_PROJECT_MAINLINE.
- Keep client-specific presentation isolated where practical; document confirmed API findings and recheck after patches.

## Protected and secret values (especially Forever)
- Values originating from secure actions, tooltip data, frame owners, counts, or protected APIs may be secret. Do not assume values are readable merely because a function returned them.
- Verify readability with the available client mechanism before inspecting types, converting via tonumber/tostring, comparing, doing arithmetic, formatting, concatenating, or placing values in APIs that inspect them. Even a guard expression can be unsafe if it examines a secret first.
- Use defensive wrappers or safe fallbacks appropriate to the client. Do not claim that pcall alone makes every protected-value operation safe.
- Distinguish an individual bag/mail/merchant stack from a character's total inventory count. Never silently substitute a total count where a per-slot quantity is required.
- Record any verified exceptions or special cases with the tested client build and UI context.

## Testing
- Test relevant item/tooltip contexts, secure action buttons, combat, and grouped or third-party addon behavior where applicable.
- Offline Lua validation cannot establish protected-value safety; verify these paths in game.
