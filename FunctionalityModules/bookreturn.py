"""
Library Management System
Book Return Module:
Contains functions allowing the user to return books and performs validation
checks to ensure a successful return.
Created on 01/12/2019
By Elzbieta Stasiak-Antser
"""

import FunctionalityModules.TextFileModules.database as database
import FunctionalityModules.bookcheckout as bc
from datetime import date

databasePath = "FunctionalityModules\TextFileModules\database.txt"
logfilePath = "FunctionalityModules\TextFileModules\logfile.txt"

def returnBook(bookID):
    """The main function used to return books.

    :param bookID (String): The ID of the book to be returned.
    :return (String): A message that tells the user the return was successful
                      or an error message with details of the problem.
    """
    bookList = database.readDatabase(databasePath)
    intBookID = bc.integerCheck(bookID)

    if intBookID == -1:
        return "Book ID: "+bookID+" is not an integer, please try again."

    if not bc.validBookCheck(intBookID, bookList):
        return "Book ID: "+bookID+" is not valid, please try again with a valid ID."

    if bc.onLoanCheck(intBookID, bookList):
        return "Book with ID: "+bookID+" is already available."

    # Checks completed so return the book and edit the book list.
    bookList[intBookID - 1][4] = "0"
    database.writeDatabase(bookList, databasePath)

    # Update log file.
    logList = database.readDatabase(logfilePath)
    logList = searchLogFile(bookID, logList)
    database.writeDatabase(logList, logfilePath)
    return "Return of book with ID: "+bookID+" was successful."


def searchLogFile(bookID, logList):
    """Searches for the log of the book with the ID 'bookID' that
    hasn't been returned and updates the return date to today.

    :param bookID (String): The ID of the book to look for.
    :param logList (List): The data from the log file in list form.
    :return (List): The updated list form of the log file.
    """
    today = date.today()
    today = today.strftime("%d/%m/%Y")

    for log in logList:
        if (log[0] == bookID) and (log[2] == "0"):
            log[2] = today

    return logList

# Test code
if __name__ == "__main__":
    # Before running this module independantly, uncomment the lines below
    # and comment out the original import lines at the beginning of the file.
    #import TextFileModules.database as database
    #import bookcheckout as bc
    databasePath = "TextFileModules\database.txt"
    logfilePath = "TextFileModules\logfile.txt"
    # Valid return test
    print(returnBook("2"))
    # Invalid book ID test
    print(returnBook("67"))
    # Non-integer book ID test
    print(returnBook("abc"))
    # Already available book test
    print(returnBook("9"))
