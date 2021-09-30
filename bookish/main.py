from importFile import *


# Main Menu
def mainMenu():
    menuOption = input('Welcome \n What would you like to do today? \n 1. Add New Book \n 2. See all books \n 3. Update Book details \n 4. Delete Book \n 5. Quit \n 6. Add New Member \n 7. View All Members \n 8. Delete Member \n 9. Add book to member')
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
    elif menuOption == '6':
        Firstname = input('Please enter new member\'s first name')
        Lastname = input('Please enter new member\'s last name')
        Email = input('Please enter new member\'s email address')
        addMember(Firstname, Lastname, Email)
        mainMenu()
    elif menuOption == '7':
        viewAllMembers()
        mainMenu()
    elif menuOption == '8':
        firstNameToDelete = input('What is the first name of the member you would like to delete?')
        lastNameToDelete = input('What is the Last Name of the member you would like to delete?')
        deleteMembers(firstNameToDelete, lastNameToDelete)
        mainMenu()
    elif menuOption == '9':
        memberFirstname = input('Please type the member\'s first name)
        memberLastname = input('Please type the member\'s last name')

    else:
        print('You have entered an invalid menu option. Please try again.')
        mainMenu()


mainMenu();



