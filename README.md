# The-Basement-MediaHub

> Centralized media access hub for NEXUS - World Traveler, ShareSpace, Mobile App, and Kodi Add-on. A monorepo serving multiple client platforms from a single media source.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Clients](#clients)
  - [NEXUS - World Traveler](#nexus---world-traveler)
  - [ShareSpace](#sharespace)
  - [Mobile App](#mobile-app)
  - [Kodi Add-on](#kodi-add-on)
- [Core](#core)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The-Basement-MediaHub is a monorepo that provides a unified media access layer for four distinct client platforms. All clients share a common REST/GraphQL media API housed in the `/core` directory, ensuring consistency and single-source-of-truth media delivery across:

- A Unity-based game (**NEXUS - World Traveler**)
- A multimedia sharing platform (**ShareSpace**)
- A cross-platform **Mobile App** (iOS & Android)
- A **Kodi Add-on** for home media center integration

---

## Repository Structure

```
The-Basement-MediaHub/
|
+-- core/
|   +-- media-api/          # Shared REST/GraphQL API for all clients
|   +-- shared-assets/      # Common images, icons, audio files
|
+-- clients/
|   +-- nexus/              # NEXUS - World Traveler (Unity/C#)
|   +-- sharespace/         # ShareSpace multimedia platform
|   +-- mobile-app/         # Mobile App (iOS & Android)
|   +-- kodi-addon/         # Kodi Add-on (addon.xml + scripts)
|
+-- docs/                   # Project documentation
+-- .gitignore
+-- README.md
```

---

## Clients

### NEXUS - World Traveler

A Unity-based 3D world exploration game. Pulls media assets (audio, textures, video) from the shared `core/media-api`. Built with Unity and C#.

- **Engine:** Unity
- **Language:** C#
- **Integration:** REST calls to `core/media-api` for dynamic asset loading
- **Path:** `clients/nexus/`

### ShareSpace

A multimedia sharing platform for hosting and distributing media content to all connected clients.

- **Language:** JavaScript
- **Integration:** Feeds media directly into the `core/media-api` endpoint
- **Path:** `clients/sharespace/`

### Mobile App

Cross-platform mobile interface (iOS & Android) that accesses the centralized media library.

- **Platforms:** iOS, Android
- **Integration:** Consumes `core/media-api` via REST/GraphQL
- **Path:** `clients/mobile-app/`

### Kodi Add-on

A Kodi repository add-on enabling home media center users to stream content from The-Basement-MediaHub.

- **Language:** Python
- **Structure:** Follows Kodi add-on standards (`addon.xml`, `/resources`, `/zips`)
- **Hosting:** Can be served via GitHub Pages for easy Kodi repository installation
- **Path:** `clients/kodi-addon/`

---

## Core

### media-api

The heart of the monorepo. A shared API layer that all four clients consume. Handles:
- Media fetching and serving
- Authentication tokens
- Metadata management

### shared-assets

Common static assets shared across all clients:
- Icons and logos
- UI sounds
- Shared textures and images

---

## Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/RJFJ-DEBUG/The-Basement-MediaHub.git
   ```

2. **Navigate to your client folder:**
   ```bash
   cd clients/nexus        # For NEXUS
   cd clients/sharespace   # For ShareSpace
   cd clients/mobile-app   # For Mobile App
   cd clients/kodi-addon   # For Kodi Add-on
   ```

3. **For sparse checkout (clone only your client):**
   ```bash
   git clone --filter=blob:none --sparse https://github.com/RJFJ-DEBUG/The-Basement-MediaHub.git
   cd The-Basement-MediaHub
   git sparse-checkout set core clients/nexus
   ```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

*Built and maintained by RJFJ-DEBUG*
