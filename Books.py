class Book:
    def __init__(self,tittle,author,isbn,publication_year,available):
        self.title=tittle
        self.author=author
        self.isbn=isbn
        self.publication_year=publication_year
        self.available=available
        

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Available: {'Yes' if self.available else 'No'}")

    def update_book(self, title=None, author=None, isbn=None, publication_year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        if publication_year:
            self.publication_year = publication_year

