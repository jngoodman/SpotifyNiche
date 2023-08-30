import sqlite3


def migrate(conn: sqlite3.Connection) -> sqlite3.Connection:
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE 
        top_artist_popularities (
        id INTEGER PRIMARY KEY,
        artist_name TEXT NOT NULL,
        popularity INTEGER,
        term TEXT NOT NULL
        );
        """
    )

    conn.commit()

    return conn
