import spotipy 
from spotipy.oauth2 import SpotifyOAuth


#TODO(Change parameter to match information from SPOTIFY WEB API, CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, SCOPE)
sp =spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID =CLIENT_ID,
                                                CLIENT_SECRET=CLIENT_SECRET,
                                                REDIRECT_URL=REDIRECT_URL,
                                                SCOPE=SCOPE,
                                                OPEN_BROWSER=True))
#TODO(Currently set to Mariah Carey, from spotify web browser, go to artist page then copy and paste the last alphanumeric query)
mariah_uri = 'spotify:artist:6HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(mariah_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])