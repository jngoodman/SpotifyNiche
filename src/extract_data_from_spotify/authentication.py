from spotipy import Spotify, SpotifyOAuth
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class AUTH:
    CLIENT_ID = getenv('CLIENT_ID')
    CLIENT_SECRET = getenv('CLIENT_SECRET')
    REDIRECT_URI = getenv('REDIRECT_URI')
    REQUEST = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-top-read'
    )
    RAW_DATA = Spotify(auth_manager=REQUEST)

