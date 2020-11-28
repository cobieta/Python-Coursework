"""
Library Management System
Menu Module:
The main program that is run and allows the user to access all the functions
of the library system. It also contains all the tkinter user interface code.
Created on 28/11/2019
By Elzbieta Stasiak-Antser
"""

import FunctionalityModules.bookcheckout as bookcheckout
import FunctionalityModules.booksearch as booksearch
import FunctionalityModules.bookreturn as bookreturn
import FunctionalityModules.booklist as booklist
from tkinter import *
from tkinter import font, _setit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def raiseFrame(frame):
    """Called by the GUI buttons to switch between frames.

    :param frame (tkinter Frame): The frame to bring forward.
    """
    frame.tkraise()
    return

def backAndClear(label):
    """Called by the back buttons on the GUI frames to clear the last
    message displayed and switch frames to the mainMenu frame.

    :param label (tkinter Label): The label widget that needs its text to be cleared.
    """
    label.configure(text="")
    raiseFrame(mainMenu)
    return


def checkoutCall():
    """Called when the checkout button is pressed to call the 'bookcheckout'
    module to checkout a book and clear the text entry boxes.
    """
    memberID = memberEntry.get()
    bookID = bookEntryC.get()
    bookEntryC.delete(0, END)
    memberEntry.delete(0, END)
    message = bookcheckout.checkout(memberID, bookID)
    messageLblC.configure(text=message)
    return

def returnCall():
    """Called when the return button is pressed to call the 'bookreturn'
    module to return a book and clear the text entry boxes.
    """
    bookID = bookEntryR.get()
    bookEntryR.delete(0, END)
    message = bookreturn.returnBook(bookID)
    messageLblR.configure(text=message)
    return

def searchCall():
    """Called when the search button is pressed to call the 'bookSearch'
    module and find the list of books that contain the title entered.
    """
    titleEntered = titleEntry.get()
    booksFound.clear()
    booksFound.extend(booksearch.searchTitle(titleEntered))
    if booksFound == []:
        message = "Title not found, try searching again with a different title."
        messageLblS.configure(text=message)
    else:
        message = "Found " + str(len(booksFound)) + " books with the title: " + titleEntered
        messageLblS.configure(text=message)
        bookMenu['menu'].delete(0, 'end')
        for book in booksFound:
            bookMenu['menu'].add_command(label=book[1], command=_setit(chosenBook, book[1]))
        bookMenu.configure(state=NORMAL)
    return

def bookSelect(*args):
    """Called when the user selects a book from the drop down menu of books found
    and configures the Label widgets in the GUI to display the books information.

    :param *args: Reads all arguments sent to the function.
    """
    bookSelection = chosenBook.get()
    for book in booksFound:
        if bookSelection == book[1]:
            IDinfoLbl.configure(text=book[0])
            titleInfoLbl.configure(text=book[1])
            authorInfoLbl.configure(text=book[2])
            dateBoughtInfoLbl.configure(text=book[3])
            borrowerIDinfoLbl.configure(text=book[4])
    return

def clearSearch():
    """Called by the back button on the search frame to clear the search
    messages and switch frames back to the main menu.
    """
    booksFound.clear()
    messageLblS.configure(text="")
    chosenBook.set("Select a book")
    bookMenu.config(state=DISABLED)
    IDinfoLbl.configure(text="")
    titleInfoLbl.configure(text="")
    authorInfoLbl.configure(text="")
    dateBoughtInfoLbl.configure(text="")
    borrowerIDinfoLbl.configure(text="")
    titleEntry.delete(0, END)
    raiseFrame(mainMenu)
    return

