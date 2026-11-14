"""Regression tests for addon version metadata validation."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_addon.py"
spec = importlib.util.spec_from_file_location("validate_addon", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class VersionValidationTests(unittest.TestCase):
    def validate(self, toc_version, changelog_version="1.2.0"):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Addon.lua").write_text("-- addon\n", encoding="utf-8")
            (root / "Addon.toc").write_text(
                "## Interface: 16001\n## Title: Addon\n"
                f"## Version: {toc_version}\nAddon.lua\n", encoding="utf-8"
            )
            (root / "CHANGELOG.md").write_text(
                f"# Changelog\n\n## {changelog_version} — release\n", encoding="utf-8"
            )
            (root / "README.md").write_text(
                "Release version 1.2.0; VoiceOver integration added in version 1.0.12.\n",
                encoding="utf-8"
            )
            return validator.check(root)

    def test_bigwigs_placeholder_accepts_release_changelog(self):
        errors, warnings, version = self.validate("@project-version@")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(version, "@project-version@")

    def test_literal_version_still_requires_matching_changelog(self):
        errors, _, _ = self.validate("1.3.0")
        self.assertTrue(any("CHANGELOG.md has no heading" in e for e in errors))

    def test_literal_version_still_reports_readme_mismatch(self):
        _, warnings, _ = self.validate("1.2.0")
        self.assertTrue(any("README version references" in w for w in warnings))

    def test_missing_toc_version_still_fails(self):
        errors, _, _ = self.validate("")
        self.assertTrue(any("missing ## Version" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
