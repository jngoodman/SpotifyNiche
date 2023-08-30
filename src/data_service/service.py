from dataclasses import dataclass
from ..database import Database


@dataclass
class Record:
    artist_name: str
    popularity: float
    term: str

    @staticmethod
    def from_row(row: dict):
        return Record(row["artist_name"], row["popularity"], row["term"])


class DataService:
    _database: Database

    def __init__(self, database: Database):
        self._database = database

    def get_all_artists_for_terms(self, terms: list[str]):
        term_condition = ""

        if len(terms) > 0:
            term_condition = f"WHERE term IN ({','.join(['?' for _ in terms])})"  # Only use `IS` for null comparison

        query = f"SELECT * FROM top_artist_popularities {term_condition} ORDER BY popularity;"
        data = self._database.select(query, params=terms)

        return [Record.from_row(row) for row in data]

    def get_most_popular_artists_by_term(self):
        data = self._database.select(
            """SELECT term, artist, MAX(popularity) FROM top_artists_popularities GROUP BY term"""
        )
        return [Record.from_row(row) for row in data]

    def get_least_popular_artists_by_term(self):
        data = self._database.select(
            """SELECT term, artist, MIN(popularity) FROM top_artists_popularities GROUP BY term"""
        )
        return [Record.from_row(row) for row in data]

    def get_least_popular_artists_by_term(self):
        data = self._database.select(
            """SELECT term, AVG(popularity) FROM top_artists_popularities GROUP BY term"""
        )
        return [Record.from_row(row) for row in data]
