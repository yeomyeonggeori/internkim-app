"""Pack the signed Mac app into the archive an installed app updates itself from.

The updater takes a gzipped tar of the app and a signature over it, made with
the updater's own key: that signature, which the installed app checks against
the public key it was built with, is the only thing that lets a download
replace the app. Tauri would make both during the build, but this app is
built unsigned and signed afterwards, so the archive is packed here from the
signed app instead.

The app is copied out of the checkout before the checkout is removed, and it
is stapled before it is packed, so a Mac that is offline the first time the
updated app starts still finds its notarization ticket.
"""

import os
from pathlib import Path

from tauri_shipping import ShipFailure, run

UPDATER_KEY_VARIABLES = ("TAURI_SIGNING_PRIVATE_KEY_PATH", "TAURI_SIGNING_PRIVATE_KEY_PASSWORD")
ARCHIVE_SUFFIX = ".app.tar.gz"
SIGNATURE_SUFFIX = ".sig"


def refuse_a_missing_updater_key() -> None:
    missing = [name for name in UPDATER_KEY_VARIABLES if name not in os.environ]
    if missing:
        raise ShipFailure(f"set {', '.join(missing)}: the updater key signs the archive installed apps update from")


def kept_application(application: Path, scratch: Path) -> Path:
    kept = scratch / "update" / application.name
    kept.parent.mkdir(parents=True, exist_ok=True)
    run(["ditto", str(application), str(kept)], scratch)
    return kept


def archive_name(application: Path, version: str, architecture: str) -> str:
    return f"{application.stem}_{version}_{architecture}{ARCHIVE_SUFFIX}"


def signed_update_archive(application: Path, version: str, architecture: str, scratch: Path, environment: dict[str, str]) -> tuple[Path, Path]:
    run(["xcrun", "stapler", "staple", str(application)], scratch)
    archive = scratch / archive_name(application, version, architecture)
    run(["tar", "-czf", str(archive), "-C", str(application.parent), application.name], scratch, {**environment, "COPYFILE_DISABLE": "1"})
    run(["cargo", "tauri", "signer", "sign", str(archive)], scratch, environment)
    signature = archive.with_name(archive.name + SIGNATURE_SUFFIX)
    if not signature.is_file():
        raise ShipFailure(f"cargo tauri signer sign left no {signature.name} beside {archive.name}")
    return archive, signature
