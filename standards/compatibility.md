# Client compatibility policy

Priority: (1) WoW Forever, (2) Classic Anniversary, (3) Classic Era including Hardcore and seasonal variants, (4) other clients case-by-case.

- Do not break previously supported clients to add Forever support.
- Distinguish tested, expected, and unsupported compatibility in release notes.
- Prefer checking available APIs and return values to inferring features from WOW_PROJECT_ID.
- WoW Forever may report WOW_PROJECT_MAINLINE but must not be treated as Retail.
- Isolate client-specific UI presentation while sharing logic when practical.
- Keep verified API findings documented; recheck assumptions when clients patch.
- Use real in-game tests for secret values, secure behavior, and UI interactions that offline checks cannot prove.
