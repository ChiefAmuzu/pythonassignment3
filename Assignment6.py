def get_input(prompt, default_value=""):  # Handle input safely in restricted environments
    try:
        return input(prompt)
    except OSError:
        print(f"Input blocked. Using default: {default_value}")
        return default_value

students = {}  # Dictionary to store student details

def display_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View One Student")
    print("4. View All Students")
    print("5. Exit")

def add_student():
    name = get_input("Enter student's name: ").strip()
    age = get_input("Enter student's age: ").strip()
    grade = get_input("Enter student's grade: ").strip()
    course = get_input("Enter student's course: ").strip()
    
    if name and age.isdigit() and grade and course:
        students[name] = {"age": int(age), "grade": grade, "course": course}
        print(f"Student {name} added successfully!")
    else:
        print("Invalid input. Please provide valid details.")

def remove_student():
    name = get_input("Enter student's name to remove: ").strip()
    if name in students:
        del students[name]
        print(f"Student {name} removed successfully!")
    else:
        print("Student not found.")

def view_student():
    name = get_input("Enter student's name to view: ").strip()
    if name in students:
        student = students[name]
        print(f"\nName: {name}\nAge: {student['age']}\nGrade: {student['grade']}\nCourse: {student['course']}")
    else:
        print("Student not found.")

def view_all_students():
    if students:
        print("\nAll Students:")
        for name, details in students.items():
            print(f"\nName: {name}\nAge: {details['age']}\nGrade: {details['grade']}\nCourse: {details['course']}")
    else:
        print("No students found.")

def main():
    while True:
        display_menu()
        choice = get_input("Enter your choice: ", "5").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            view_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
