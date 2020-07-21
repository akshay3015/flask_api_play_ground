import sqlite3

# connect to sqlite 3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text,password txt)"

cursor.execute(create_table)

usr = (1, 'bambi', 'asdf')

insert_query = "INSERT INTO users values (?,?,?)"

cursor.execute(insert_query, usr)

usrs = [
    (2, 'test_user', 'asdf'),
    (3, 'akshay', 'asdf'),
    (4, 'akki', 'asdf'),
    (5, 'hero', 'asdf')
]
cursor.executemany(insert_query, usrs)
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
