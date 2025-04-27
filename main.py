import json
import os

dataFile = "lib.txt"

def loadLib():
    if os.path.exists(dataFile):
        with open(dataFile, "r") as file:
            return json.load(file)
    else:
        return []

def saveLibrary(library):
    with open(dataFile, "w") as file:
        json.dump(library, file)

def addBooks(library):
    title = str(input("Enter The Title of the Book:"))
    author = str(input("Enter The Author of the Book:"))
    year = int(input("Enter The Year Of The Book:"))
    genre = str(input("Enter The genre of book:"))
    read = input("Have you read the book? (yes/no):").lower() == "yes"

    newBook = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(newBook)
    saveLibrary(library)
    print(f"Book: {title} Added Successfully")

def removeBook(library):
    title = input("Enter the title book to remove book from library:")

    initialLength = len(library)
    library = [book for book in library if book["title"].lower() != title.lower()]

    if len(library) < initialLength:
        saveLibrary(library)
        print(f"Book: {title} Removed successfully!")
    else:
        print(f"Book: {title} Not Found In the library!")

    return library

def searchLibrary(library):
    searchBy = input("Search by Title or Author (Type: title/author): ").lower()
    searchTerms = input(f"Enter the {searchBy}: ").lower()

    results = [book for book in library if searchTerms in book[searchBy].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "Not Read"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No Books found matching '{searchTerms}' in the '{searchBy}' field.")

# def displayAllBooks(library):
#     if library:
#         for book in library:
#             status = "Read" if book["read"] else "Not Read"
#             print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
#     else:
#         print("The Library is Empty.")

def displayAllBooks(library):
    if library:
        for book in library:
            status = "Read" if book.get("read", False) else "Not Read"
            genre = book.get("genre", "Unknown Genre")
            print(f"{book.get('title', 'Unknown Title')} by {book.get('author', 'Unknown Author')} - {book.get('year', 'Unknown Year')} - {genre} - {status}")
    else:
        print("The Library is Empty.")

def display(library):
    totalBooks = len(library)
    readBook = len([book for book in library if book["read"]])
    percent = (readBook / totalBooks) * 100 if totalBooks > 0 else 0
    print(f"Total Books: {totalBooks}")
    print(f"Percentage Read: {percent:.2f}%")

def mainFunc():
    library = loadLib()
    if not library:
        print("Library is currently empty, please add some books.")
        
    while True:
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the Library")
        print("4. Display all Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter Your Choice:")

        if choice == "1":
            addBooks(library)
        elif choice == "2":
            library = removeBook(library)
        elif choice == "3":
            searchLibrary(library)
        elif choice == "4":
            displayAllBooks(library)
        elif choice == "5":
            display(library)
        elif choice == "6":
            print("Good Bye!")
            break
        else:
            print("Invalid Choice Please Try Again!")

if __name__ == "__main__":
    mainFunc()
