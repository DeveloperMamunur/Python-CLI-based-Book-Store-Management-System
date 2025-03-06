from add_book import addBookCall as addbook
from view_book import ViewBookCall as viewbook
from search_book import searchBookCall as searchbook

def main():
    # Programme first view book list
    viewbook()
    # then loads main menu
    while True:
        print("--------------------------------------")
        print("---------- Select an option ----------")
        print("--------------------------------------")
        print("1. Add Book")
        print("2. View Book")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        print("--------------------------------------")

        try:
            choice = int(input("Enter your choice number(1 - 5) and press enter: "))
            
            if choice == 1:
                addbook()
            elif choice == 2:
                viewbook()
            elif choice == 3:
                searchbook()
            elif choice == 4:
                pass
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()