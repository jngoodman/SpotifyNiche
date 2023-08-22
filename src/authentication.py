from spotipy import Spotify, oauth2, SpotifyOAuth
from dotenv import load_dotenv
from os import getenv
from dataclasses import dataclass

load_dotenv()


class APICall:
    CLIENT_ID = getenv('CLIENT_ID')
    CLIENT_SECRET = getenv('CLIENT_SECRET')
    REDIRECT_URL = getenv('REDIRECT_URL')
    request = Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URL,
            scope='user-top-read'
        )
    )

