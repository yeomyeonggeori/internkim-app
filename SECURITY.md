# Security policy

## Reporting a vulnerability

Report it privately through GitHub: open the repository's "Security" tab and
choose "Report a vulnerability", or go to
<https://github.com/yeomyeonggeori/internkim-app/security/advisories/new>.
Do not open a public issue, pull request or discussion for it.

Say what you found, the steps that reproduce it, and what an attacker gains.
A report with a working reproduction is triaged first. You will get an
acknowledgment, and a fix is coordinated with you before anything is disclosed.

## In scope

- A native command the shell exposes to a page it should not trust: a
  capability under `src-tauri/capabilities` that admits an origin other than
  the company web app.
- A plugin reading or writing outside what its permission states: files,
  photos, notifications, or control of the desktop.
- Credential exposure: a session, a push token or a signing secret reaching a
  log, a bundle or a published release.

## Out of scope

- Findings that need a device or account the attacker already controls.
- The web app, the public API and the company host. Report those to
  [internkim](https://github.com/yeomyeonggeori/internkim/security/advisories/new).
- Issues in a dependency with no path to this product. Report those upstream.
