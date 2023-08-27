from spotipy import Spotify, SpotifyOAuth
from dotenv import load_dotenv
from os import getenv
from src.constants import TERMS

load_dotenv()


class GetRawData:

    def __init__(self):
        self.spotify = None
        self.raw_data: dict = {}

    def make_request(self):
        CLIENT_ID = getenv('CLIENT_ID')
        CLIENT_SECRET = getenv('CLIENT_SECRET')
        REDIRECT_URI = getenv('REDIRECT_URI')
        REQUEST = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-top-read'
        )
        self.spotify = Spotify(auth_manager=REQUEST)

    def get_raw_data_from_request(self):
        for term in TERMS:
            raw_data_for_term = self.spotify.current_user_top_artists(time_range=term)['items']
            self.raw_data.update({term: raw_data_for_term})


class ConvertRawData:

    def __init__(self, raw_data):
        self.list_of_column_values: list = []
        self.list_of_rows: list = []
        self.raw_data = raw_data

    def extract_data_by_term(self):
        """Processes raw spotify data contained in a dictionary to retrieve names, popularities and terms."""
        [names, popularities, terms] = [[], [], []]
        for term in TERMS:
            for artist_data in self.raw_data[term]:
                names.append(artist_data['name'])
                popularities.append(artist_data['popularity'])
                terms.append(term)
        self.list_of_column_values = [names, popularities, terms]

    def create_rows(self):
        """Creates a list of rows that can be passed into a database using SQLite."""
        [names, popularities, terms] = self.list_of_column_values
        for index in range(len(names)):
            self.list_of_rows.append([names[index], popularities[index], terms[index]])

    def return_rows(self):
        """Performs the extract data by term function and returns the list of rows for processing via SQLite."""
        self.extract_data_by_term()
        self.create_rows()
        return self.list_of_rows
