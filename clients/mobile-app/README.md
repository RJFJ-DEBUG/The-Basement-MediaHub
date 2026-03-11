# Mobile App

Cross-platform mobile interface (iOS & Android) for The-Basement-MediaHub.

## Overview

The mobile app provides users with on-the-go access to the centralized media library. It connects to `core/media-api` via REST/GraphQL to browse, stream, and download media content.

## Tech Stack

- **Framework:** React Native (cross-platform iOS & Android)
- **Language:** JavaScript
- **API:** REST/GraphQL integration with `core/media-api`
- **Media Playback:** react-native-video, react-native-sound

## Folder Structure

```
clients/mobile-app/
+-- src/
|   +-- screens/        # App screens (Home, Browse, Player, Settings)
|   +-- components/     # Reusable UI components
|   +-- services/       # API service layer
|   +-- navigation/     # React Navigation config
|   +-- store/          # State management
+-- android/            # Android-specific files
+-- ios/                # iOS-specific files
+-- package.json
+-- app.json
```

## API Integration Example

```javascript
// services/mediaService.js
import { API_BASE_URL } from '../config';

export const fetchMedia = async () => {
  const res = await fetch(`${API_BASE_URL}/api/media`);
  return res.json();
};

export const getStreamUrl = (id) =>
  `${API_BASE_URL}/api/media/stream/${id}`;
```

## Setup

```bash
cd clients/mobile-app
npm install

# iOS
npx pod-install
npx react-native run-ios

# Android
npx react-native run-android
```

## Notes

- Requires `core/media-api` running (or deployed) and accessible
- Sparse checkout: `git sparse-checkout set core clients/mobile-app`
- Minimum iOS 13 / Android API 21
