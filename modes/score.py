import sqlite3

class Score():

    def __init__(self):
        sqlite_file = (r"C:\Users\32498\sqlite3\data.db")
        connection = sqlite3.connect(sqlite_file)
        cursor = connection.cursor()
        sql = "SELECT * FROM " + "db"
        cursor.execute(sql)
        connection.commit()
        cursor.close()