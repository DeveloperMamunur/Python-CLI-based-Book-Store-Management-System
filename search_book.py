import json
import os
from error_code import ErrorCode
class SearchBook:
    def __init__(self, file_path='books.json'):
        self.file_path = file_path

    def _load_books(self):
        # Helper function to safely load books from JSON file
        if not os.path.exists(self.file_path):
            print("Error: books.json not found.")
            return []

        try:
            with open(self.file_path, 'r') as fp:
                books = json.load(fp)
                if not isinstance(books, list):
                    raise ValueError("Invalid data format in books.json")
                return books
        except json.JSONDecodeError:
            print("Error: books.json contains invalid JSON.")
            return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def _search(self, key, value):
        # Generalized search function
        books = self._load_books()
        found_books = [book for book in books if book.get(key) == value]

        if not found_books:
            print(f"Error: No books found with {key} = {value}")
            return False

        print("--------------------------------------")
        print("---------- Search Results ------------")
        for book in found_books:
            print("----------------------------------------------------------")
            print(" | ".join(f"{key}: {value}" for key, value in book.items()))

        return True

    def search_id(self, id):
        return self._search('book_id', id)
    
    def search_title(self, title):
        return self._search('title', title)
    def search_author(self, author):
        return self._search('author', author)
    def search_price(self, price):
        return self._search('price', price)
    def search_genre(self, genre):
        return self._search('genre', genre)
    def search_publisher(self, publisher):
        return self._search('publisher', publisher)
    def search_publish_date(self, publish_date):
        return self._search('publish_date', publish_date)

def searchBookCall():
    searchbook = SearchBook()

    book_headings = ['ID', 'Title', 'Author', 'Genre', 'Price', 'Publisher', 'Publish Date']
    
    print("Key   Heading -------------------------------")
    for index, heading in enumerate(book_headings):
        print(f"{index}  {heading}")

    try:
        print("===============================================")
        heading_input = int(input("Enter Your key No and press enter: "))
        
        if 0 <= heading_input < len(book_headings):
            print("===============================================")
            search_methods = [
                searchbook.search_id, searchbook.search_title, searchbook.search_author,
                searchbook.search_genre, searchbook.search_price, searchbook.search_publisher,
                searchbook.search_publish_date
            ]
            
            search_value = input(f"Enter {book_headings[heading_input]} and press enter: ")
            if heading_input == 0 or heading_input == 4:  # Convert ID & Price to int if needed
                try:
                    search_value = int(search_value)
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    return
            else:
                search_value = ErrorCode.error_str(searchbook, search_value)
            
            if not search_methods[heading_input](search_value):
                print(f"Search for {book_headings[heading_input]} not found.")

        else:
            print("Error: You have entered an invalid number.")

    except ValueError:
        print("Error: Invalid input! Please enter a number corresponding to a heading.")