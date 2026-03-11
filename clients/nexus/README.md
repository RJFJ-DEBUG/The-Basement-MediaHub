# NEXUS - World Traveler

Unity-based 3D world exploration game client for The-Basement-MediaHub.

## Overview

NEXUS - World Traveler is a Unity/C# game that dynamically loads media assets (audio, textures, video) from the shared `core/media-api`. This allows the game to stream and update content without requiring a full rebuild.

## Tech Stack

- **Engine:** Unity
- **Language:** C#
- **API Integration:** REST calls to `core/media-api`
- **Asset Format:** Textures (PNG/JPEG), Audio (MP3/OGG), Video (MP4)

## Folder Structure

```
clients/nexus/
+-- Assets/             # Unity Assets folder
|   +-- Scripts/        # C# scripts including MediaAPIClient.cs
|   +-- Scenes/         # Unity scene files
|   +-- Prefabs/        # Reusable prefabs
|   +-- StreamingAssets/ # Locally cached media
+-- ProjectSettings/    # Unity project settings
+-- Packages/           # Unity package manifest
```

## Media API Integration (C# Example)

```csharp
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class MediaAPIClient : MonoBehaviour
{
    private string apiBase = "http://localhost:3000/api/media";

    public IEnumerator GetMediaList()
    {
        UnityWebRequest request = UnityWebRequest.Get(apiBase);
        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            Debug.Log(request.downloadHandler.text);
        }
    }
}
```

## Setup

1. Open Unity Hub and add `clients/nexus/` as a project
2. Ensure `core/media-api` is running locally on port 3000
3. Play the game in the Unity editor or build for your target platform

## Notes

- Sparse checkout recommended: `git sparse-checkout set core clients/nexus`
- Requires Unity 2022.3 LTS or newer
