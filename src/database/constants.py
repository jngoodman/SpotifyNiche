CREATE_TOP_ARTIST_POPULARITIES_TABLE = """
CREATE TABLE 
top_artist_popularities (
id INTEGER PRIMARY KEY,
artist_name TEXT NOT NULL,
popularity INTEGER,
term TEXT NOT NULL
);
"""
