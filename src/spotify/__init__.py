from .service import SpotifyService
from spotipy import Spotify, SpotifyOAuth


def create_spotify_service(client_id: str, client_secret: str, redirect_uri: str):
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-top-read",
    )

    spotify_client = Spotify(auth_manager=auth_manager)

    spotify_service = SpotifyService(spotify_client)

    return spotify_service
