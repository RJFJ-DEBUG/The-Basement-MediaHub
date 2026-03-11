using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using Newtonsoft.Json;

[System.Serializable]
public class MediaSource {
    public string id, title, type, url, thumbnail, description;
    public List<string> tags;
}

[System.Serializable]
public class SourcesResponse {
    public List<MediaSource> sources;
}

public class MediaHubClient : MonoBehaviour {
    [Header("API Settings")]
    public string apiBaseUrl = "http://localhost:5000";

    public delegate void OnSourcesLoaded(List<MediaSource> sources);

    public void FetchSources(string mediaType = "", OnSourcesLoaded callback = null) {
        string url = $"{apiBaseUrl}/api/sources";
        if (!string.IsNullOrEmpty(mediaType)) url += $"?type={mediaType}";
        StartCoroutine(GetSources(url, callback));
    }

    private IEnumerator GetSources(string url, OnSourcesLoaded callback) {
        using (UnityWebRequest req = UnityWebRequest.Get(url)) {
            yield return req.SendWebRequest();
            if (req.result == UnityWebRequest.Result.Success) {
                var response = JsonConvert.DeserializeObject<SourcesResponse>(req.downloadHandler.text);
                callback?.Invoke(response.sources);
            } else {
                Debug.LogError($"[MediaHubClient] Error: {req.error}");
            }
        }
    }
}
