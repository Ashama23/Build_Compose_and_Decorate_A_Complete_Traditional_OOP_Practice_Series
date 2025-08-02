class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_book_count(cls):
        return cls.total_books
    
print(f"Initial number of books: {Book.get_book_count()}")

book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
print(f"Number of books after adding two: {Book.get_book_count()}")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
print(f"Final number of books: {Book.total_books}") 