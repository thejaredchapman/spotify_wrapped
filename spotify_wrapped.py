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