def graphSelect(*args):
    """Called when the user selects a popularity criteria from the drop down menu
    of criteria and displays the graph of this data using the matplotlib library.

    :param *args: Reads all arguments sent to the function.
    """
    graphSelection = chosenCriteria.get()
    if graphSelection == "Lifetime borrows":
        data = booklist.lifetimeBorrows()
    elif graphSelection == "Average lifetime borrows":
        data = booklist.averageLifetimeBorrows()
    elif graphSelection == "Year borrows":
        data = booklist.yearBorrows()
    elif graphSelection == "Average year borrows":
        data = booklist.averageYearBorrows()
    elif graphSelection == "Month borrows":
        data = booklist.monthBorrows()
    elif graphSelection == "Average month borrows":
        data = booklist.averageMonthBorrows()
    # Create the graph as a bar chart and display it.
    titleList = booklist.createTitleList()
    figure = Figure(figsize=(6.5, 3.5), dpi=100, constrained_layout=True)
    graph = figure.add_subplot(111)
    graph.bar(titleList, data[0])
    graph.set_title(data[1])
    canvas = FigureCanvasTkAgg(figure, listMenu)
    canvas.draw()
    # Rotate the book labels on the x-axis and make sure they don't overlap.
    xticklabels = graph.get_xticklabels()
    for tick in xticklabels:
        tick.set_rotation(50)
        tickText = tick.get_text()
        if len(tickText) > 10:
            wordList = tickText.split()
            newText = ""
            for word in wordList:
                if len(word) < 5:
                    newText = newText + word + " "
                else:
                    newText = newText + word + "\n"
            tick.set_text(newText)
    graph.set_xticklabels(xticklabels)
    # Place the graph in the user interface.
    canvas.get_tk_widget().place(x=20, y=130)
    return

def loadGraph():
    """Loads the graph to make sure it displays the current data
    and switches the frame to the 'listMenu' frame.
    """
    graphSelect()
    raiseFrame(listMenu)


# Main Program and user interface.

# Initialise the window.
window = Tk()
window.title("Library System")
window.geometry("700x500")

# Create each separate frame.
mainMenu = Frame(window)
searchMenu = Frame(window)
checkoutMenu = Frame(window)
returnMenu = Frame(window)
listMenu = Frame(window)
for frame in (mainMenu, searchMenu, checkoutMenu, returnMenu, listMenu):
    frame.place(width=700, height=500)

# fonts
titleFont = font.Font(family="Arial", size=28, weight="bold")
btnFont = font.Font(family="Arial", size=14)

# mainMenu widgets:
title = "Welcome to the library system"
heading = Label(mainMenu, text=title, font=titleFont)
heading.place(x=100, y=75)
listBksBtn = Button(mainMenu,text="List Books",font=btnFont,command=loadGraph)
listBksBtn.place(x=310, y=150)
searchBksBtn = Button(mainMenu,text="Search Books",font=btnFont,command=lambda:raiseFrame(searchMenu))
searchBksBtn.place(x=295, y=210)
checkoutBksBtn = Button(mainMenu,text="Check-out Books",font=btnFont,command=lambda:raiseFrame(checkoutMenu))
checkoutBksBtn.place(x=285, y=270)
returnBksBtn = Button(mainMenu,text="Return Books",font=btnFont,command=lambda:raiseFrame(returnMenu))
returnBksBtn.place(x=300, y=330)

# checkoutMenu widgets:
checkoutHeading = Label(checkoutMenu, text="Checkout a book", font=titleFont)
checkoutHeading.place(x=200, y=75)
memberLblText = "Enter the ID of the member who wants to checkout a book:"
memberLbl = Label(checkoutMenu,text=memberLblText, font=btnFont)
memberLbl.place(x=100,y=150)
memberEntry = Entry(checkoutMenu, font=btnFont)
memberEntry.place(x=250, y=200)
bookLblTextC = "Enter the ID of the book to be withdrawn:"
bookLblC = Label(checkoutMenu,text=bookLblTextC,font=btnFont)
bookLblC.place(x=100, y=250)
bookEntryC = Entry(checkoutMenu, font=btnFont)
bookEntryC.place(x=250, y=300)
checkoutBtn = Button(checkoutMenu,text="Check-out",font=btnFont,command=checkoutCall)
checkoutBtn.place(x=310,y=350)
messageLblC = Label(checkoutMenu,text="",font=btnFont)
messageLblC.place(x=100, y=400)
backBtnC = Button(checkoutMenu,text="Back",font=btnFont,command=lambda:backAndClear(messageLblC))
backBtnC.place(x=330, y=450)

