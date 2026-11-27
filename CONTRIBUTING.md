# Contributing

Nothing lands on `main` by direct push. Branch, build what your change
touches, open a pull request, merge.

The rules for this repository are in [AGENTS.md](AGENTS.md), also read as
`CLAUDE.md`. Commit messages, pull requests, prose and code style follow
[internkim's](https://github.com/yeomyeonggeori/internkim/blob/main/AGENTS.md).

## Set up

```bash
git clone https://github.com/yeomyeonggeori/internkim-app.git
cd internkim-app
cargo install tauri-cli --version "^2" --locked
```

The Mac build needs Xcode, and the Android modules need an SDK named in
`android/local.properties`.

## Check your change

```bash
cargo tauri build --target aarch64-apple-darwin --bundles app --no-sign
cargo check --manifest-path src-tauri/Cargo.toml --target aarch64-apple-ios
android/gradlew -p android :attendance-widget:testDebugUnitTest :sender-notification:compileDebugJavaWithJavac
```

Run the ones for the platforms your diff touches. No workflow runs them after
you push, so a pull request that skipped them has not been checked.

## Branches

`<type>/<subject-in-kebab-case>`, for example `fix/widget-clock-after-midnight`.
The type is the word the commit will carry. Branch off `main` and rebase when
it moves.

## Commits

```
<type>: <what changes, imperative, lowercase, no trailing period>

<why it changes; wrap at 72 columns>
```

`type` is one of `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`.
`git config commit.template .gitmessage` installs the template.

## Pull requests

One reviewable change each. The template asks what to look at and what shows it
works. Branch names, commits, issues and pull requests are written in English.
