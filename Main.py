from Book import Book
from Books_Data import List_of_Books
from BookReader import BookReader
from UI import BookReaderUI

def calculate_edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

book_reader = BookReader()

for book_data in List_of_Books:
    book = Book(*List_of_Books)
    book_reader.add_book(book)

book_reader_ui = BookReaderUI(book_reader)
book_reader_ui.start()
