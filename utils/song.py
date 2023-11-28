from schemas.user import User, Token
from db import get_cursor

def get_song(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT Song.name, Song.duration,
        Artist.name AS artist
        FROM Song
        JOIN Artist
        ON Song.artist_id = Artist.id
        WHERE Song.id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchone()

def get_song_name(name: str):
    conn, cur = get_cursor()
    name = '%' + name + '%'
    cur.execute(
        """
        SELECT Song.id, Song.name, Song.duration,
        Artist.name AS artist
        FROM Song
        JOIN Artist
        ON Song.artist_id = Artist.id
        WHERE Song.name LIKE %s;
        """,
        (name,)
    )
    conn.commit()
    return cur.fetchall()

def get_song_artist(name: str):
    conn, cur = get_cursor()
    name = '%' + name + '%'
    cur.execute(
        """
        SELECT Song.id, Song.name, Song.duration,
        Artist.name AS artist
        FROM Song
        JOIN Artist
        ON Song.artist_id = Artist.id
        WHERE Artist.name LIKE %s;
        """,
        (name,)
    )
    conn.commit()
    return cur.fetchall()

def add_song(user_id: int, song_id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        INSERT INTO User_Song (user_id, song_id)
        VALUES(%s, %s);
        """,
        (user_id, song_id)
    )
    conn.commit()

def remove_song(user_id: int, song_id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        DELETE FROM User_Song
        WHERE user_id = %s AND song_id = %s;
        """,
        (user_id, song_id)
    )
    conn.commit()

def get_my_song(user_id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT Song.id, Song.name, Song.duration,
        Artist.name AS artist
        FROM User_Song
        JOIN Song
        ON Song.id = User_Song.song_id
        JOIN Artist
        ON Artist.id = Song.artist_id
        WHERE User_Song.user_id = %s;
        """,
        (user_id,)
    )
    conn.commit()
    return cur.fetchall()
