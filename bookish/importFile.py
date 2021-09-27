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
    CREATE TABLE IF NOT EXISTS contacts (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Firstname TEXT, 
        Lastname TEXT, 
        Email TEXT
    )'''

cursor.execute(sql_command)
print('here')
# Commit the changes to the database
conn.commit()

conn.close()