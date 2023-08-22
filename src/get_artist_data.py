from .authentication import APICall
from dataclasses import dataclass
from .constants import TERMS


@dataclass
class GetArtistData:
    names_by_term = {}
    pops_by_term = {}

    @staticmethod
    def request_top_artists_data(term):
        top_artists_data: dict = APICall.request.current_user_top_artists(time_range=term)['items']
        return top_artists_data

    def set_names_by_term(self):
        for term in TERMS:
            names = []
            for artist_data in self.request_top_artists_data(term):
                name = artist_data['name']
                names.append(name)
            self.names_by_term.update({term: names})

    def set_pops_by_term(self):
        for term in TERMS:
            pops = []
            for artist_data in self.request_top_artists_data(term):
                pop = artist_data['popularity']
                pops.append(pop)
            self.pops_by_term.update({term: pops})

    def get_names_by_term(self, term):
        self.set_names_by_term()
        return self.names_by_term[term]

    def get_pops_by_term(self, term):
        self.set_pops_by_term()
        return self.pops_by_term[term]

