import json
import os

class RemoveBook:
    def remove_book(self, book_id):
        file_path = 'books.json'

        # Check if the file exists
        if not os.path.exists(file_path):
            print("Error: books.json not found.")
            return False

        try:
            # Read books from the file
            with open(file_path, 'r') as fp:
                try:
                    books = json.load(fp)
                    if not isinstance(books, list):
                        raise ValueError("Invalid data format in books.json")
                except json.JSONDecodeError:
                    print("Error: books.json contains invalid JSON.")
                    return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False

        # Check if the book exists and remove it
        original_length = len(books)
        books = [book for book in books if book.get('book_id') != book_id]
        print("----------------------------------------------------------")
        if len(books) == original_length:
            print("Error: Book not found.")
            return False

        # Write updated list back to file
        try:
            with open(file_path, 'w') as fp:
                json.dump(books, fp, indent=4)
            print("Book removed successfully.")
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False


def removeBookCall():
    try:
        book_id = int(input("Enter book id to remove and press enter: "))
        book = RemoveBook()

        if not book.remove_book(book_id):
            raise Exception("Book not found or removal failed.")
    
    except ValueError:
        print("Invalid input! Please enter a valid book ID (integer).")
    except Exception as e:
        print(e)