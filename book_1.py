class MyBook:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.borrowed = False

def read_books():
    library = []
    n = int(input("enter number of books: "))
    for i in range(n):
        title = input("enter the book title: ")
        author = input("enter the author name: ")
        publication_date = input("enter publication date: ")

        book = MyBook(title, author, publication_date)
        library.append(book)
    return library

def borrow_book(library, title):
    for book in library:
        if book.title == title:
            if book.borrowed:
                print("'", title, "' is already borrowed.")
            else:
                book.borrowed = True
                print("u have borrowed:", title)
            return
    print("'", title, "' not found in the library.")

def return_book(library, title):
    for book in library:
        if book.title == title:
            if book.borrowed:
                book.borrowed = False
                print("u have returned:", title)
            else:
                print("'", title, "' was not borrowed.")
            return
    print("'", title, "' not found in the library.")

def main():
    library = read_books()
    
    title_to_borrow = input("enter the title of the book to borrow: ")
    borrow_book(library, title_to_borrow)
    
    title_to_return = input("enter the title of the book to return: ")
    return_book(library, title_to_return)

main()
