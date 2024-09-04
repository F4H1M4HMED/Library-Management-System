# main.py

from book import Book
from library import Library

def main():
    # Create instances of Book
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 5)
    book2 = Book("1984", "George Orwell", 3)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 2)

    # Create an instance of Library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display all books in the library
    print("All books in the library:")
    library.display_books()
    print()

    # Find and display a specific book
    search_title = "1984"
    found_book = library.find_book(search_title)
    if found_book:
        print(f"Found book: {found_book.title} by {found_book.author}")
        found_book.display_info()
    else:
        print(f"Book with title '{search_title}' not found.")
    print()

    # Borrow a book
    print("Attempting to borrow '1984':")
    book_to_borrow = library.find_book("1984")
    if book_to_borrow:
        book_to_borrow.borrow_book()
    else:
        print("Book not found.")
    print()

    # Try to borrow the same book again
    print("Attempting to borrow '1984' again:")
    book_to_borrow = library.find_book("1984")
    if book_to_borrow:
        book_to_borrow.borrow_book()
    else:
        print("Book not found.")
    print()

    # Return a book
    print("Attempting to return '1984':")
    book_to_return = library.find_book("1984")
    if book_to_return:
        book_to_return.return_book()
    else:
        print("Book not found.")
    print()

    # Display all books in the library again
    print("All books in the library after borrowing and returning:")
    library.display_books()

if __name__ == "__main__":
    main()
