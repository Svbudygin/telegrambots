import sqlite3


def bd_get_last():
    conn = sqlite3.connect("mat.sql")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mat ORDER BY ID  DESC LIMIT 1")
    data = list(cursor.fetchall())[0][-1]
    cursor.close()
    conn.close()
    return data


