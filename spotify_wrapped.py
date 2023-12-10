import requests
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import datetime

sp =spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID ='3de178190d004e12bc58be2787d128a4'
                                                CLIENT_SECRET='22002629a66c481998ef8d717b5235d6'
                                                REDIRECT_URL='http://127.0.0.1:9090'
                                                SCOPE='user-library-read'))