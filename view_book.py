import json
import os

class ViewBook:
    def view_book(self):
        # Displays all books from books.json safely
        if not os.path.exists('books.json') or os.path.getsize('books.json') == 0:
            print("Error: books.json is missing or empty.")
            return
        try:
            with open('books.json', 'r', encoding='utf-8') as fp:
                books = json.load(fp)

            if not books:
                print("No books available in the database.")
                return

            print("----------------------------------------------------------")
            print("------------- View All Book From Json File ---------------")

            for book in books:
                print("----------------------------------------------------------")
                print(" | ".join(f"{key}: {value}" for key, value in book.items()))


        except json.JSONDecodeError:
            print("Error: books.json contains invalid JSON data.")
        except Exception as e:
            print(f"Unexpected error: {e}")

def ViewBookCall():
    # Calls the ViewBook class to display books
    book1 = ViewBook()
    book1.view_book()