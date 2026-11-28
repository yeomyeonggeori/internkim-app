"""The file an installed Mac app reads to learn whether a newer one exists.

The app asks one fixed address, the newest release's `latest.json`, and
installs what it names when the version there is above its own and the
signature matches the archive at the address beside it.
"""

import json
import re
from pathlib import Path

REPOSITORY = "yeomyeonggeori/internkim-app"
MANIFEST_NAME = "latest.json"
UPDATER_PLATFORM = "darwin-aarch64"
VERSION_PATTERN = re.compile(r"\d+\.\d+\.\d+")


class UnusableRelease(Exception):
    pass


def release_tag(version: str) -> str:
    if not VERSION_PATTERN.fullmatch(version):
        raise UnusableRelease(f"{version} is not MAJOR.MINOR.PATCH, and the updater compares versions by that grammar")
    return f"v{version}"


def asset_address(version: str, asset_name: str) -> str:
    return f"https://github.com/{REPOSITORY}/releases/download/{release_tag(version)}/{asset_name}"


def update_manifest(version: str, archive_name: str, signature: str, published_at: str) -> str:
    if not signature.strip():
        raise UnusableRelease(f"the signature of {archive_name} is empty, and an app refuses an update it cannot check")
    manifest = {
        "version": version,
        "pub_date": published_at,
        "platforms": {UPDATER_PLATFORM: {"signature": signature.strip(), "url": asset_address(version, archive_name)}},
    }
    return json.dumps(manifest, indent=2) + "\n"


def write_update_manifest(directory: Path, version: str, archive: Path, signature: Path, published_at: str) -> Path:
    manifest = directory / MANIFEST_NAME
    manifest.write_text(update_manifest(version, archive.name, signature.read_text(), published_at))
    return manifest
