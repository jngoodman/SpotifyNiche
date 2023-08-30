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

    def insert(self, query: str, params):
        self._print_query(query, params)

        with self.create_connection() as connection:
            cursor = connection.cursor()
            if len(params) > 1:
                cursor.executemany(query, params)
            else:
                cursor.execute(query, params)

    def select(self, query: str, params=None):
        self._print_query(query, params)

        with self.create_connection() as connection:
            cursor = connection.cursor()

            if not params or len(params) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

            data = cursor.fetchall()
            cursor.close()

            print(data)
            print()

            return data

    def _print_query(self, query, params):
        if "print" in self._options and self._options["print"] == True:
            print(query)
            print(params)
            print()

    def read_sql_data_into_pandas(self, retrieval_command: str):
        """Retrieves data from database in pandas dataframe format."""
        return read_sql_query(retrieval_command, self.create_connection())
