from dataclasses import dataclass
from ..database import Database


@dataclass
class Record:
    artist_name: str
    popularity: float
    term: str

    @staticmethod
    def from_row(row: dict):
        return Record(term=row[0], artist_name=row[1], popularity=row[2])


class DataService:
    _database: Database

    def __init__(self, database: Database):
        self._database = database

    def get_all_artists_for_terms(self, terms: list[str]):
        term_condition = ""

        if len(terms) > 0:
            term_condition = f"WHERE term IN ({','.join(['?' for _ in terms])})"  # Only use `IS` for null comparison

        query = f"SELECT term, artist_name, popularity FROM top_artist_popularities {term_condition} ORDER BY popularity"

        # data = self._database.select(query, params=terms)
        # return [Record.from_row(row) for row in data]
        return self._database.read_sql_data_into_pandas(query, params=terms)

    def get_most_popular_artists_by_term(self):
        data = self._database.select(
            """SELECT term, artist_name, MAX(popularity) FROM top_artist_popularities GROUP BY term"""
        )
        return [Record.from_row(row) for row in data]

    def get_least_popular_artists_by_term(self):
        data = self._database.select(
            """SELECT term, artist_name, MIN(popularity) FROM top_artist_popularities GROUP BY term"""
        )
        return [Record.from_row(row) for row in data]

    def get_average_popular_artists_by_term(self):
        data = self._database.select(
            """SELECT term, artist_name, AVG(popularity) FROM top_artist_popularities GROUP BY term"""
        )
        return [Record.from_row(row) for row in data]
