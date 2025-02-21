#Book Title Library
#Add Title To Library
def book_library():
    library = []
    
    while True:
    #Menu printed for Book Library   
        print("\nWelcome To The Book Title Library")

        print("\n1. Add a Book ")
        print("2. Remove a Book ")
        print("3. View All Books")
        print("4. Search Title In Library")
        print("5. Exit")

        option =input("\nEnter Your choice 1-5: ")
        if option == "1":
            title = input( "\nEnter Book Title(s) separated by comma: ")
            library.extend(title.split(','))
            print(f'{title} has been added to the library')
            
            n_library=[lit.strip().lower() for lit in library]

        elif option == "2":
            title= input("\n Enter Book Title to Remove: ").strip().lower()
            if title in n_library:
                n_library.remove(title)
                print(f" '{title.title()}' removed from the Library")
            else:
                print(f" '{title}' not in Library")

        elif option == "3":
            print("\nBooks In The Library")
            for book in n_library:
                print(f'-{(book.title())}')

        elif option == "4":
            print("Search for Book Title")
            bk= input("\nEnter The Book Title:").strip().lower()
            if bk in n_library:
                print(f" {(bk.title())} is Available")
            else:
                print("Book Not In Library")
            
        elif option == "5":
            print("Good Bye!")
            break
        else:
            print("Invalid Input, Enter the a Number (1-5)")
book_library()
