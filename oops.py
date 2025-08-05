class Book:
    def __init__(self, title,author,availablility_status):
        self.title = title
        self.author = author
        self.availablility_status = availablility_status
    def borrow(self):
        if self.availablility_status:
            self.availablility_status = False
            print("You borrowed '{self.title}' by '{self.author}'")
        else:
            print("'{self.title}' is currently not available.")
    def return_b(self):
        self.availablility_status = True
        print("You returned '{self.title}' by '{self.author}'")

class Library:
    def __init__(self):
        self.books = []
    def add(self, book):
        self.books.append(book)
    def find_b(self, title):
        for i in self.books:
            if i.title == title:
                return i
        return None
    

title=input("Enter the book title: ")
author=input("Enter the book author: ")
obj= Book(title, author, True)
lib= Library()
lib.add(obj)
title= input("Enter the book title to borrow: ")
book = lib.find_b(title)
if book:
    book.borrow()
else:
    print("Book not found in the library.")
title= input("Enter the book title to return: ")
book = lib.find_b(title)
if book:
    book.return_b()






    