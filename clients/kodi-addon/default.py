import xbmcgui, xbmcplugin, xbmcaddon
import urllib.request, urllib.parse, json, sys

ADDON = xbmcaddon.Addon()
API_BASE = ADDON.getSetting("api_url") or "http://localhost:5000"
HANDLE = int(sys.argv[1])

def get_sources(media_type=None):
    url = f"{API_BASE}/api/sources"
    if media_type:
        url += f"?type={media_type}"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read())["sources"]

def list_menu():
    categories = [("Videos", "video"), ("Audio", "audio"), ("Images", "image")]
    for label, mtype in categories:
        li = xbmcgui.ListItem(label)
        params = urllib.parse.urlencode({"action": "list", "type": mtype})
        xbmcplugin.addDirectoryItem(HANDLE, f"{sys.argv[0]}?{params}", li, isFolder=True)
    xbmcplugin.endOfDirectory(HANDLE)

def list_sources(media_type):
    sources = get_sources(media_type)
    for s in sources:
        li = xbmcgui.ListItem(s["title"])
        li.setInfo("video", {"title": s["title"], "plot": s.get("description", "")})
        li.setArt({"thumb": s.get("thumbnail", "")})
        li.setProperty("IsPlayable", "true")
        params = urllib.parse.urlencode({"action": "play", "url": s["url"]})
        xbmcplugin.addDirectoryItem(HANDLE, f"{sys.argv[0]}?{params}", li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)

def play(url):
    xbmcplugin.setResolvedUrl(HANDLE, True, xbmcgui.ListItem(path=url))

params = dict(urllib.parse.parse_qsl(sys.argv[2].lstrip("?")))
action = params.get("action")

if not action:
    list_menu()
elif action == "list":
    list_sources(params.get("type"))
elif action == "play":
    play(params.get("url"))
