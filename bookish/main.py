from importFile import *


# Main Menu
def mainMenu():
    menuOption = input('Welcome \n What would you like to do today? \n 1. Add New Book \n 2. See all books \n 3. Update Book details \n 4. Delete Book \n 5. Quit')
    if menuOption == '1':
        title = input('Please enter Book Title')
        author = input('Please Enter Author Name')
        ISBN = input('Please Enter Book ISBN')
        copies = input('Please Enter Number of Copies')
        addBook(title, author, ISBN, copies)
        mainMenu()
    elif menuOption == '2':
        viewAllBooks()
        mainMenu()
    elif menuOption == '3':
        itemToBeUpdated = input('What would you like to update? (Title, Author, ISBN, Copies)')
        changeToBeMade = input('What would you like to change this to?')
        identifyTheBook = input('What is the Title of the book you wish to change?')
        updateBooks(itemToBeUpdated, changeToBeMade, identifyTheBook)
        mainMenu()
    elif menuOption == '4':
        titleToDelete = input('What is the Title of the Book you would like to delete?')
        delete_books(titleToDelete)
        mainMenu()
    elif menuOption == '5':
        conn.close()
        print('My Time is Limited. You must Ask The Right Questions...\n Programme Terminated.')

mainMenu();



