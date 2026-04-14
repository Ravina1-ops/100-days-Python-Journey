'''
EXERCISE 6: Library Management System

Write a Library class with:
1. no_of_books (instance variable)
2. books (list instance variable to store book names)

The class should have the following methods:
- add_book(book_name): To add a book to the list and increment the count.
- show_all_books(): To print all books currently in the library.
- get_no_of_books(): To return the total number of books.

CRITICAL TASK:
Create a program that:
- Allows the user to add multiple books.
- Validates the book count: Ensure that the 'no_of_books' variable 
  always matches the actual length of the 'books' list.
- Use a check to see if your program is working correctly by 
  comparing the length of the list with the 'no_of_books' variable.

Goal: Practice Instance Variables, Methods, and Data Consistency.
'''

#  - Library Management System Solution
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are:")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Atomic Habits")
l1.showInfo()