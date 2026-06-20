students = []

def add_student():
        name = input("Enter Student Name: ")
        students.append(name)
        print("Student Added Successfully!")

def view_students():
        print("\nStudents List:")

        for student in students:
            print(student) 

def search_student():
        search_name = input("Enter Student Name to Search: ")
        if search_name in students:
            print("Student Found!")
        else:
            print("Student Not Found!")

def delete_student():
        delete_name = input("Enter Student Name to Delete: ")
        if delete_name in students:
            students.remove(delete_name)
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")



while True:
    print("\n===== Student Management System ====")

    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
        

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")

