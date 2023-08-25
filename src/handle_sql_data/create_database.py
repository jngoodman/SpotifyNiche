from src.handle_sql_data.sql_connection_class import Connection
from os import path


def create_db():
    """Creates SQL database and inserts processed Spotify data from GetArtistsData if database does not exist."""
    if not path.isfile("database.db"):
        connection = Connection()
        connection.create_connection("database.db")
        connection.create_table()
        connection.insert_into_table()
        connection.close_connection()
