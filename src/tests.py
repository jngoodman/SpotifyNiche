from src import TERMS
from dotenv import load_dotenv
from unittest import TestCase, main
from os import getenv, path, stat, remove
from spotipy import Spotify, SpotifyOAuth
from sqlite3 import connect


class RawDataTests(TestCase):

    def test_env_params(self):
        """Passes if .env parameters not empty."""
        load_dotenv()
        env_params = [getenv('CLIENT_ID'), getenv('CLIENT_SECRET'), getenv('REDIRECT_URI')]
        self.assertTrue(all(env_params), "CLIENT_ID, CLIENT_SECRET and REDIRECT_URI should be non-empty in .env")

    def test_is_spotify(self):
        """Passes if Spotify object."""
        test_spotify = Spotify(auth_manager=SpotifyOAuth
        (client_id=getenv('CLIENT_ID'),
         client_secret=getenv('CLIENT_SECRET'),
         redirect_uri=getenv('REDIRECT_URI'),
         scope='user_top_read')
                               )
        self.assertIsInstance(test_spotify, Spotify, "Should be a Spotify object,")

    def test_terms_in_raw_data(self):
        """Passes if all terms found in raw data."""
        test_spotify = Spotify(auth_manager=SpotifyOAuth
        (client_id=getenv('CLIENT_ID'),
         client_secret=getenv('CLIENT_SECRET'),
         redirect_uri=getenv('REDIRECT_URI'),
         scope='user-top-read')
                               )
        test_data = {}
        for term in TERMS:
            try:
                test_data.update({term: test_spotify.current_user_top_artists(time_range=term)['items']})
            except KeyError:
                self.fail(f"{term} not found.")


class ConvertDataTests(TestCase):
    dummy_spotify_data = {
        'short_term': [
            {'name': 'short_term_band_1', 'popularity': 80},
            {'name': 'short_term_band_2', 'popularity': 75}],
        'medium_term': [
            {'name': 'medium_term_band_1', 'popularity': 70},
            {'name': 'medium_term_band_2', 'popularity': 65}],
        'long_term': [
            {'name': 'long_term_band_1', 'popularity': 60},
            {'name': 'long_term_band_2', 'popularity': 55}]
    }

    # dummy_spotify_data has the same structure as test_data in RawDataTests().test_terms_in_raw_data()

    def test_column_extraction(self):
        [names, popularities, terms] = [[], [], []]
        for term in TERMS:
            for artist_data in self.dummy_spotify_data[term]:
                names.append(artist_data['name'])
                popularities.append(artist_data['popularity'])
                terms.append(term)
        self.assertEqual(names, ['short_term_band_1', 'short_term_band_2', 'medium_term_band_1', 'medium_term_band_2',
                                 'long_term_band_1', 'long_term_band_2'],
                         "Names column should contain all band names for all terms in order set out in TERMS.")
        self.assertEqual(popularities, [80, 75, 70, 65, 60, 55],
                         "Popularities column should contain all popularities for all terms in order set out in TERMS.")
        self.assertEqual(terms, ['short_term', 'short_term', 'medium_term', 'medium_term', 'long_term', 'long_term'],
                         "Terms column should contain term for each entry in order set out in TERMS.")

    def test_row_extraction(self):
        [names, popularities, terms] = [[], [], []]
        for term in TERMS:
            for artist_data in self.dummy_spotify_data[term]:
                names.append(artist_data['name'])
                popularities.append(artist_data['popularity'])
                terms.append(term)
        list_of_rows = []
        for index in range(len(names)):
            list_of_rows.append([names[index], popularities[index], terms[index]])
        self.assertEqual(list_of_rows[0], ['short_term_band_1', 80, 'short_term'],
                         "Row should be name, popularity and term of corresponding entry in dummy_spotify_data.")
        self.assertEqual(list_of_rows[3], ['medium_term_band_2', 65, 'medium_term'],
                         "Row should be name, popularity and term of corresponding entry in dummy_spotify_data.")
        self.assertEqual(list_of_rows[4], ['long_term_band_1', 60, 'long_term'],
                         "Row should be name, popularity and term of corresponding entry in dummy_spotify_data.")


class ConnectionTests(TestCase):
    database = 'dummy_database.db'
    dummy_insertion_data = [['short_term_band', 'popularity_value', 'short_term'],
                            ['medium_term_band', 'popularity_value', 'medium_term'],
                            ['long_term_band', 'popularity_value', 'long_term']]

    # dummy_insertion_data is equivalent to list_of_rows from ConvertDataTests().test_row_extraction()

    def test_create_close_connection(self):
        connection = connect(self.database)
        self.assertTrue(path.isfile('dummy_database.db'), "dummy_database.db should exist if connection established.")
        connection.close()
        connection = None
        self.assertIsNone(connection, "connection should be None after closing and setting to None.")

    def execute_sql_command(self, *args, many=False, fetch=False):
        connection = connect(self.database)
        cursor = connection.cursor()
        fetched_data = None
        if not many:
            cursor.execute(*args)
        else:
            cursor.executemany(*args)
        if fetch:
            fetched_data = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        if fetch:
            return fetched_data

    def test_step_a_create_table(self):
        sql_command = """CREATE TABLE dummy_table (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        popularity INTEGER,
        term TEXT NOT NULL 
        );"""
        self.execute_sql_command(sql_command)
        self.assertTrue(stat(self.database).st_size != 0, "if table, file size should be > 0")

    def test_step_b_fetch_from_table(self):
        """We'll test the retrieval of data works before inserting any data, since we can still retrieve empty lists.
        Knowing the retrieval works will allow us to test we inserted the right kind of data into the database later."""
        sql_command = """SELECT * FROM dummy_table"""
        fetched_data = self.execute_sql_command(sql_command, fetch=True)
        self.assertIsInstance(fetched_data, list)

    @staticmethod
    def remove_database_after_testing():
        remove('dummy_database.db')

    def test_step_c_data_inserted_into_table(self):
        insert_command = """INSERT INTO dummy_table (name, popularity, term)
        VALUES(?, ?, ?)"""
        fetch_command = """SELECT * from dummy_table"""
        self.execute_sql_command(insert_command, self.dummy_insertion_data, many=True)
        fetched_results = self.execute_sql_command(fetch_command, fetch=True)
        self.assertEqual(fetched_results[0], (1, 'short_term_band', 'popularity_value', 'short_term'))
        self.assertEqual(fetched_results[2], (3, 'long_term_band', 'popularity_value', 'long_term'))
        self.remove_database_after_testing()


if __name__ == "__main__":
    main()
