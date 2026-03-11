# media-api

The core shared REST/GraphQL API layer for The-Basement-MediaHub.

## Purpose

This module serves as the single source of truth for media delivery across all client platforms:
- NEXUS - World Traveler (Unity/C#)
- ShareSpace (JavaScript)
- Mobile App (iOS/Android)
- Kodi Add-on (Python)

## Endpoints (Planned)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/media | List all media |
| GET | /api/media/:id | Get media by ID |
| POST | /api/media | Upload new media |
| DELETE | /api/media/:id | Remove media |
| GET | /api/media/stream/:id | Stream media content |

## Tech Stack

- Node.js / Express (REST)
- GraphQL (optional layer)
- JSON Web Tokens (JWT) for auth

## Setup

```bash
cd core/media-api
npm install
npm start
```

## Environment Variables

Create a `.env` file in this directory:

```
PORT=3000
MEDIA_STORAGE_PATH=./media
JWT_SECRET=your_secret_here
```
