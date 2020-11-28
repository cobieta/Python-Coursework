"""
Library Management System
Book List Module:
Lists books according to different criteria of popularity and generates
data lists that the menu module can use to display as a graph.
Created on 02/12/2019
By Elzbieta Stasiak-Antser
"""

import FunctionalityModules.TextFileModules.database as database
from datetime import date, timedelta

databasePath = "FunctionalityModules\TextFileModules\database.txt"
logfilePath = "FunctionalityModules\TextFileModules\logfile.txt"

def createTitleList():
    """Create a list of all the book titles.

    :return (List): The list of titles.
    """
    bookList = database.readDatabase(databasePath)
    titleList = []
    for book in bookList:
        titleList.append(book[1])

    return titleList

def lifetimeBorrows():
    """Gives the list of the total times each book has been borrowed.

    :return (List(List, String)): The popularity list and the name of the popularity criteria.
    """
    logList = database.readDatabase(logfilePath)
    popList = [0,0,0,0,0,0,0,0,0,0]
    for log in logList:
        if log != ['']:
            popList[int(log[0]) - 1] = popList[int(log[0]) - 1] + 1

    return [popList, "Number of borrows since the book was bought"]

def averageLifetimeBorrows():
    """Gives a list of book titles in order of highest average borrows
    since the book was bought.

    :return (List(List, String)): The popularity list and the name of the popularity criteria.
    """
    bookList = database.readDatabase(databasePath)
    today = date.today()
    avrPopList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    lifePopList = lifetimeBorrows()
    for book in bookList:
        bookIndex = bookList.index(book)
        # Split the stored date into separate components.
        separateDate = book[3].split('/')
        # Convert the date parts into integers.
        separateDate = [int(i) for i in separateDate]
        # Calculate the days since the purchase of the book.
        days = today - date(separateDate[2], separateDate[1], separateDate[0])
        # Calculate the average borrows for each book.
        avrPopList[bookIndex] = lifePopList[0][bookIndex] / days.days

    return [avrPopList, "Average borrows since the book was bought"]

def yearBorrows():
    """Gives the list of how many times each book has been borrowed
    in the last year.

    :return (List(List, String)): The popularity list and the name of the popularity criteria.
    """
    logList = database.readDatabase(logfilePath)
    popList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    today = date.today()
    date1YearAgo = today - timedelta(days=365)

    for log in logList:
        if log != ['']:
            separateDate = log[1].split('/')
            separateDate = [int(i) for i in separateDate]
            dateOfWithdrawal = date(separateDate[2], separateDate[1], separateDate[0])
            if dateOfWithdrawal >= date1YearAgo:
                popList[int(log[0]) - 1] = popList[int(log[0]) - 1] + 1

    return [popList, "Number of borrows in the last year"]

def averageYearBorrows():
    """Gives a list of book titles in order of highest average borrows
    in the last year.

    :return (List(List, String)): The popularity list and the name of the popularity criteria.
    """
    bookList = database.readDatabase(databasePath)
    avrPopList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    yearPopList = yearBorrows()
    for book in bookList:
        bookIndex = bookList.index(book)
        # Calculate the average borrows for each book.
        avrPopList[bookIndex] = yearPopList[0][bookIndex] / 365

    return [avrPopList, "Average borrows in the last year"]

def monthBorrows():
    """Gives the list of how many times each book has been borrowed
    in the last month.

    :return (List(List, String)): The popularity list and the name of the popularity criteria.
    """
    logList = database.readDatabase(logfilePath)
    popList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    today = date.today()
    date1MonthAgo = today - timedelta(days=30)

    for log in logList:
        if log != ['']:
            separateDate = log[1].split('/')
            separateDate = [int(i) for i in separateDate]
            dateOfWithdrawal = date(separateDate[2], separateDate[1], separateDate[0])
            if dateOfWithdrawal >= date1MonthAgo:
                popList[int(log[0]) - 1] = popList[int(log[0]) - 1] + 1

    return [popList, "Number of borrows in the last month"]

def averageMonthBorrows():
    """Gives a list of book titles in order of highest average borrows
    in the last month.

    :return (List(List, String)): The popularity list and the name of the popularity criteria.
    """
    bookList = database.readDatabase(databasePath)
    avrPopList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    monthPopList = monthBorrows()
    for book in bookList:
        bookIndex = bookList.index(book)
        # Calculate the average borrows for each book.
        avrPopList[bookIndex] = monthPopList[0][bookIndex] / 30

    return [avrPopList, "Average borrows in the last month"]

# Test code
if __name__ == "__main__":
    # Before running this module independantly, uncomment the line below
    # and comment out the original import line at the beginning of the file.
    #import TextFileModules.database as database
    databasePath = "TextFileModules\database.txt"
    logfilePath = "TextFileModules\logfile.txt"
    # Test the list of titles can be created.
    testList = createTitleList()
    print(testList)
    # Test the total number of borrows.
    testList = lifetimeBorrows()
    print(testList[1])
    print(testList[0])
    # Test the borrows within the last year.
    testList = yearBorrows()
    print(testList[1])
    print(testList[0])
    # Test the borrows within the last month.
    testList = monthBorrows()
    print(testList[1])
    print(testList[0])
    # Test the average total number of borrows.
    testList = averageLifetimeBorrows()
    print(testList[1])
    print(testList[0])
    # Test the average number of borrows this year.
    testList = averageYearBorrows()
    print(testList[1])
    print(testList[0])
    # Test the average number of borrows this month.
    testList = averageMonthBorrows()
    print(testList[1])
    print(testList[0])
