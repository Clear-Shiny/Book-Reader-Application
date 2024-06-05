import os
from Book import Book

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

class BookReader:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self, books):
        if books:
            for i, book in enumerate(books):
                genres = ", ".join(book.genres)
                print(f"{i+1}. {book.title} by {book.author} ({genres})")
        else:
            print("No books available.")

    def search_books_by_author(self, author):
        found_books = []
        author_lower = author.lower()
        for book in self.books:
            if author_lower == book.author.lower():
                found_books.append(book)
            elif calculate_edit_distance(author_lower, book.author.lower()) <= 2:
                found_books.append(book)

        if found_books:
            print(f"Books by {author}:")
            self.list_books(found_books)
            self.choose_book(found_books)
        else:
            print(f"No books found by {author}.")

    def search_books_by_genre(self, genre):
        found_books = []
        genre_lower = genre.lower()
        for book in self.books:
            if genre_lower in [g.lower() for g in book.genres]:
                found_books.append(book)
            elif calculate_edit_distance(genre_lower, book.genres[0].lower()) <= 2:
                found_books.append(book)

        if found_books:
            print(f"Books in the {genre} genre:")
            self.list_books(found_books)
            self.choose_book(found_books)
        else:
            print(f"No books found in the {genre} genre.")

    def search_books_by_series(self, series):
        found_books = []
        series_lower = series.lower()
        for book in self.books:
            if series_lower == book.series.lower():
                found_books.append(book)
            elif calculate_edit_distance(series_lower, book.series.lower()) <= 2:
                found_books.append(book)

        if found_books:
            print(f"Books in the {series} series:")
            self.list_books(found_books)
            self.choose_book(found_books)
        else:
            print(f"No books found in the {series} series.")

    def search_books_by_title_first_letter(self, letter):
        found_books = [book for book in self.books if book.title.lower().startswith(letter.lower())]
        if found_books:
            print(f"Books with titles starting with the letter '{letter}':")
            self.list_books(found_books)
            self.choose_book(found_books)
        else:
            print(f"No books found with titles starting with the letter '{letter}'.")

    def search_books_by_line(self, line):
        found_books = []
        line_lower = line.lower()
        for book in self.books:
            with open(book.file_path, 'r') as f:
                for file_line in f:
                    if line_lower in file_line.lower():
                        found_books.append(book)
                        break

        if found_books:
            print(f"Books containing the line '{line}':")
            self.list_books(found_books)
            self.choose_book(found_books)
        else:
            print(f"No books found containing the line '{line}'.")

    def search_books(self):
        while True:
            search_choice = input("Search books by Author (A), Genre (G), Series (S), Title (T), First letter of the title (F), Lines (L), Back to the start (B), or Exit now (E)? Enter the letter of your choice: ")
            if search_choice.upper() == "A":
                author = input("Enter the author's name: ")
                self.search_books_by_author(author)
                break
            elif search_choice.upper() == "G":
                genre = input("Enter the genre: ")
                self.search_books_by_genre(genre)
                break
            elif search_choice.upper() == "S":
                series = input("Enter the series: ")
                self.search_books_by_series(series)
                break
            elif search_choice.upper() == "T":
                letter = input("Enter the first letter of the title: ")
                self.search_books_by_title_first_letter(letter)
                break
            elif search_choice.upper() == "L":
                line = input("Enter a line to search: ")
                self.search_books_by_line(line)
                break
            elif search_choice.upper() == "B":
                self.start_reading()
                break
            elif search_choice.upper() == "E":
                print("Book reader is closing now.\nWe hope you enjoy.\nThank you!")
                return
            else:
                print("Invalid search choice. Please try again.")

    def view_book_info(self, book):
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Classification: {book.classification}")
        print(f"Kind of Book: {book.kind_of_book}")
        print(f"Genres: {', '.join(book.genres)}")
        print(f"Series: {book.series}")
        print(f"Publication Year: {book.publication_year}")
        print(f"Description: {book.description}")
        print(f"Synopsis: {book.synopsis}")

    def choose_book(self, books):
        if books:
            choice = int(input("Enter the number of the book you want to choose: ")) - 1
            if 0 <= choice < len(books):
                book = books[choice]
                action = input("Do you want to view information (I) or read (R)? Enter the letter of your choice: ")
                if action.upper() == "I":
                    self.view_book_info(book)
                    self.ask_after_reading(book)
                elif action.upper() == "R":
                    self.read_book(book)
                else:
                    print("Invalid choice. Please try again.")
                    self.choose_book(books)
            else:
                print("Invalid book number. Please try again.")
                self.choose_book(books)
        else:
            print("No books available.")

    def ask_after_reading(self, book):
        while True:
            choice = input("Do you want to go back to the start (S), view the list again (L), or exit the program (E)? Enter the letter of your choice: ")
            if choice.upper() == "S":
                self.start_reading()
                break
            elif choice.upper() == "L":
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif choice.upper() == "E":
                confirm = input("Are you sure you want to exit? (Y/N): ")
                if confirm.upper() == "Y":
                    print("Book reader is closing now.\nWe hope you enjoy.\nThank you!")
                    return
            else:
                print("Invalid choice. Please try again.")

    def sort_books(self):
        while True:
            sort_choice = input("Sort books by Author (A), Genre (G), Title (T), Series (S), or Exit now (E)? Enter the letter of your choice: ")
            if sort_choice.upper() == "A":
                ascending_choice = input("Do you want ascending (A) or descending (D)? Enter the letter of your choice: ")
                if ascending_choice.upper() == "A":
                    self.books.sort(key=lambda book: book.author)
                elif ascending_choice.upper() == "D":
                    self.books.sort(key=lambda book: book.author, reverse=True)
                else:
                    print("Invalid choice. Please try again.")
                    continue
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif sort_choice.upper() == "G":
                ascending_choice = input("Do you want ascending (A) or descending (D)? Enter the letter of your choice: ")
                if ascending_choice.upper() == "A":
                    self.books.sort(key=lambda book: book.genres[0] if book.genres else "")
                elif ascending_choice.upper() == "D":
                    self.books.sort(key=lambda book: book.genres[0] if book.genres else "", reverse=True)
                else:
                    print("Invalid choice. Please try again.")
                    continue
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif sort_choice.upper() == "T":
                ascending_choice = input("Do you want ascending (A) or descending (D)? Enter the letter of your choice: ")
                if ascending_choice.upper() == "A":
                    self.books.sort(key=lambda book: book.title)
                elif ascending_choice.upper() == "D":
                    self.books.sort(key=lambda book: book.title, reverse=True)
                else:
                    print("Invalid choice. Please try again.")
                    continue
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif sort_choice.upper() == "S":
                ascending_choice = input("Do you want ascending (A) or descending (D)? Enter the letter of your choice: ")
                if ascending_choice.upper() == "A":
                    self.books.sort(key=lambda book: book.series if book.series else "")
                elif ascending_choice.upper() == "D":
                    self.books.sort(key=lambda book: book.series if book.series else "", reverse=True)
                else:
                    print("Invalid choice. Please try again.")
                    continue
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif sort_choice.upper() == "E":
                print("Closing now the program.\nWe hope you enjoy.\nThank you and goodbye!")
                return
            else:
                print("Invalid sort choice. Please try again.")

    def view_book_info(self, book):
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Classification: {book.classification}")
        print(f"Kind of Book: {book.kind_of_book}")
        print(f"Genres: {', '.join(book.genres)}")
        print(f"Series: {book.series}")
        print(f"Publication Year: {book.publication_year}")
        print(f"Description: {book.description}")
        print(f"Synopsis: {book.synopsis}")

    def choose_book(self, books):
        if books:
            choice = int(input("Enter the number of the book you want to choose: ")) - 1
            if 0 <= choice < len(books):
                book = books[choice]
                action = input("Do you want to view information (I) or read (R)? Enter the letter of your choice: ")
                if action.upper() == "I":
                    self.view_book_info(book)
                    self.ask_after_reading(book)
                elif action.upper() == "R":
                    self.read_book(book)
                else:
                    print("Invalid choice. Please try again.")
                    self.choose_book(books)
            else:
                print("Invalid book number. Please try again.")
                self.choose_book(books)
        else:
            print("No books available.")

    def ask_after_reading(self, book):
        while True:
            choice = input("Do you want to go back to the start (S), view the list again (L), or exit the program (E)? Enter the letter of your choice: ")
            if choice.upper() == "S":
                self.start_reading()
                break
            elif choice.upper() == "L":
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif choice.upper() == "E":
                confirm = input("Are you sure you want to exit? (Y/N): ")
                if confirm.upper() == "Y":
                    print("Book reader is closing now.\nWe hope you enjoy.\nThank you!")
                    return
            else:
                print("Invalid choice. Please try again.")

    def read_book(self, book):
        choice = input("Choose the method to read the book:\n1. Open with default program\n2. Read in console\nEnter your choice (1 or 2): ")
        
        if choice == "1":
            if os.path.exists(book.file_path):
                os.startfile(book.file_path)
            else:
                print("File not found.")
        elif choice == "2":
            if os.path.exists(book.file_path):
                with open(book.file_path, 'r') as f:
                    print(f"Reading {book.title}...\n")
                    print(f.read())
                input("Press Enter to continue...")
            else:
                print("File not found.")
        else:
            print("Invalid choice. Please try again.")

    def start_reading(self):
        print("Welcome to the book reader!\nIn this application, you will enjoy reading different kinds of books in accessible files.")
        while True:
            choice = input("Do you want to Search (S), View the list of books (V), Sort the books (R), or Exit the program (E)? Enter the letter of your choice: ")
            if choice.upper() == "S":
                self.search_books()
                break
            elif choice.upper() == "V":
                self.list_books(self.books)
                self.choose_book(self.books)
                break
            elif choice.upper() == "R":
                self.sort_books()
                break
            elif choice.upper() == "E":
                confirm = input("Are you sure you want to exit? (Y/N): ")
                if confirm.upper() == "Y":
                    print("Book reader is closing now.\nWe hope you enjoy.\nThank you!")
                    return
            else:
                print("Invalid choice. Please try again.")

    def start(self):
        self.start_reading()

