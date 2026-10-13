# Fitness app research materials

Materials from the onboarding/paywall research and the 23-app design audit, collected on 11–12 October 2026. This repository is the handoff package for an agent restoring screenshots and evidence references.


## Update: 13 October 2026 — recovered onboarding evidence

Start with [the change report](UPDATES-2026-10-13.md) and [the ready-to-forward agent prompt](PROMPT-FOR-AGENT.md). The handoff now contains **all 1,590 analyzed state screenshots**, **554 English questions linked to frames**, **261 icon crops**, and the **35 previously analyzed Appllama recordings**.

Use [onboarding/step-index.csv](onboarding/step-index.csv) or [the full step analysis](onboarding/steps.json) to populate screenshot fields. The 367 user-recording states and 694 Appllama video states have dedicated PNGs with local privacy masks. These supersede full-screen privacy plates for state-level screenshots. [App indexes](onboarding/README.md) begin with English question summaries.

Download [materials-v2](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/tag/materials-v2): `onboarding-recovery.zip` for screenshots and indexes, and `appllama-onboarding-videos.zip` for the 35 recordings. Extract both at the repository root. The 12 long user recordings and historical supplementary media remain in `materials-v1`.

Buddyfit's seven monetization-related states and Technogym's Plus entry are restored. Technogym's recording does not show a priced paywall. Unavailable Gravl Monthly report and unsupplied A/B concept mockups are excluded from the evidence requirements. [E040](v2-contrast-method.py) is included and reproduces E041 exactly.

## Original research reports

- [Paywall screenshots](PAYWALLS.md): 38 catalog screens, indexed by app and screen code.
- [Onboarding research — complete structured Markdown](fitness-onboarding-agent-data.md): steps, English question summaries, choices, CTAs, observations, prices, typography and color evidence, and source timestamps.
- [English onboarding questions as JSON](onboarding/questions.json).
- [Design audit — text only](fitness-audit-text-only.md), including evidence descriptions E001–E041.
- [Design audit with material references](fitness-design-audit-23-apps.md).
- [Machine-readable audit](audit-structured.json) and [evidence index](evidence-index.json).
- [Download all 12 recordings and supplementary media](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/tag/materials-v1).

## Screenshots and preserved paths

There are **1,064 Appllama catalog screenshots** and **5,234 image files overall**. Catalog screenshots are real PNG files in app folders, such as the paths listed in [PAYWALLS.md](PAYWALLS.md). Use [screens.json](manifests/screens.json) to resolve each exact screen code and app folder.

`boards/`, `frames/`, `v2-media/`, `v2-measurements/`, `16-22-media/`, `motion/` and `official-media/` retain their existing relative paths. The root contact sheets are included too. [path-map.json](manifests/path-map.json) maps old catalog paths such as `appllama/02/...jpg` to their app-folder PNG paths. References in the published audit have been updated to those PNG paths.

The 58 supplementary video files are in the release asset **supplementary-media.zip**. Extract it into the repository root to restore their original relative paths, including videos under `v2-media/`. Research images and text are already in Git. Downloader scripts, browser caches, temporary HTML and authentication data are not part of the evidence package.

## The 12 screen recordings

The two studies assigned different identifiers to the same source files. Use this table rather than assuming V01 equals U01.

| Audit | Onboarding | App | Video | Duration |
|---|---|---|---|---|
| V01 | U07 | MacroFactor | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-10-2026.15-01-54_1.mp4) | 9:14 |
| V02 | U11 | BeFit | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-10-2026.15-37-51_1.mp4) | 27:56 |
| V03 | U01 | Fitbod | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-10-2026.18-39-27_1.mp4) | 8:47 |
| V04 | U08 | Planfit | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-10-2026.22-56-29_1.mp4) | 18:08 |
| V05 | U02 | TRX | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-10-2026.23-42-23_1.mp4) | 7:18 |
| V06 | U05 | Muscle Booster | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.00-03-29_1.mp4) | 10:02 |
| V07 | U04 | SmartWorkout | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.01-19-42_1.mp4) | 12:13 |
| V08 | U06 | Gymdone | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.14-57-59_1.mp4) | 10:30 |
| V09 | U09 | iFIT | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.15-11-09_1.mp4) | 5:32 |
| V10 | U12 | Technogym | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.15-37-12_1.mp4) | 19:58 |
| V11 | U03 | Buddyfit | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.16-16-57_1.mp4) | 17:32 |
| V12 | U10 | MCI | [Download MP4](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/ScreenRecording_10-11-2026.17-46-36_1.mp4) | 21:26 |

The manifests preserve the original archive filenames. GitHub replaces spaces with dots in the release asset names; `release_filename` and `download_url` give the exact published names. Published files are **privacy-redacted copies**: account, credential, payment and unrelated personal-content sequences are covered; audio is removed. No time segments are cut. The original 1290 × 2796 dimensions and timeline are retained, so existing timestamps still apply. They are HEVC/H.265 files; use a compatible player or ffmpeg. A privacy plate is not an app screen and must not be counted as an onboarding step.

Some original audit overview frames labelled `t` were extracted at approximately `t + 1 second`; this convention remains unchanged. Exact video durations, SHA-256 checksums, download URLs and redacted time intervals are in [recordings.json](manifests/recordings.json), with a [CSV mapping](manifests/recordings.csv).

## Reading the evidence

Preserve the source distinctions in the reports: catalog metadata, observed pixels, recorded behavior, published developer documentation and inferred design properties have different evidential strength. Colors from Appllama are catalog samples, not an export of internal design tokens. Visually inferred fonts are not confirmed font families. Multiple screenshots may show alternate states rather than consecutive onboarding steps.

Privacy redactions are also applied to still images and text exports; their locations are listed in [privacy-redactions.json](manifests/privacy-redactions.json). The private source recordings and unreviewed OCR are not published. Assets remain attributable to their respective apps and source authors; this handoff does not claim ownership of third-party designs.

## Integrity

[files.json](manifests/files.json) lists file sizes and SHA-256 hashes for the image/document payload. [screens.json](manifests/screens.json) gives app names, screen IDs and catalog metadata. Supplementary video details and hashes are in `manifests/supplementary-media.json`.

Release asset integrity: [archive metadata](manifests/release-assets.json) and [SHA256SUMS.txt](https://github.com/aiuniversee112-byte/fitness-app-research-materials/releases/download/materials-v1/SHA256SUMS.txt). Supplemental copies are silent; privacy-sensitive intervals are blacked out. One fragmented App Store preview had an inconsistent duration header, which remuxing corrected; its frame count and presentation timestamps were checked against the source.
