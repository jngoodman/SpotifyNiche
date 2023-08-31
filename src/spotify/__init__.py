from os import getenv
from .service import SpotifyService, TERMS
from spotipy import Spotify, SpotifyOAuth

client_id = getenv("CLIENT_ID")
client_secret = getenv("CLIENT_SECRET")
redirect_uri = getenv("REDIRECT_URI")

auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-top-read",
)

spotify_client = Spotify(auth_manager=auth_manager)

spotify_service = SpotifyService(spotify_client)
