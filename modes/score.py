import sqlite3

class Score():

    def __init__(self):
        sqlite_file = (r"db.sqlite")
        connection = sqlite3.connect(sqlite_file)
        cursor = connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS " + "db" + "(id integer PRIMARY KEY AUTOINCREMENT, result char not null)"
        cursor.execute(sql)
        sql = "SELECT * FROM " + "db"
        a = cursor.execute(sql).fetchall()
        print(a)
        connection.commit()
        cursor.close()
