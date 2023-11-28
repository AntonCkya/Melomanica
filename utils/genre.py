from schemas.user import User, Token
from db import get_cursor

def get_genre_name(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT id, name
        FROM Genre
        WHERE id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchone()

def get_genre_songs(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT
        Song.id, Song.name, Song.duration,
        Artist.name AS artist
        FROM Genre_Song
        JOIN Song
        ON Song.id = Genre_Song.song_id
        JOIN Artist
        ON Artist.id = Song.artist_id
        WHERE Genre_Song.genre_id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchall()

def get_song_genres(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT
        Genre.id, Genre.name
        FROM Genre_Song
        JOIN Genre
        ON Genre.id = Genre_Song.genre_id
        WHERE Genre_Song.song_id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchall()
