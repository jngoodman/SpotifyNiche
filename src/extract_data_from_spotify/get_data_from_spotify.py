from src.extract_data_from_spotify.authentication import APICall
from src.constants.__init__ import TERMS


class GetArtistData:

    def __init__(self):
        self.top_artists_data: dict = {}
        self.list_of_column_values: list = []
        self.list_of_rows: list = []
        self.api_request = APICall.request

    def request_top_artist_data(self):
        """Makes API request for current user's top artists and appends this raw data to a dictionary."""
        for term in TERMS:
            self.top_artists_data.update({term: self.api_request.current_user_top_artists(time_range=term)['items']})

    def extract_data_by_term(self):
        """Processes raw spotify data contained in a dictionary to retrieve names, popularities and terms."""
        [names, popularities, terms] = [[], [], []]
        for term in TERMS:
            for artist_data in self.top_artists_data[term]:
                names.append(artist_data['name'])
                popularities.append(artist_data['popularity'])
                terms.append(term)
        self.list_of_column_values = [names, popularities, terms]

    def create_rows(self):
        """Creates a list of rows that can be passed into a database using SQLite."""
        [name, popularity, term] = self.list_of_column_values
        for index in range(len(name)):
            self.list_of_rows.append([name[index], popularity[index], term[index]])

    def format_desired_data_into_rows(self):
        """Performs the request, extraction and row creation functions."""
        self.request_top_artist_data()
        self.extract_data_by_term()
        self.create_rows()

    def return_rows(self):
        """Performs the aggregate data creation function and returns the list of rows for processing via SQLite."""
        self.format_desired_data_into_rows()
        return self.list_of_rows

