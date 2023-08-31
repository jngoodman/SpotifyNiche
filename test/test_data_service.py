from unittest import TestCase

from src.data_service import DataService, Record
from src.database import Database


class DataServiceTest(TestCase):
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

    def test_get_most_popular_artists_by_term(self):
        # Given
        self.insert_data()
        service = DataService(self.database)

        # When
        data = service.get_most_popular_artists_by_term()

        # Then
        self.assertEqual(len(data), 3, "should return 3 records")

        record0 = data[0]
        self.assertEqual(
            record0.artist_name, "artist 4", "most popular long_term artist"
        )
        self.assertEqual(record0.popularity, 40, "most popular long_term popularity")
        self.assertEqual(record0.term, "long_term", "long_term term")

        record1 = data[1]
        self.assertEqual(
            record1.artist_name, "artist 4", "most popular medium_term artist"
        )
        self.assertEqual(record1.popularity, 40, "most popular medium_term popularity")
        self.assertEqual(record1.term, "medium_term", "medium_term term")

        record2 = data[2]
        self.assertEqual(
            record2.artist_name, "artist 3", "most popular short_term artist"
        )
        self.assertEqual(record2.popularity, 30, "most popular short_term popularity")
        self.assertEqual(record2.term, "short_term", "short_term term")
