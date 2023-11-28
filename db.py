import psycopg2
import db_adress

def __init__():
    conn = psycopg2.connect(db_adress.URL)
    cur = conn.cursor()

    with open("db.sql", "r") as file:
            schema = file.read()
    try:
            cur.execute(schema)
            conn.commit()
            print("SQL file executed successfully")
    except Exception as e:
            print("Error executing SQL file:", e)

    cur.close()
    conn.close()


def get_cursor():
    conn = psycopg2.connect(db_adress.URL)
    cur = conn.cursor()
    return conn, cur
