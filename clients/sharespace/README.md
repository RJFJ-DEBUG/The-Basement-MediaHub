# ShareSpace

Multimedia sharing platform client for The-Basement-MediaHub.

## Overview

ShareSpace is a JavaScript-based web platform that allows users to host, share, and distribute media content. It acts as both a media producer (uploading content to `core/media-api`) and a consumer (streaming content to users).

## Tech Stack

- **Language:** JavaScript (Node.js + frontend framework)
- **API:** REST integration with `core/media-api`
- **Media Formats:** Video (MP4/WebM), Audio (MP3/OGG), Images (WebP/PNG)

## Folder Structure

```
clients/sharespace/
+-- src/
|   +-- components/     # UI components
|   +-- pages/          # Page views
|   +-- services/       # API service calls (mediaService.js)
|   +-- assets/         # Local static assets
+-- public/             # Public-facing files
+-- package.json
+-- .env.example
```

## Media API Integration (JS Example)

```javascript
// services/mediaService.js
const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:3000/api';

export const getMediaList = async () => {
  const response = await fetch(`${API_BASE}/media`);
  return response.json();
};

export const streamMedia = (id) => {
  return `${API_BASE}/media/stream/${id}`;
};
```

## Setup

```bash
cd clients/sharespace
npm install
npm run dev
```

## Notes

- Requires `core/media-api` running on port 3000
- Sparse checkout: `git sparse-checkout set core clients/sharespace`
