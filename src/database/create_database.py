from .database import Database
from ..constants import SQL_DATA


def create_db(rows):
    """Creates SQL database and inserts processed Spotify data from GetArtistsData if database does not exist."""
    connection = Database(SQL_DATA, print=True)
    connection.migrate()
    connection.insert(
        """INSERT INTO 
        top_artist_popularities (artist_name, popularity, term)
        VALUES(?, ?, ?);""",
        rows,
    )
