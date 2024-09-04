from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
    
    def display_books(self):
        for book in self.books:
            book.display_info()

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None  

        
    

    

        