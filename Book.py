import os

class Book:
    def __init__(self, title, author, classification, kind_of_book, genres, series, publication_year, description, synopsis, file_path):
        self.title = title
        self.author = author
        self.classification = classification
        self.kind_of_book = kind_of_book
        self.genres = genres
        self.series = series
        self.publication_year = publication_year
        self.description = description
        self.synopsis = synopsis
        self.file_path = file_path

    def read(self):
        if os.path.exists(self.file_path):
            os.startfile(self.file_path)
        else:
            print("File not found.")

    def view_description(self):
        print(self.description)

    def view_synopsis(self):
        print(self.synopsis)
