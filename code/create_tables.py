import sqlite3

# connect to sqlite 3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password txt)"

cursor.execute(create_table)

connection.commit()

connection.close()
