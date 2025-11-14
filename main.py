from library_books import library_books
from datetime import datetime, timedelta
import toolbox as tb

# modulation functions

def MOD_print_book(book):
    book.print_info()

def MOD_search_library(library: list, term: str, condition: bool, *args):
    found = False
    extra_searches = False
    condition_meeters = []
    returning = False
    for arg in args:
        if arg == "idx":
            returning = True
            continue
        extra_searches = extra_searches or arg
    for idx, book in enumerate(library):
        if getattr(book, term) == condition or extra_searches:
            MOD_print_book(book)
            found = True
            condition_meeters.append(idx)
    if found:
        print("end books.")
    else:
        print("no books found.")
        print("--------------------------------------------")
    if returning:
        return condition_meeters

""" -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author """

def view():
    include = input("INCLUDE UNAVAILABLE BOOKS? (y/n) ")
    print("\navailable books")
    print("--------------------------------------------")
    MOD_search_library(library_books, "available", True, include == "y")
    tb.wait()

""" -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books """

def search():
    search_type = input("Are you searching by author or genre? ").lower()
    
    if search_type == "author":
        author = input("ENTER AUTHOR: ").title()
        
        print("\nmatching books")
        print("--------------------------------------------")
        MOD_search_library(library_books, "author", author)
    
    elif search_type == "genre":
        genre = input("ENTER GENRE: ").title()
        
        print()
        print("matching books")
        print("--------------------------------------------")
        MOD_search_library(library_books, "genre", genre)
        
    else:
        print("INVALID SEARCH TYPE")
    tb.wait()

""" -------- Level 3 --------
    # TODO: Create a function to checkout a book by ID
    # If the book is available:
    #   - Mark it unavailable
    #   - Set the due_date to 2 weeks from today
    #   - Increment the checkouts counter
    # If it is not available:
    #   - Print a message saying it's already checked out """

def checkout():
    to_checkout = input("ENTER ID OF BOOK TO BE CHECKED OUT: ").upper()
    
    print("\n--------------------------------------------")
    
    checkoutables = MOD_search_library(library_books, "id", to_checkout, "idx")
    
    for loop, book_idx in enumerate(checkoutables):
        print()
        correct = input("IS BOOK "+str(loop+1)+" RIGHT? (y/n) ")
        if correct == "y":
            if library_books[book_idx].available:
                print(f"\nchecking out book {loop + 1}...")
                library_books[book_idx].available = False
                library_books[book_idx].due_date = (datetime.now() + timedelta(weeks=2) ).strftime("%Y-%m-%d")
                library_books[book_idx].checkouts += 1
            else:
                print(f"\nbook {loop + 1} already checked out.")
    tb.wait()

""" -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date """

def return_book():
    to_return = input("ENTER ID OF BOOK TO BE RETURNED: ").upper()
    
    print("\n--------------------------------------------")
    
    returnables = MOD_search_library(library_books, "id", to_return, "idx")
    
    for loop, book_idx in enumerate(returnables):
        print()
        correct = input("IS BOOK "+str(loop+1)+" RIGHT? (y/n) ")
        if correct == "y":
            if library_books[book_idx].available:
                print(f"\nbook {loop + 1} already returned.")
            else:
                print(f"\nreturning book {loop + 1}...")
                library_books[book_idx].available = True
                library_books[book_idx].due_date = None
    tb.wait()

"""
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
"""

def list_overdue():
    print("\noverdue books")
    print("--------------------------------------------")
    found = False
    for book in library_books:
        if book["due_date"] < datetime.now().strftime("%Y-%m-%d"):
            MOD_print_book(book)
            found = True
    if found:
        print("end books.")
    else:
        print("no books found.")
        print("--------------------------------------------")

""" -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc. """

""" -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system! """

def menu():
    print("library menu")
    print("--------------------------------------------")
    print("0) view books")
    print("1) search books")
    print("2) checkout book")
    print("3) return book")
    print("4) list overdue books")
    print("--------------------------------------------")
    while True:
        try:
            choice = int(input("\nENTER A NUMBER (0-4): "))
            if choice in range(5):
                break
        except ValueError:
            pass
        print("please enter a number between 0 and 4.")
    tb.clear()
    if choice == 0:
        view()
    elif choice == 1:
        search()
    elif choice == 2:
        checkout()
    elif choice == 3:
        return_book()
    else:
        list_overdue()

def main():
    while True:
        tb.clear()
        menu()

if __name__ == "__main__":
    main()
