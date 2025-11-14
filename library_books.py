class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def print_info(self):
        print(f"id: {self.id}")
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"genre: {self.genre}")
        print(f"available: {self.available}")
        print(f"due date: {self.due_date}")
        print(f"checkouts: {self.checkouts}")
        print("--------------------------------------------")

library_books = [
    Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2),
    Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5),
    Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3),
    Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4),
    Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6),
    Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8),
    Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1),
    Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, "2025-11-12", 3)
]