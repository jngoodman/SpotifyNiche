from spotipy import Spotify
from dataclasses import dataclass


class TERMS:
    SHORT = "short_term"
    MEDIUM = "medium_term"
    LONG = "long_term"


@dataclass
class TopArtistsData:
    name: str
    popularity: float

    @staticmethod
    def from_dict(dict: dict):
        return TopArtistsData(name=dict["name"], popularity=dict["popularity"])

    def __eq__(self, __value: "TopArtistsData") -> bool:
        return __value.name == self.name and __value.popularity == self.popularity


@dataclass
class TopArtistsByTerm:
    SHORT: list[TopArtistsData]
    MEDIUM: list[TopArtistsData]
    LONG: list[TopArtistsData]

    def __eq__(self, __value: "TopArtistsByTerm") -> bool:
        for i in range(len(self.SHORT)):
            if self.SHORT[i] != __value.SHORT[i]:
                return False

        for i in range(len(self.MEDIUM)):
            if self.MEDIUM[i] != __value.MEDIUM[i]:
                return False

        for i in range(len(self.LONG)):
            if self.LONG[i] != __value.LONG[i]:
                return False

        return True


class SpotifyService:
    _spotify = Spotify

    def __init__(self, spotify: Spotify):
        self._spotify = spotify

    def get_top_artists_by_terms(self):
        short_term_data = self._spotify.current_user_top_artists(time_range=TERMS.SHORT)

        medium_term_data = self._spotify.current_user_top_artists(
            time_range=TERMS.MEDIUM
        )

        long_term_data = self._spotify.current_user_top_artists(time_range=TERMS.LONG)

        top_artists_by_term = TopArtistsByTerm(
            SHORT=[TopArtistsData.from_dict(d) for d in short_term_data["items"]],
            MEDIUM=[TopArtistsData.from_dict(d) for d in medium_term_data["items"]],
            LONG=[TopArtistsData.from_dict(d) for d in long_term_data["items"]],
        )

        return top_artists_by_term
