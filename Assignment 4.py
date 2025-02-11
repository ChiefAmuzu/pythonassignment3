
# Program to store, update, and display personal details

def main():
    # Store personal details
    personal_info = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "favorite_colors": input("Enter your favorite colors (comma-separated): ").split(",")
    }
    
    # Store a list of friends' names
    friends = input("Enter your friends' names (comma-separated): ").split(",")
    friends = [friend.strip() for friend in friends]
    
    while True:
        print("\nMenu:")
        print("1. Update Age")
        print("2. Update Favorite Colors")
        print("3. Remove a Friend")
        print("4. Display Information")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            new_age = int(input("Enter new age: "))
            personal_info["age"] = new_age
            print("Age updated successfully!")
        
        elif choice == "2":
            new_colors = input("Enter favorite colors (comma-separated): ").split(",")
            personal_info["favorite_colors"] = [color.strip() for color in new_colors]
            print("Favorite colors updated successfully!")
        
        elif choice == "3":
            print("Friends List:", ", ".join(friends))
            friend_to_remove = input("Enter the name of the friend to remove: ")
            if friend_to_remove in friends:
                friends.remove(friend_to_remove)
                print(f"{friend_to_remove} has been removed from your friends list.")
            else:
                print("Friend not found!")
        
        elif choice == "4":
            print("\nUpdated Information:")
            print(f"Name: {personal_info['name']}")
            print(f"Age: {personal_info['age']}")
            print(f"Favorite Colors: {', '.join(personal_info['favorite_colors'])}")
            print(f"Friends: {', '.join(friends)}")
        
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
