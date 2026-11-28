# AGENTS.md

This file is for repository-specific behavior that an agent cannot infer from
the codebase. Keep it short, concrete, and updated when workflows change.

## Core Rules

- This repository builds the apps a person installs. The screens they show
  come from the web app in
  [internkim](https://github.com/yeomyeonggeori/internkim), loaded from
  `https://intern.kim`. A change to a screen belongs there.
- Branch names, commit messages, pull requests, prose and code style follow
  internkim's `AGENTS.md`. Read it there; nothing here repeats it.
- Nothing lands on `main` by direct push. `CONTRIBUTING.md` lists the builds
  that check a change.
- Do not revert user or generated changes unless explicitly asked.
- No secret belongs in a tracked file: signing certificates, provisioning
  profiles and App Store Connect keys stay in the vault.

## What must not change

- The app is one app to Apple and Google only while its identity holds: the
  identifier `app.intern.kim` in `src-tauri/tauri.conf.json`, the Apple team,
  and the signing certificates. Changing any of them makes a different app,
  and installed copies stop updating.
- An iOS build number is higher than every one uploaded before it.

## Files copied from internkim

- `internal/desktop/commands.json`, `assets/internkim.square.png` and
  `tests/fixtures/attendance-today-cases.json` are owned by internkim. Change
  them there first, then copy the file here. internkim's
  `web/tests/conventions/native-shell/app-repository-copies.test.ts` fails
  while the two differ.
- internkim reads this repository as the submodule `.dependency/internkim-app`
  and holds its web code to several files here by test. Moving or renaming a
  file under `src-tauri/plugins`, `src-tauri/gen` or `sender-notification` can
  break those tests, so run internkim's `tools/verify` with the pointer moved.

## Shipping

- `tools/ship-tauri-ios` and `tools/ship-tauri-macos` build from a commit,
  `origin/main` unless `--ref` names another, in a throwaway checkout. Their
  `--help` says what each needs.
