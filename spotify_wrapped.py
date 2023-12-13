import requests
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import datetime

#TODO(Change parameter to match information from SPOTIFY WEB API, CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, SCOPE)
sp =spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID =CLIENT_ID
                                                CLIENT_SECRET=CLIENT_SECRET
                                                REDIRECT_URL=REDIRECT_URL
                                                SCOPE=SCOPE))

mariah_uri = 'spotify:artist:6HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(mariah_uri_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])