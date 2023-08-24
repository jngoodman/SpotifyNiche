from src.extract_data_from_spotify.authentication import APICall
from src.constants.__init__ import TERMS


class GetArtistData:

    def __init__(self):
        self.top_artists_data: dict = {}
        self.list_of_column_values: list = []
        self.list_of_rows: list = []

    def request_top_artist_data(self):
        for term in TERMS:
            self.top_artists_data.update({term: APICall.request.current_user_top_artists(time_range=term)['items']})

    def extract_data_by_term(self):
        [names, popularities, terms] = [[], [], []]
        for term in TERMS:
            for artist_data in self.top_artists_data[term]:
                names.append(artist_data['name'])
                popularities.append(artist_data['popularity'])
                terms.append(term)
        self.list_of_column_values = [names, popularities, terms]

    def create_rows(self):
        [name, popularity, term] = self.list_of_column_values
        for index in range(len(name)):
            self.list_of_rows.append([name[index], popularity[index], term[index]])

    def format_desired_data_into_rows(self):
        self.request_top_artist_data()
        self.extract_data_by_term()
        self.create_rows()

    def return_rows(self):
        self.format_desired_data_into_rows()
        return self.list_of_rows

