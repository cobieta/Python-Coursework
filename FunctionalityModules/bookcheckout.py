"""
Library Management System
Book Checkout Module:
Contains functions allowing the user to checkout books and performs validation
checks to ensure a successful checkout.
Created on 29/11/2019
By Elzbieta Stasiak-Antser
"""

from datetime import date
import FunctionalityModules.TextFileModules.database as database

databasePath = "FunctionalityModules\TextFileModules\database.txt"
logfilePath = "FunctionalityModules\TextFileModules\logfile.txt"

def checkout(memberID, bookID):
    """The main function used to withdraw books.
    All parameters are entered as strings.

    :param memberID (String): The ID of the library member who wants to withdraw a book.
    :param bookID (String): The ID of the book to be withdrawn.
    :return (String): a message that confirms the book has been checked out or an
    error message.
    """
    bookList = database.readDatabase(databasePath)
    intMemberID = integerCheck(memberID)
    intBookID = integerCheck(bookID)
    if intMemberID == -1:
        return "Member ID: "+memberID+" was not an integer, please try again."
    elif intBookID == -1:
        return "Book ID: "+bookID+" was not an integer, please try again."

    if not validMemberCheck(intMemberID):
        return "Member ID: "+memberID+" not valid, please try again with a valid ID."

    if not validBookCheck(intBookID, bookList):
        return "Book ID: "+bookID+" not valid, please try again with a valid ID."

    if not onLoanCheck(intBookID, bookList):
        return "Book with ID: "+bookID+" is already on loan to another member."

    # Checks completed so withdraw the book and edit book list
    bookList[intBookID - 1][4] = memberID
    database.writeDatabase(bookList, databasePath)

    # Update the log file
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    newLog = bookID + "," + today + ",0\r"
    database.appendLogfile(newLog, logfilePath)
    return "Checkout of book with ID: "+bookID+" was successful."


def integerCheck(IDvariable):
    """Checks the IDs of the library member and book have been entered as
    integers so that the program won't crash if they're not.

    :param IDvariable (String): The ID value to check.
    :return (Int): The value of IDvariable as an integer or -1 if
    it couldn't be converted.
    """
    try:
        canBeConverted = int(IDvariable)
    except ValueError:
        canBeConverted = -1

    return canBeConverted

def validMemberCheck(memberID):
    """Check the ID of the library member to make sure it is valid.

    :param memberID (Int): The ID of the library member.
    :return (Bool): A boolean value that is True only if the ID was valid.
    """
    validID = False
    # Valid IDs are between 1000 and 9999
    if (memberID >= 1000) and (memberID <= 9999):
        validID = True

    return validID

def validBookCheck(bookID, booklist):
    """Check the ID of the book to make sure it is in the book database.

    :param bookID (Int): The ID of the book.
    :param booklist (List): The list containing all books from the database file.
    :return (Bool): A boolean value that is True only if the ID was valid.
    """
    validID = False
    # Valid IDs are between 1 and the number of records in booklist.
    if (bookID >= 1) and (bookID <= len(booklist)):
        validID = True

    return validID

def onLoanCheck(bookID, booklist):
    """Check if the book is already being loaned to another person.

    :param bookID (Int): The ID of the book.
    :param booklist (List): The list containing all books from the database file.
    :return (Bool): A boolean value that is True only if the book is available.
    """
    available = False
    book = booklist[bookID - 1]
    if book[4] == "0":
        available = True

    return available

# Test Code
if __name__ == "__main__":
    # Before running this module independantly, uncomment the line below
    # and comment out the original import line at the beginning of the file.
    #import TextFileModules.database as database
    databasePath = "TextFileModules\database.txt"
    logfilePath = "TextFileModules\logfile.txt"
    # Valid Checkout test
    print(checkout("1234", "10"))
    # Invalid member ID test
    print(checkout("456789", "1"))
    # Invalid book ID test
    print(checkout("1234", "67"))
    # Non-integer member ID test
    print(checkout("abc", "1"))
    # Non-integer book ID test
    print(checkout("1234", "abc"))
    # Already loaned book test
    print(checkout("1234", "1"))
