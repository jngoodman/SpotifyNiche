from unittest import TestCase

from src.database import Database
from src.data_service import Record, DataService
from src.graph import Bar
from src import construct_bar


class CreateBarClassTest(TestCase):
    # Runs before each test
    def setUp(self):
        database = Database("test.database.db")
        database.migrate()
        database.delete("DELETE FROM top_artist_popularities")

        self.database = database

    def insert_data(self):
        service = DataService(self.database)

        service.create_records(
            [
                Record(artist_name="artist 1", popularity=10, term="short_term"),
                Record(artist_name="artist 1", popularity=10, term="medium_term"),
                Record(artist_name="artist 1", popularity=10, term="long_term"),
                #
                Record(artist_name="artist 2", popularity=20, term="short_term"),
                Record(artist_name="artist 2", popularity=20, term="medium_term"),
                #
                Record(artist_name="artist 3", popularity=30, term="short_term"),
                Record(artist_name="artist 3", popularity=30, term="long_term"),
                #
                Record(artist_name="artist 4", popularity=40, term="medium_term"),
                Record(artist_name="artist 4", popularity=40, term="long_term"),
            ]
        )

    def test_creates_bar_chart(self):
        self.insert_data()
        bar = construct_bar("short_term", data_service=DataService(self.database))
        bar.save_bar()

        self.assertEqual(1, 1, "chart")

        expected_graph_path = "test/assets/spotify_niche_[short_term].expected.png"
        actual_graph_path = "spotify_niche_[short_term].png"
        with open(expected_graph_path, "rb") as expected:
            with open(actual_graph_path, "rb") as actual:
                self.assertEqual(
                    expected.read(),
                    actual.read(),
                    "Generated graph should be correct",
                )

        # bar = Bar(
        #     ["short_term"],
        #     {"long_term": 65.45, "medium_term": 60.7, "short_term": 62.95},
        #     {
        #         "term": ["short_term", "short_term"],
        #         "artist_name": ["MF DOOM", "Djo"],
        #         "popularity": [40, 58],
        #     },
        # )

        # bar.construct_bars()
        # bar.determine_title_suffix()
        # bar.adjust_axes()
        # bar.adjust_labels()
