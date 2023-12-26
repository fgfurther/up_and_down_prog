class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")

# Пример использования паттерна ООП
library_oop_pattern = Library()
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library_oop_pattern.add_book(book1)
library_oop_pattern.add_book(book2)

print("Books in the library (OOP pattern):")
library_oop_pattern.display_books()



class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

def add_book(library, book):
    library.append(book)

def display_books(library):
    for book in library:
        print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")

# Пример использования процедурного стиля с паттерном
library_procedural_pattern = []
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

add_book(library_procedural_pattern, book1)
add_book(library_procedural_pattern, book2)

print("Books in the library (Procedural pattern):")
display_books(library_procedural_pattern)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Пример использования объектно-ориентированного стиля без паттерна
library_oop_without_pattern = []
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library_oop_without_pattern.append(book1)
library_oop_without_pattern.append(book2)

print("Books in the library (OOP without pattern):")
for book in library_oop_without_pattern:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
