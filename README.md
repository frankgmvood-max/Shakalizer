# Shakalizer

Shakalizer is a desktop image converter with a simple meme-based compression scale and a beginner-friendly interface.

## macOS

GitHub Actions builds native macOS application bundles and DMG installers for:

- Apple Silicon (arm64)
- Intel (x86_64)

After a successful workflow run, ready-to-use DMG files are published on the repository Releases page.

### Installation

1. Download the DMG for your Mac.
2. Open the DMG.
3. Drag **Shakalizer.app** to **Applications**.
4. Launch Shakalizer.

The current public builds use an ad-hoc signature. Because they are not yet notarized with an Apple Developer ID, macOS Gatekeeper may require **Control-click → Open** the first time on another Mac.

## Features

- JPEG, PNG and WEBP output
- exact maximum output size in KB
- transparent output for PNG / WEBP
- drag & drop
- image previews
- multi-select
- clipboard paste
- cancel processing
- Russian / English UI
- low-memory thumbnail loading
- HEIC / HEIF / AVIF, RAW, PDF and SVG decoding when supported by bundled decoders

## Build

The macOS release workflow is in:

`.github/workflows/build-macos.yml`

It reconstructs the packaged source payload, builds the app with PyInstaller on native GitHub macOS runners, creates a DMG, and publishes a release.
