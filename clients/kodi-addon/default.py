# -*- coding: utf-8 -*-
"""
The Basement MediaHub - Kodi Add-on
Entrypoint: default.py
"""

import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import requests

# Add-on info
ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

# MediaHub API config (update with your deployed API URL)
API_BASE = ADDON.getSetting('api_url') or 'http://localhost:3000/api'


def list_media():
    """Fetch and list all media from The Basement MediaHub API."""
    try:
        response = requests.get(f"{API_BASE}/media", timeout=10)
        media_items = response.json()

        for item in media_items:
            list_item = xbmcgui.ListItem(label=item.get('title', 'Unknown'))
            stream_url = f"{API_BASE}/media/stream/{item['id']}"
            list_item.setPath(stream_url)
            xbmcplugin.addDirectoryItem(
                handle=HANDLE,
                url=stream_url,
                listitem=list_item,
                isFolder=False
            )
    except Exception as e:
        xbmc.log(f"[BasementMediaHub] Error fetching media: {e}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification(
            ADDON_NAME,
            'Could not connect to MediaHub API. Check your settings.',
            xbmcgui.NOTIFICATION_ERROR
        )

    xbmcplugin.endOfDirectory(HANDLE)


if __name__ == '__main__':
    list_media()
