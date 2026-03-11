# -*- coding: utf-8 -*-
"""
The Basement MediaHub - Kodi Add-on
Entrypoint: default.py
"""

import sys
import urllib.parse
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

try:
    import requests
except ImportError:
    xbmcgui.Dialog().ok('Missing Dependency', 'requests library not found. Install it via pip.')
    sys.exit(1)

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])
ARGS = urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query)
API_BASE = ADDON.getSetting('api_url') or 'http://localhost:3000/api'


def build_url(query):
    return PLUGIN_URL + '?' + urllib.parse.urlencode(query)


def main_menu():
    """Show top-level categories."""
    categories = [
        ('movies', 'Movies', 'DefaultMovies.png'),
        ('tvshows', 'TV Shows', 'DefaultTVShows.png'),
        ('search', 'Search', 'DefaultAddonsSearch.png'),
    ]
    for cat_id, label, icon in categories:
        li = xbmcgui.ListItem(label=label)
        li.setArt({'icon': icon, 'thumb': icon})
        li.setInfo('video', {'title': label, 'mediatype': 'video'})
        url = build_url({'category': cat_id})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=li, isFolder=True)
    xbmcplugin.addSortMethods(HANDLE, xbmcplugin.SORT_METHOD_LABEL)
    xbmcplugin.endOfDirectory(HANDLE)


def list_media(category):
    """Fetch and list media items for the given category."""
    try:
        response = requests.get(f"{API_BASE}/media?type={category}", timeout=10)
        response.raise_for_status()
        media_items = response.json()
    except Exception as e:
        xbmc.log(f"[BasementMediaHub] API error: {e}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification(
            ADDON_NAME,
            'Could not connect to MediaHub API. Check Settings.',
            xbmcgui.NOTIFICATION_ERROR
        )
        xbmcplugin.endOfDirectory(HANDLE)
        return

    for item in media_items:
        title = item.get('title', 'Unknown')
        item_id = item.get('id', '')
        thumb = item.get('thumbnail', '')
        plot = item.get('description', '')
        year = item.get('year', '')
        genre = item.get('genre', '')
        stream_url = f"{API_BASE}/media/stream/{item_id}"

        li = xbmcgui.ListItem(label=title)
        li.setArt({'thumb': thumb, 'poster': thumb, 'fanart': thumb})
        li.setInfo('video', {
            'title': title,
            'plot': plot,
            'year': year,
            'genre': genre,
            'mediatype': 'movie' if category == 'movies' else 'episode'
        })
        li.setProperty('IsPlayable', 'true')
        li.setPath(stream_url)
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=stream_url, listitem=li, isFolder=False)

    xbmcplugin.addSortMethods(HANDLE, xbmcplugin.SORT_METHOD_LABEL)
    xbmcplugin.endOfDirectory(HANDLE)


def search():
    """Open keyboard dialog, query API, and list results."""
    kb = xbmc.Keyboard('', 'Search The Basement MediaHub')
    kb.doModal()
    if not kb.isConfirmed():
        xbmcplugin.endOfDirectory(HANDLE)
        return
    query = kb.getText().strip()
    if not query:
        xbmcplugin.endOfDirectory(HANDLE)
        return

    try:
        response = requests.get(f"{API_BASE}/media/search", params={'q': query}, timeout=10)
        response.raise_for_status()
        media_items = response.json()
    except Exception as e:
        xbmc.log(f"[BasementMediaHub] Search error: {e}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification(ADDON_NAME, 'Search failed. Check API.', xbmcgui.NOTIFICATION_ERROR)
        xbmcplugin.endOfDirectory(HANDLE)
        return

    for item in media_items:
        title = item.get('title', 'Unknown')
        item_id = item.get('id', '')
        thumb = item.get('thumbnail', '')
        stream_url = f"{API_BASE}/media/stream/{item_id}"

        li = xbmcgui.ListItem(label=title)
        li.setArt({'thumb': thumb})
        li.setInfo('video', {'title': title, 'mediatype': 'video'})
        li.setProperty('IsPlayable', 'true')
        li.setPath(stream_url)
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=stream_url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


# --- Router ---
if __name__ == '__main__':
    category = ARGS.get('category', [None])[0]

    if category is None:
        main_menu()
    elif category == 'search':
        search()
    else:
        list_media(category)
