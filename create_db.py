import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_users_table = "CREATE TABLE IF NOT EXISTS users \
    (id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)"

cursor.execute(create_users_table)

connection.commit()
connection.close()