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
        Copies INTEGER,
        Members TEXT,
        Deleted TEXT
    )'''

cursor.execute(sql_command)
conn.commit()

# def addBook(title, author, isbn, copies):
def addBook(title, author, isbn, copies):
    params = (title, author, isbn, copies)
    sql_insert = '''
        INSERT INTO bookish
            (Title, Author, ISBN, Copies, Members, Deleted)
        VALUES (
            ?, ?, ?, ?, 'None', 'False'
        )'''
    cursor.execute(sql_insert, params)
    conn.commit()
    select_data = 'SELECT * FROM bookish WHERE Deleted = "False"'
    cursor.execute(select_data)
    rows = cursor.fetchall()
    for row in rows:
            print(row)

#To see the data
def viewAllBooks():
    select_data = 'SELECT * FROM bookish WHERE Deleted = "False"'
    cursor.execute(select_data)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def searchBooks():
    search = input('What is the title of the book you want to find?')
    select_title = f'SELECT * FROM bookish WHERE Title = {search}'
    cursor.execute(select_title)
    print(cursor.fetchone())

def updateBooks(itemToBeUpdated, changeToBeMade, identifyTheBook):
    params = (changeToBeMade, identifyTheBook)
    if itemToBeUpdated == 'Title':
        sql_update = 'UPDATE bookish SET Title = ? WHERE Title = ?'
        cursor.execute(sql_update, params)
        conn.commit()
    elif itemToBeUpdated == 'Author':
        sql_update = 'UPDATE bookish SET Author = ? WHERE Title = ?'
        cursor.execute(sql_update, params)
        conn.commit()
    elif itemToBeUpdated == 'ISBN':
        sql_update = 'UPDATE bookish SET ISBN = ? WHERE Title = ?'
        cursor.execute(sql_update, params)
        conn.commit()
    elif itemToBeUpdated == 'Copies':
        sql_update = 'UPDATE bookish SET Copies = ? WHERE Title = ?'
        cursor.execute(sql_update, params)
        conn.commit()
    elif itemToBeUpdated == 'Members':
        sql_update = 'UPDATE bookish SET Members = ? WHERE Title = ?'
        cursor.execute(sql_update, params)
        conn.commit()
    else:
        print('There is no such column')
    viewAllBooks()
    print('\nYou have sucessfully updated the database')

# sql_view = 'SELECT * FROM bookish WHERE Title = {search}'
# cursor.execute(sql_view)
# book1 = cursor.fetchone()
# print(book1)


# sql_delete = ''' DELETE FROM bookish WHERE id = 2'''
# cursor.execute(sql_delete)
# conn.commit()


sql_delete = '''
    CREATE TABLE IF NOT EXISTS deletedfrombookish (
        Id,
        Title TEXT, 
        Author TEXT, 
        ISBN TEXT,
        Copies INTEGER,
        Members TEXT,
        Deleted TEXT
    )'''
cursor.execute(sql_delete)
conn.commit()

def delete_books(title):
    param = title
    sql_deleted = 'UPDATE bookish SET Deleted = "True" WHERE Title = ?'
    cursor.execute(sql_deleted, param)
    conn.commit()
    sql_safe_delete = '''INSERT INTO deletedfrombookish SELECT * FROM bookish WHERE Deleted = 'True' '''
    cursor.execute(sql_safe_delete)
    conn.commit()
    viewAllBooks()
    print(f'You have deleted {title}')

# conn.close()

# foreigh key to primary key, composite key

# Create a SQL Table
# sql_member_table = '''
#     CREATE TABLE IF NOT EXISTS membership (
#         Id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Firstname TEXT,
#         Lastname TEXT,
#         BookIds INTEGER,
#         Deleted TEXT
#     )'''
# cursor.execute(sql_command)
# conn.commit()

# sql_insert_new_member = '''
#     INSERT INTO membership
#         (Firstname, Lastname, BookIds, Deleted)
#     VALUES (
#         'Boe', 'Faceof', 1, 'false'
#     )
# '''

# SELECT * FROM membership WHERE book.bookID = BookCopy.BookID
