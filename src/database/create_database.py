from .connection_class import Connection
from ..constants import SQL_DATA, INSERT_VALUES_INTO_TABLE


def create_db(rows):
    """Creates SQL database and inserts processed Spotify data from GetArtistsData if database does not exist."""
    connection = Connection(SQL_DATA)
    connection.migrate()
    connection.insert(INSERT_VALUES_INTO_TABLE, rows)
