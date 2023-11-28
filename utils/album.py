from schemas.user import User, Token
from db import get_cursor

def get_album(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT Album.name,
        Artist.name AS artist
        FROM Album
        JOIN Artist
        ON Album.artist_id = Artist.id
        WHERE Album.id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchone()

def get_album_name(name: int):
    conn, cur = get_cursor()
    name = '%' + name + '%'
    cur.execute(
        """
        SELECT Album.id, Album.name,
        Artist.name AS artist
        FROM Album
        JOIN Artist
        ON Album.artist_id = Artist.id
        WHERE Album.name LIKE %s;
        """,
        (name,)
    )
    conn.commit()
    return cur.fetchall()

def get_album_artist(name: int):
    conn, cur = get_cursor()
    name = '%' + name + '%'
    cur.execute(
        """
        SELECT Album.id, Album.name,
        Artist.name AS artist
        FROM Album
        JOIN Artist
        ON Album.artist_id = Artist.id
        WHERE Artist.name LIKE %s;
        """,
        (name,)
    )
    conn.commit()
    return cur.fetchall()

def get_songs_album(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT Song.id, Song.name, Song.duration,
        Artist.name AS artist
        FROM Song
        JOIN Artist
        ON Song.artist_id = Artist.id
        JOIN Album_Song
        ON Song.id = Album_Song.song_id
        WHERE Album_Song.album_id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchall()
