import json
import os
from error_code import ErrorCode

books = []

def load_books():
    if not os.path.exists("books.json") or os.path.getsize("books.json") == 0:
        return []
    try:
        with open("books.json", 'r', encoding='utf-8') as fp:
            books_data = json.load(fp)
            return books_data
        
    except json.JSONDecodeError:
        print("Error: books.json contains invalid JSON.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

class AddBook:
    def __init__(self):
        # Ensure books are loaded properly
        self.books = load_books()

    def add_book(self, book_id, title, author, genre, price, stock_qty, publisher, publish_year):
        # Add a new book to books.json
        book = {
            "book_id": book_id,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "stock_qty": stock_qty,
            "publisher": publisher,
            "publish_year": publish_year
        }
        
        self.books.append(book)

        try:
            with open('books.json', 'w', encoding='utf-8') as fp:
                json.dump(self.books, fp, indent=4)
            print("--------------------------------------")
            print("Success: Data added to books.json successfully")
        except Exception as e:
            print(f"Error writing to books.json: {e}")

    def get_id(self, book_id):
        # Check if a book ID already exists
        for book in self.books:
            if book.get('book_id') == book_id:
                return book_id

    def get_title(self, title):
        # Check if a book title already exists
        for book in self.books:
            if book.get('title') == title:
                return title

def addBookCall():
    addbook = AddBook()
    err = ErrorCode()

    try:
        book_id = int(input("Enter book ID: "))
        if addbook.get_id(book_id):
            raise Exception("Error: Book ID already exists.")
        err.error_negative(book_id)
        
        book_title = input("Enter book title: ").strip()
        if addbook.get_title(book_title):
            raise Exception("Error: Book title already exists.")
        err.error_str(book_title)

        book_author = input("Enter book author: ").strip()
        err.error_str(book_author)

        book_genre = input("Enter book genre: ").strip()
        err.error_str(book_genre)

        book_price = float(input("Enter book price: "))
        err.error_negative(book_price)

        book_stock_qty = int(input("Enter book stock quantity: "))
        err.error_negative(book_stock_qty)

        book_publisher = input("Enter book publisher: ").strip()
        err.error_str(book_publisher)

        book_publish_year = int(input("Enter book publish year: "))
        err.error_negative(book_publish_year)

        addbook.add_book(book_id, book_title, book_author, book_genre, book_price, book_stock_qty, book_publisher, book_publish_year)

    except ValueError as ev:
        print("Unexpected error: Invalid input: Only number is allowed.")
    except Exception as e:
        print(f"Unexpected error: {e}")