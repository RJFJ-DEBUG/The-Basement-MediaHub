# Documentation

This directory contains all project documentation for The-Basement-MediaHub.

## Documents

| File | Description |
|------|-------------|
| `architecture.md` | System architecture overview and data flow diagrams |
| `api-reference.md` | Full API endpoint reference for `core/media-api` |
| `kodi-setup.md` | Step-by-step Kodi add-on installation guide |
| `mobile-setup.md` | Mobile app build and deployment guide |
| `nexus-integration.md` | Unity/NEXUS media integration guide |
| `sharespace-setup.md` | ShareSpace platform setup and deployment |
| `contributing.md` | Contribution guidelines and code style |

## Quick Links

- [Main Repository README](../README.md)
- [Core Media API](../core/media-api/README.md)
- [NEXUS Client](../clients/nexus/README.md)
- [ShareSpace Client](../clients/sharespace/README.md)
- [Mobile App Client](../clients/mobile-app/README.md)
- [Kodi Add-on Client](../clients/kodi-addon/)

## Architecture Overview

```
[ShareSpace]  [NEXUS Unity]  [Mobile App]  [Kodi Add-on]
      |              |              |              |
      +------+-------+--------------+              |
             |                                     |
      [core/media-api]  <--------------------------+
             |
      [core/shared-assets]
```

All clients connect to `core/media-api` as the single source of truth for media access.
