from .connection_class import Connection
from ..constants import SQL_DATA


def retrieve_from_db(retrieval_command, pandas=False):
    """Establishes connection to existing database file and reads in using the read_sql_data methods of the
    Connection() class, allowing pandas flag to select appropriate command, then closes connection.
    """
    connection = Connection(SQL_DATA, print=True)
    if not pandas:
        return connection.select(retrieval_command)

    return connection.read_sql_data_into_pandas(retrieval_command)
