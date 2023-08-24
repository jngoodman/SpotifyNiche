from sqlite3 import connect
from pandas import read_sql_query
from src.constants.__init__ import CREATE_DATA_STRUCTURE, INSERT_VALUES_INTO_TABLE
from src.extract_data_from_spotify.__init__ import GetArtistData


class Connection:

    def __init__(self):
        self.connection = None
        self.data_in_python = None

    def create_connection(self, database_file):
        self.connection = connect(database_file)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_sql_command(self, *args, many=False, fetch=False):
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

    def create_table(self, create_table_command: str = CREATE_DATA_STRUCTURE,
                     insert_data_command: str = INSERT_VALUES_INTO_TABLE,
                     rows_to_insert: list = GetArtistData().return_rows()):
        self.execute_sql_command(create_table_command)
        self.execute_sql_command(insert_data_command, rows_to_insert, many=True)

    def read_sql_data(self, retrieval_command: str):
        self.execute_sql_command(retrieval_command, fetch=True)

    def read_sql_data_into_pandas(self, retrieval_command: str):
        self.data_in_python = read_sql_query(retrieval_command, self.connection)
