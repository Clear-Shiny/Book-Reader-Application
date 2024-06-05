from Book import Book
from Books_Data import List_of_Books
from BookReader import BookReader

book_reader = BookReader()

for book in List_of_Books:
    book_reader.add_book(book)

book_reader.start()
