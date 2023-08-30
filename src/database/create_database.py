from .database import Database
from ..constants import SQL_DATA, INSERT_VALUES_INTO_TABLE


def create_db(rows):
    """Creates SQL database and inserts processed Spotify data from GetArtistsData if database does not exist."""
    connection = Database(SQL_DATA, print=True)
    connection.migrate()
    connection.insert(INSERT_VALUES_INTO_TABLE, rows)
