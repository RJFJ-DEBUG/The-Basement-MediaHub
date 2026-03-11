# shared-assets

Common static assets shared across all client platforms in The-Basement-MediaHub.

## Contents

```
shared-assets/
+-- icons/          # App icons and logos
+-- images/         # Shared UI images and backgrounds
+-- audio/          # UI sounds, ambient audio clips
+-- textures/       # Shared textures (used by NEXUS Unity client)
+-- fonts/          # Shared font files
```

## Usage

Each client references assets from this directory via the `core/media-api`.
Do not store large binary files directly here — use the media-api streaming endpoint instead.

## Asset Guidelines

- Icons: PNG/SVG, 512x512 max
- Images: WebP preferred, fallback PNG
- Audio: MP3 or OGG format
- Textures: PNG or JPEG, power-of-two dimensions for Unity compatibility
- Fonts: TTF or WOFF2
