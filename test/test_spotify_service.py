from unittest import TestCase

from src.spotify.service import TopArtistsByTerm, TopArtistsData, SpotifyService

from test.assets import (
    spotify_response_long_term_mock,
    spotify_response_medium_term_mock,
    spotify_response_short_term_mock,
)


class MockSpotifyClient:
    def current_user_top_artists(self, time_range: str):
        if time_range == "short_term":
            return spotify_response_short_term_mock.data

        if time_range == "medium_term":
            return spotify_response_medium_term_mock.data

        if time_range == "long_term":
            return spotify_response_long_term_mock.data

        raise Exception(f"Invalid time_range: {time_range}")


class SpotifyServiceTest(TestCase):
    def test_get_top_artists_by_terms(self):
        # Given
        spotify_service = SpotifyService(MockSpotifyClient())

        # When
        data = spotify_service.get_top_artists_by_terms()

        # Then
        self.assertEquals(
            data,
            TopArtistsByTerm(
                SHORT=[
                    TopArtistsData(name="Foals", popularity=62),
                    TopArtistsData(name="Djo", popularity=58),
                    TopArtistsData(name="Yot Club", popularity=65),
                    TopArtistsData(name="Young the Giant", popularity=66),
                    TopArtistsData(name="Vundabar", popularity=63),
                    TopArtistsData(name="Sundara Karma", popularity=45),
                    TopArtistsData(name="The Strokes", popularity=74),
                    TopArtistsData(name="Queens of the Stone Age", popularity=70),
                    TopArtistsData(name="Franz Ferdinand", popularity=65),
                    TopArtistsData(name="Peach Pit", popularity=61),
                    TopArtistsData(name="Wallows", popularity=67),
                    TopArtistsData(name="DANGERDOOM", popularity=52),
                    TopArtistsData(name="JJ DOOM", popularity=40),
                    TopArtistsData(name="MF DOOM", popularity=73),
                    TopArtistsData(name="Her's", popularity=61),
                    TopArtistsData(name="Gorillaz", popularity=77),
                    TopArtistsData(name="Muse", popularity=73),
                    TopArtistsData(name="TOOL", popularity=67),
                    TopArtistsData(name="Wolfmother", popularity=58),
                    TopArtistsData(
                        name="King Gizzard & The Lizard Wizard", popularity=62
                    ),
                ],
                MEDIUM=[
                    TopArtistsData(name="Foals", popularity=62),
                    TopArtistsData(name="Psychedelic Porn Crumpets", popularity=49),
                    TopArtistsData(name="Queens of the Stone Age", popularity=70),
                    TopArtistsData(name="Alice In Chains", popularity=69),
                    TopArtistsData(name="The Cribs", popularity=41),
                    TopArtistsData(name="Two Door Cinema Club", popularity=66),
                    TopArtistsData(name="Djo", popularity=58),
                    TopArtistsData(
                        name="King Gizzard & The Lizard Wizard", popularity=62
                    ),
                    TopArtistsData(name="Gorillaz", popularity=77),
                    TopArtistsData(name="The Strokes", popularity=74),
                    TopArtistsData(name="Peach Pit", popularity=61),
                    TopArtistsData(name="Mastodon", popularity=56),
                    TopArtistsData(name="Bad Nerves", popularity=47),
                    TopArtistsData(name="Yot Club", popularity=65),
                    TopArtistsData(name="Muse", popularity=73),
                    TopArtistsData(name="The Hellacopters", popularity=42),
                    TopArtistsData(name="Kato", popularity=64),
                    TopArtistsData(name="MF DOOM", popularity=73),
                    TopArtistsData(name="DANGERDOOM", popularity=52),
                    TopArtistsData(name="The Darkness", popularity=53),
                ],
                LONG=[
                    TopArtistsData(name="Foals", popularity=62),
                    TopArtistsData(name="Queens of the Stone Age", popularity=70),
                    TopArtistsData(name="The Cribs", popularity=41),
                    TopArtistsData(name="Pearl Jam", popularity=72),
                    TopArtistsData(name="Blue Öyster Cult", popularity=61),
                    TopArtistsData(name="Alice In Chains", popularity=69),
                    TopArtistsData(name="Gorillaz", popularity=77),
                    TopArtistsData(name="Two Door Cinema Club", popularity=66),
                    TopArtistsData(name="The Darkness", popularity=53),
                    TopArtistsData(name="Interpol", popularity=62),
                    TopArtistsData(name="The Smiths", popularity=74),
                    TopArtistsData(name="Phoenix", popularity=63),
                    TopArtistsData(name="Psychedelic Porn Crumpets", popularity=49),
                    TopArtistsData(name="Arctic Monkeys", popularity=84),
                    TopArtistsData(name="Foo Fighters", popularity=76),
                    TopArtistsData(name="Last Dinosaurs", popularity=50),
                    TopArtistsData(name="Muse", popularity=73),
                    TopArtistsData(name="The Wombats", popularity=61),
                    TopArtistsData(name="Wolfmother", popularity=58),
                    TopArtistsData(name="Eminem", popularity=88),
                ],
            ),
            "spotify data is not correct",
        )
