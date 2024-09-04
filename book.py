class Book:
    def __init__(self,title,author,copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def display_info(self):
        print("Title: ",(self.title),"Author: ",(self.author),"Copies: ",(self.copies))
    
    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"Book Borrowed: {self.title} by {self.author}. Copies remaining: {self.copies}")
        else:
            print(f"Sorry, all copies of {self.title} by {self.author} are currently borrowed.")

    def return_book(self):
        self.copies += 1
        print(f"Book Returned: {self.title} by {self.author}. Copies available: {self.copies}")