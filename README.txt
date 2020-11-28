A few notes on my program:
 - When a book is in the library and not currently on loan, 
   if you search for the book, the member ID will be displayed 
   as '0' because that is what is stored in the database. 
 - All valid IDs are between 1000 and 9999.
 - Books that are still on loan have their return date set
   to '0' in the logfile instead of a date.
 - The functions in the booklist module that calculate an 
   average, use the number of times a book has been checked-out
   and divide by the number of days the function describes it 
   looks at. For example the averageMonthBorrows function counts
   how many times a book has been checked out in the last 30 days 
   and calculates the average by dividing that number by 30.
   A higher average means a book has been taken out more frequently.


