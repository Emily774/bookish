import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('database.db')
except Error as e:
    print(e)

# Create a cursor to allow to execute SQL commands
cursor = conn.cursor()

# Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS bookish (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Title TEXT, 
        Author TEXT, 
        ISBN TEXT,
        Copies INTEGER
    )'''

cursor.execute(sql_command)
# Commit the changes to the database
conn.commit()

sql_insert = '''
    INSERT INTO bookish
        (Title, Author, ISBN, Copies)
    VALUES (
        'Do Androids Dream of Electric Sheep?', 'Isaac Asimov', 'AI2413000', 13
    )
'''
cursor.execute(sql_insert)
conn.commit()

select_data = 'SELECT * FROM bookish'
cursor.execute(select_data)
# row = cursor.fetchone()
# print(row)

rows = cursor.fetchall()
for row in rows:
    print(row)

# manyrows = cursor.fetchmany(2)
# for row in manyrows:
#     print(row)

# sql_view = '''SELECT * FROM contacts WHERE Firstname = '''
# sql_update = '''
#
#
# '''
#
# cursor.execute(sql_update)
# conn.commit()
#
# sql_delete = '''
#
#
# '''
#
# cursor.execute(sql_delete)
# conn.commit()

conn.close()