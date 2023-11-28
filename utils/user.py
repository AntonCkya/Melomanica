from schemas.user import User, Token
from db import get_cursor
import hashlib

def register(user: User):
    conn, cur = get_cursor()
    cur.execute(
        """
        INSERT INTO Users (login, password)
        VALUES(%s, %s)
        RETURNING id;
        """,
        (user.login, hashlib.sha256(bytes(user.password, 'utf-8')).hexdigest())
    )
    conn.commit()
    return cur.fetchone()

def login(user: User):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT id
        FROM Users
        WHERE login = %s AND password = %s;
        """,
        (user.login, hashlib.sha256(bytes(user.password, 'utf-8')).hexdigest())
    )
    conn.commit()
    return cur.fetchone()

def get_token(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        SELECT token
        FROM Token
        WHERE user_id = %s;
        """,
        (id,)
    )
    conn.commit()
    return cur.fetchone()

def put_token(t: Token):
    conn, cur = get_cursor()
    cur.execute(
        """
        INSERT INTO Token (user_id, token)
        VALUES(%s, %s)
        """,
        (t.user_id, t.token)
    )
    conn.commit()

def delete_token(id: int):
    conn, cur = get_cursor()
    cur.execute(
        """
        DELETE FROM Token
        WHERE user_id = %s;
        """,
        (id,)
    )
    conn.commit()
