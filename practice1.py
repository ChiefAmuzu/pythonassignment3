
def get_input(prompt, default_value=""):  # Function to simulate input in restricted environments
    try:
        return input(prompt)  # Standard input function
        print(f"Input blocked. Using default: {default_value}")
        return default_value  # Use default values if input() is restricted

def main():
    book_library = []  # List to store book titles
    
    while True:
        print("\nWelcome to the Book Title Library!")
        print("Choose an option:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. View All Books")
        print("4. Exit")
        
        choice = get_input("Enter your choice: ", "4")
        
        if choice == "1":
            book_title = get_input("Enter the book title: ").strip()
            if book_title:
                book_library.append(book_title)
                print(f'"{book_title}" has been added to the library.')
            else:
                print("Invalid input. Book title cannot be empty.")
        
        elif choice == "2":
            if book_library:
                print("Books in the Library:")
                for i, book in enumerate(book_library, 1):
                    print(f"{i}. {book}")
                book_to_remove = get_input("Enter the book title to remove: ").strip()
                if book_to_remove in book_library:
                    book_library.remove(book_to_remove)
                    print(f'"{book_to_remove}" has been removed from the library.')
                else:
                    print("Book not found in the library.")
            else:
                print("No books in the library to remove.")
        
        elif choice == "3":
            if book_library:
                print("Books in the Library:")
                for book in book_library:
                    print(f"- {book}")
            else:
                print("The library is empty.")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()