# returnMenu widgets:
returnHeading = Label(returnMenu,text="Return a book", font=titleFont)
returnHeading.place(x=200, y=75)
bookLblTextR = "Enter the ID of the book to be returned:"
bookLblR = Label(returnMenu,text=bookLblTextR,font=btnFont)
bookLblR.place(x=100, y=150)
bookEntryR = Entry(returnMenu, font=btnFont)
bookEntryR.place(x=250, y=200)
returnBtn = Button(returnMenu,text="return",font=btnFont,command=returnCall)
returnBtn.place(x=320, y=250)
messageLblR = Label(returnMenu,text="",font=btnFont)
messageLblR.place(x=100, y=300)
backBtnR = Button(returnMenu,text="Back",font=btnFont,command=lambda:backAndClear(messageLblR))
backBtnR.place(x=325, y=350)

# searchMenu widgets:
searchHeading = Label(searchMenu,text="Search for a book", font=titleFont)
searchHeading.place(x=200, y=25)
bookTitleText = "Enter the title of the book to search for:"
bookTitleLbl = Label(searchMenu,text=bookTitleText,font=btnFont)
bookTitleLbl.place(x=100, y=100)
titleEntry = Entry(searchMenu, font=btnFont)
titleEntry.place(x=100, y=150)
searchGoBtn = Button(searchMenu,text="Search",font=btnFont,command=searchCall)
searchGoBtn.place(x=350, y=150)
messageLblS = Label(searchMenu, text="", font=btnFont)
messageLblS.place(x=100, y=200)
backBtnS = Button(searchMenu,text="Back",font=btnFont,command=clearSearch)
backBtnS.place(x=450, y=150)
# List of books found by search:
chosenBook = StringVar(searchMenu)
chosenBook.set("Select a book")
bookMenu = OptionMenu(searchMenu, chosenBook, value="Select a book")
bookMenu.config(font=btnFont, state=DISABLED)
bookMenu.place(x=100, y=250)
booksFound = []
# Display the information of the book selected:
IDLbl = Label(searchMenu, text="ID:", font=btnFont)
IDLbl.place(x=100, y=300)
IDinfoLbl = Label(searchMenu, text="", font=btnFont)
IDinfoLbl.place(x=250, y=300)
titleLbl = Label(searchMenu, text="Title:", font=btnFont)
titleLbl.place(x=100, y=330)
titleInfoLbl = Label(searchMenu, text="", font=btnFont)
titleInfoLbl.place(x=250, y=330)
authorLbl = Label(searchMenu, text="Author:", font=btnFont)
authorLbl.place(x=100, y=360)
authorInfoLbl = Label(searchMenu, text="", font=btnFont)
authorInfoLbl.place(x=250, y=360)
dateBoughtLbl = Label(searchMenu, text="Date Bought:", font=btnFont)
dateBoughtLbl.place(x=100, y=390)
dateBoughtInfoLbl = Label(searchMenu, text="", font=btnFont)
dateBoughtInfoLbl.place(x=250, y=390)
borrowerIDLbl = Label(searchMenu, text="ID of Borrower:", font=btnFont)
borrowerIDLbl.place(x=100, y=420)
borrowerIDinfoLbl = Label(searchMenu, text="", font=btnFont)
borrowerIDinfoLbl.place(x=250, y=420)
chosenBook.trace("w", bookSelect)

# listMenu widgets
listHeading = Label(listMenu,text="Book Popularity",font=titleFont)
listHeading.place(x=200, y=25)
chosenCriteria = StringVar(listMenu)
criteriaList = ["Lifetime borrows", "Average lifetime borrows", "Year borrows",
                "Average year borrows", "Month borrows", "Average month borrows"]
chosenCriteria.set(criteriaList[0])
criteriaMenu = OptionMenu(listMenu, chosenCriteria, *criteriaList)
criteriaMenu.config(font=btnFont)
criteriaMenu.place(x=100, y=85)
chosenCriteria.trace("w", graphSelect)
backBtnL = Button(listMenu,text="Back",font=btnFont,command=lambda:raiseFrame(mainMenu))
backBtnL.place(x=500, y=85)

# Starting frame.
raiseFrame(mainMenu)
window.mainloop()
