from sqlite3 import connect
from pandas import read_sql_query
from .migrate import migrate


class Database:
    _database_file: str
    _options: dict

    def __init__(self, database_file: str, **kwargs):
        self._database_file = database_file
        self._options = kwargs

    def create_connection(self):
        """Establishes connection to database file."""
        return connect(self._database_file)

    def migrate(self):
        """Creates the database."""
        con = self.create_connection()
        migrate(con).close()

    def insert(self, query: str, params) -> int:
        self._print_query(query, params)

        connection = self.create_connection()
        cursor = connection.cursor()
        if len(params) > 1:
            cursor.executemany(query, params)
        else:
            cursor.execute(query, params)

        connection.commit()

        id = cursor.lastrowid
        cursor.close()
        connection.close()

        return id

    def select(self, query: str, params=None):
        self._print_query(query, params)

        connection = self.create_connection()
        cursor = connection.cursor()

        if not params or len(params) == 0:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

        data = cursor.fetchall()
        cursor.close()
        connection.close()

        print(data)

        return data

    def _print_query(self, query, params):
        if "print" in self._options and self._options["print"] == True:
            print()
            print(query)
            print(params)

    def read_sql_data_into_pandas(self, retrieval_command: str, params):
        """Retrieves data from database in pandas dataframe format."""
        return read_sql_query(
            retrieval_command, self.create_connection(), params=params
        )
