from sqlite3 import connect
from pandas import read_sql_query
from ..constants import INSERT_VALUES_INTO_TABLE
from .constants import CREATE_TOP_ARTIST_POPULARITIES_TABLE


class Connection:
    _database_file: str

    def __init__(self, database_file: str):
        self._database_file = database_file

        self.connection = None
        self.data_in_python = None

    def create_connection(self):
        """Establishes connection to database file."""
        self.connection = connect(self._database_file)

    def close_connection(self):
        """Closes connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_sql_command(self, *args, many=False, fetch=False):
        """Executes SQL commands using dynamic variables *args allowing insertion of both SQL commands and additional
        required variables, e.g., as for cursor.executemany()"""
        if self.connection:
            cursor = self.connection.cursor()
            if not many:
                cursor.execute(*args)
            else:
                cursor.executemany(*args)
            if fetch:
                self.data_in_python = cursor.fetchall()
            self.connection.commit()
            cursor.close()

    def create_table(
        self, create_table_command: str = CREATE_TOP_ARTIST_POPULARITIES_TABLE
    ):
        """Creates table using create_table_command. Default command is src.constants.CREATE_TOP_ARTIST_POPULARITIES_TABLE."""
        self.execute_sql_command(create_table_command)

    def insert_into_table(
        self,
        insert_data_command: str = INSERT_VALUES_INTO_TABLE,
        rows_to_insert: list = None,
    ):
        """Inserts data into table. Default command is src.constants.INSERT_VALUES_INTO_TABLE. Default rows to
        insert obtained by processing using GetArtistData class."""
        self.execute_sql_command(insert_data_command, rows_to_insert, many=True)

    def read_sql_data(self, retrieval_command: str):
        """Retrieves data from database."""
        self.execute_sql_command(retrieval_command, fetch=True)

    def read_sql_data_into_pandas(self, retrieval_command: str):
        """Retrieves data from database in pandas dataframe format."""
        self.data_in_python = read_sql_query(retrieval_command, self.connection)
