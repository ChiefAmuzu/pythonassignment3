std_details= {}

while True:
    print("\nWelcome to the Student Management System")
    print("\n1. Add a Student, collect(Name,Age, list of courses and grade)")
    print("2. Remove a Student")
    print("3. View One Student")
    print("4. View All Students")
    print("5. Exit")
    
    option = input("\nChoose an Option:")
    if option == "1":
        name= input("Enter Student Name:")
        age=input("Enter Student Age:")
        course=input("Enter Student Course:")
        grade=input("Enter Student Grade:")
       # course_grade=dict(zip(course.split(","),grade.split(",")))
        std_details[name]={"Age":age, "Course":course, "Grade":grade}
        #std_details[name]={"Age":age, "Course":course, "Grade":grade}
        #print(std_details)
        print(f" {name} has been added to the system")
    
    elif option == "2":
        print("\nRemove Student From System")
        name=input('Enter Name of Student to remove:')
        if name in std_details:    
            del std_details[name]
            print(f"{name} has been removed from system")
        else:
            print(f"{name} not in records")

    elif option == "3":
        print("\nView Student Details")
        name=input("Enter Name of Student To View:")
        if name in std_details:
            #print(f"{name} {std_details[name]}")
            av=std_details[name]
            print(f'-{name}',*[f"{k}:{v}" for k, v in av.items()])
        else:
            print("No Records Found")

    elif option == "4":
        if std_details:
            print("\nAll Student In System")
            for key, value in std_details.items():
                #print(key,value)
                ab=value
                print(f'-{key}',*[f"{k}: {v}" for k, v in ab.items()],sep=",")
            
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Input, Enter a Number(1-5)")
