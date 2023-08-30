from .connection_class import Connection
from ..constants import SQL_DATA


def create_db(rows):
    """Creates SQL database and inserts processed Spotify data from GetArtistsData if database does not exist."""
    connection = Connection(SQL_DATA)
    connection.create_table()
    connection.insert_into_table(rows_to_insert=rows)
