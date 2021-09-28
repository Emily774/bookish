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

# Commit the changes to the database
conn.commit()

sql_insert = '''
    INSERT INTO contacts
        (Firstname, Lastname, Email)
    VALUES (
        'Lols', 'Chocolate', 'lols@chocolate.com'
    )

'''

conn.close()