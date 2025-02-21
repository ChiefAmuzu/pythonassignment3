# Store personal details (like name, age, and favorite colors) in variables and dictionaries.

Name = input("Enter your name: ")
Age = input("Enter your age  ")
Favorite_color = input("Enter your favorite color ")

user = {    
    "Name": Name,
    "Age": Age,
    "Favorite color" : Favorite_color,
}


# Store lists of friends names

friend_names = input("Please enter friends name: ")
friend_names = friend_names.split(", ")
friend_names = list(friend_names)

print("These are your current details: ", user)

# Allow user to update personal information, like age and favorite color
changes = input("Do you want to make any changes? ").capitalize()

if changes == "Yes":

    new_name = input("Enter New Name: ")
    user["name"] = new_name

    new_age = input("Enter New Age ")
    user["age"] = new_age

    new_favorite_color = input("Enter Favorite color: ")
    user["favorite color"] = new_favorite_color

else:
    print(user)

# Remove a friend from the list.
remove_friend = input("which friend do you want to remove: ")
if remove_friend in friend_names:
    friend_names.remove(remove_friend)
    print(f"{remove_friend} has been removed")
else:
    print("Name not found")

# Display the updated information in an organized format.
print("These are your updated details: ", user)

print("And these are your friends' names: ", friend_names)
    
