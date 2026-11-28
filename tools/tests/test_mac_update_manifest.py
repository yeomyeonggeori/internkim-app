import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mac_update_manifest import UnusableRelease, release_tag, update_manifest

ARCHIVE = "internkim_1.2.3_aarch64.app.tar.gz"


class UpdateManifestTests(unittest.TestCase):
    def test_names_the_version_and_where_its_archive_is_downloaded(self):
        manifest = json.loads(update_manifest("1.2.3", ARCHIVE, "c2lnbmF0dXJl\n", "2026-11-28T09:00:00Z"))
        self.assertEqual(manifest["version"], "1.2.3")
        self.assertEqual(manifest["pub_date"], "2026-11-28T09:00:00Z")
        self.assertEqual(
            manifest["platforms"]["darwin-aarch64"],
            {
                "signature": "c2lnbmF0dXJl",
                "url": f"https://github.com/yeomyeonggeori/internkim-app/releases/download/v1.2.3/{ARCHIVE}",
            },
        )

    def test_refuses_an_archive_nobody_signed(self):
        with self.assertRaises(UnusableRelease):
            update_manifest("1.2.3", ARCHIVE, " \n", "2026-11-28T09:00:00Z")

    def test_refuses_a_version_the_updater_cannot_compare(self):
        for version in ["1.2", "v1.2.3", "1.2.3-beta", ""]:
            with self.assertRaises(UnusableRelease):
                release_tag(version)


if __name__ == "__main__":
    unittest.main()
