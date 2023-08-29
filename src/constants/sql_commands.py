INSERT_VALUES_INTO_TABLE = """
INSERT INTO 
top_artist_popularities (artist_name, popularity, term)
VALUES(?, ?, ?);
"""


class EXTRACT_VALUES:
    VALUES_INTRO = "SELECT * FROM top_artist_popularities WHERE"

    VALUES_OUTRO = "ORDER BY popularity;"

    AVG = """SELECT term, AVG(popularity)
    FROM top_artist_popularities
    GROUP BY term;"""

    MOST = """SELECT term, artist_name, MAX(popularity)
    FROM top_artist_popularities
    GROUP BY term;"""

    LEAST = """SELECT term, artist_name, MIN(popularity)
    FROM top_artist_popularities
    GROUP BY term;"""

    EXTRACTION_KEYS = {
        "short_term": "term IS 'short_term'",
        "medium_term": "term IS 'medium_term'",
        "long_term": "term IS 'long_term'",
    }
