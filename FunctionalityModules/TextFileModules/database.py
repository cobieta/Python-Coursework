"""
Library Management System
Database Module:
Contains all functions used to read and write to the logfile and database file.
Created on 28/11/2019
By Elzbieta Stasiak-Antser
"""

def readDatabase(filename):
    """Reads the database or log file and converts its data into a list with
    each book record being its own list.

    :param filename (String): The name of the file to be read.
    :return (List): The list of records of books.
    """
    booklist = []
    databaseFile = open(filename, "r")

    for record in databaseFile:
        cleanDatabase = record.strip()
        bookrecord = cleanDatabase.split(",")
        booklist.append(bookrecord)

    databaseFile.close()
    return booklist


def writeDatabase(bookList, filename):
    """Writes the list of books to the database file.

    :param bookList (List): The list of books to be written.
    :param filename (String): The name of the file to be written to.
    """
    file = open(filename, "w")
    for record in bookList:
        recordString = ",".join(record)
        recordString = recordString + "\r"
        file.write(recordString)

    file.close()
    return


def appendLogfile(newLog, filename):
    """Appends new lines to the log file.

    :param newLog (String): The new line to be added to the end of the log file.
    :param filename (String): The name of the logfile.
    """
    file = open(filename, "a")
    file.write(newLog)
    file.close()
    return

