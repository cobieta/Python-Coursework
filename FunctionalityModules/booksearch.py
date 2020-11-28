"""
Library Management System
Book Search Module:
Contains functions allowing the user to search for books by entering their title.
Created on 28/11/2019
By Elzbieta Stasiak-Antser
"""

from FunctionalityModules.TextFileModules.database import readDatabase

databasePath = "FunctionalityModules\TextFileModules\database.txt"

def searchTitle(title):
    """Search for books that contain the title parameter in their title.

    :param title (String): The Title of the book to search for.
    :return (List): The books found as a list or an empty list if no books are found.
    """
    database = readDatabase(databasePath)
    foundBooks = []
    for book in database:
        if title in book[1]:
            foundBooks.append(book)
    return foundBooks

def displayBook(bookList):
    """Only used to test this module by printing book information to the console.

    :param bookList (List): The list of books found by the search function.
    """
    for bookRecord in bookList:
        print("\nID:", bookRecord[0])
        print("Title:", bookRecord[1])
        print("Author:", bookRecord[2])
        print("Date Bought:", bookRecord[3])
        print("ID of borrower:", bookRecord[4])


# Test code
if __name__ == "__main__":
    # Before running this module independantly, uncomment the line below
    # and comment out the original import line at the beginning of the file.
    #from TextFileModules.database import readDatabase
    databasePath = "TextFileModules\database.txt"
    
    # Valid title search test
    validBook = searchTitle("Hood")
    print("\nBooks found from searching for 'Hood':")
    displayBook(validBook)

    # Multiple title search test
    multBook = searchTitle("The")
    print("\nBooks found from searching 'The':")
    displayBook(multBook)

    # Invalid title search test
    invalidBook = searchTitle("xyz")
    print("\nBooks found from searching 'xyz':")
    if invalidBook == []:
        print("\nTest successful.\n")
