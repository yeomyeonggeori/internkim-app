# internkim-app

The internkim apps for iOS, Android, macOS, Windows and Linux. Each is a Tauri
shell around the web app at `https://intern.kim`, so the screens come from
[internkim](https://github.com/yeomyeonggeori/internkim) and this repository
holds what runs on the device: the shell, its native plugins, the widgets and
the tools that build and sign a release.

## Layout

| path | holds |
| --- | --- |
| `src-tauri/` | the Tauri project, its plugins, and the generated Xcode and Gradle projects under `gen/` |
| `app-shell/` | the page the shell shows before the web app loads |
| `attendance-widget/` | the attendance widget, as a Tauri plugin and an Android module |
| `sender-notification/` | Android notification code |
| `android/` | the Gradle root the Android modules build under |
| `tools/` | `ship-tauri-ios` and `ship-tauri-macos`, and what they call |

## Building

```bash
cargo tauri build --target aarch64-apple-darwin --bundles app --no-sign
android/gradlew -p android :attendance-widget:testDebugUnitTest :sender-notification:compileDebugJavaWithJavac
```

The Mac build bundles two programs that `tools/prepare-agent-desktop` places
first. `tools/ship-tauri-ios --help` and `tools/ship-tauri-macos --help` say
what a signed release needs.

## Files shared with internkim

`internal/desktop/commands.json`, `assets/internkim.square.png` and
`tests/fixtures/attendance-today-cases.json` are copies. internkim owns them
and carries the test that fails when a copy here differs.
