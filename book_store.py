class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2026 - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


book1 = Book(
    "Harry Potter and the Philosopher's Stone",
    "J.K. Rowling",
    "9780747532699",
    1997,
)

book2 = Book(
    "The Alchemist",
    "Paulo Coelho",
    "9780061122415",
    1988,
)

book3 = Book(
    "A Man Called Ove",
    "Fredrik Backman",
    "9781476738017",
    2012,
)


print(book1.get_summary())
print("Age:", book1.get_age())

print(book2.get_summary())
print("Age:", book2.get_age())

print(book3.get_summary())
print("Age:", book3.get_age())