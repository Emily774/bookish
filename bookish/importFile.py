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


sql_member_table = '''
    CREATE TABLE IF NOT EXISTS membership (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Firstname TEXT,
        Lastname TEXT,
        Email Text,
        BookIds INTEGER,
        Deleted TEXT
    )'''
cursor.execute(sql_member_table)
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






def delete_books(titleToDelete):
    param = (titleToDelete, )
    sql_delete_is_true = '''UPDATE bookish SET Deleted = "True" WHERE Title = ?'''
    cursor.execute(sql_delete_is_true, param)
    conn.commit()
    sql_insert_into_deleted_database = '''INSERT INTO deletedfrombookish
    SELECT * FROM bookish WHERE Title = ? '''
    cursor.execute(sql_insert_into_deleted_database, param)
    conn.commit()
    sql_delete = ''' DELETE FROM bookish WHERE Title = ?'''
    cursor.execute(sql_delete, param)
    conn.commit()
    viewAllBooks()
    print(f'\nYou have deleted {titleToDelete}\n')


# foreigh key to primary key, composite key

def addMember(Firstname, Lastname, Email):
    param = (Firstname, Lastname, Email)
    sql_insert_new_member = '''
        INSERT INTO membership
            (Firstname, Lastname, Email, BookIds, Deleted)
        VALUES (
            ?, ?, ?, 0, 'False'
        )
    '''
    cursor.execute(sql_insert_new_member, param)
    conn.commit()
    select_data = 'SELECT * FROM membership WHERE Deleted = "False"'
    cursor.execute(select_data)
    rows = cursor.fetchall()
    for row in rows:
            print(row)
    print(f'You have sucessfully added {Firstname} {Lastname} at {Email} to the membership database')

def viewAllMembers():
    select_data = 'SELECT * FROM membership WHERE Deleted = "False"'
    cursor.execute(select_data)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def deleteMembers(firstNameToDelete, lastNameToDelete):
    param = (firstNameToDelete, lastNameToDelete)
    sql_delete_is_true = '''UPDATE membership SET Deleted = "True" WHERE Firstname = ? AND Lastname = ?'''
    cursor.execute(sql_delete_is_true, param)
    conn.commit()
    sql_insert_into_deleted_database = '''INSERT INTO deletedfrombookish
    SELECT * FROM membership WHERE Firstname = ? AND Lastname = ? '''
    cursor.execute(sql_insert_into_deleted_database, param)
    conn.commit()
    # pretty sure up to here works
    sql_delete = ''' DELETE FROM membership WHERE Firstname = ? AND Lastname = ?'''
    cursor.execute(sql_delete, param)
    conn.commit()
    viewAllMembers()
    print(f'\nYou have deleted {firstNameToDelete}{lastNameToDelete}\n')

def addBookToMember(memberFirstname, memberLastname):
    param = (memberFirstname, memberLastname)
    findMember = 'SELECT * FROM membership WHERE Firstname = ? AND Lastname = ?'
    cursor.execute(findMember, param)
    conn.commit()



# SELECT * FROM membership WHERE book.bookID = BookCopy.BookID

# connect a book to a member
# link member id in membership to bookish Members
# - make it so the new id is added along side the old
# - make it so every time a member is added the number in copies decreases
# - make it so the number of copies can't go below zero

# Part1 Check out book to member


# Part2 link book to member
# def searchForMember
# param = (firstName, LastName)
# firstName = input('What is the firstname of the member you wish to look for?')
# lastNamte = input('What is the lastname of the member you wish to look for?')
# searchForMember = 'SELECT id FROM membership WHERE Firstname = ? AND Lastname = ?'
# cursor.execute(searchForMember, param)
# conn.commit()

# def seeMembersBooks(membersId)
# param = (membersId, )
# sql_identify_member = 'SELECT * FROM bookish WHERE members = ?'
# cursor.execute(sql_identify_member, param)
# con.commit

# Might have to iterate through each item in bookish.members in a loop then pass each one as a param into the below statement
# for bookish.members as id:
# 'SELECT * FROM membership, bookish WHERE members.id = bookish.members'
#