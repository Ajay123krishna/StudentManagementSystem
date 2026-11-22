
students = []

def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": sid,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found")
    else:
        for s in students:
            print(s)

def search_student():
    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == sid:
            print(s)
            return

    print("Student not found")

def delete_student():
    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
