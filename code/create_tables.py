import sqlite3

# connect to sqlite 3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password txt)"
create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY name text,price real)"

cursor.execute(create_table)
cursor.execute(create_table_items)

connection.commit()

connection.close()
