def read_books():
    library = []
    n = int(input("Enter number of books:"))
    for i in range(n):
        title = input("Enter book title:")
        author = input("Enter author name:")
        publication_date = input("Enter publication date:")

        book = {
            "title": title,
            "author": author,
            "publication_date": publication_date,
            "borrowed": False
        }
        
        library.append(book)
    return library

def borrow_book(library, title):
    for book in library:
        if book["title"] == title:
            if book["borrowed"]:  
                print("'" + title + "' is already borrowed.")
            else:  
                book["borrowed"] = True
                print("You have borrowed:", title)
            return
    print("'", title, "' not found in the library.")

def return_book(library, title):
    for book in library:
        if book["title"] == title:
            if book["borrowed"]:  
                book["borrowed"] = False
                print("You have returned:", title)
            else:  
                print("'" + title + "' was not borrowed.")
            return
    print("'" + title + "' not found in the library.")

def main():  
    library = read_books()
    
    title_to_borrow = input("Enter the title of the book to borrow: ")
    borrow_book(library, title_to_borrow)
    

    title_to_return = input("Enter the title of the book to return: ")
    return_book(library, title_to_return)



main()
