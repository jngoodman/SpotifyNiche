from os import path, remove
from .spotify.service import SpotifyService, TERMS
from .data_service import DataService, Record
from .graph import Bar


class InputController:
    _data_service: DataService
    _spotify_service: SpotifyService

    def __init__(self, database: DataService, spotify_service: SpotifyService):
        self._data_service = database
        self._spotify_service = spotify_service

    def check_for_data_refresh(self):
        while True:
            get_update = input(
                "Local data found. Would you like to update 'database.db' from Spotify? (Y/N): "
            ).lower()

            if get_update == "y":
                self.refresh_data()
                print("Old database deleted. Requesting new database...")
                return

            elif get_update == "n":
                print("Using existing database...")
                return

            else:
                print("Invalid response.")

    def refresh_data(self):
        self._data_service.delete_existing_data()

        artists = self._spotify_service.get_top_artists_by_terms()

        records: list[Record] = []
        records.extend(
            [Record(t.name, t.popularity, TERMS.SHORT) for t in artists.SHORT]
        )
        records.extend(
            [Record(t.name, t.popularity, TERMS.MEDIUM) for t in artists.MEDIUM]
        )
        records.extend([Record(t.name, t.popularity, TERMS.LONG) for t in artists.LONG])

        self._data_service.create_records(records)

    def get_sml_request(self):
        """Gets user request for what terms they would like to insert. Accepts only a combination of 'sml'."""
        term_request: str = ""
        request_accepted = False
        while not request_accepted:
            term_request = input(
                "What terms would you like to include? Any combination of (s/m/l): "
            ).lower()
            fail_list = []
            for letter in term_request:
                if letter not in "sml":
                    fail_list.append(letter)
                if not fail_list:
                    request_accepted = True
        return [request for request in term_request]

    def get_save_show_request(self, bar: Bar):
        save_show_request: str = ""

        request_accepted = False
        while not request_accepted:
            save_show_request = input(
                "Graph produced. Would you like to save, show, or both? (save/show/both): "
            ).lower()

            if save_show_request in ["save", "show", "both"]:
                request_accepted = True
            else:
                print("Invalid input.")

        logic_dict = {
            "save": [bar.save_bar],
            "show": [bar.show_bar],
            "both": [bar.save_bar, bar.show_bar],
        }

        for request, function_list in logic_dict.items():
            if save_show_request == request:
                [function() for function in function_list]
