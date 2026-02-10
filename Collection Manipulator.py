students = {}
print("Welcome to the Student Data Organizer!")

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Enter student details:")
        sid = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").

        students[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": [s.strip() for s in subjects]
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students available.")
        else:
            print("--- Display All Students ---")
            for sid in students:
                s = students[sid]
                print(
                    f"Student ID: {sid} | Name: {s['name']} | Age: {s['age']} | "
                    f"Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}"
                )

    elif choice == "3":
        sid = int(input("Enter Student ID to update: "))

        if sid in students:
            students[sid]["name"] = input("Name: ")
            students[sid]["age"] = int(input("Age: "))
            students[sid]["grade"] = input("Grade: ")
            students[sid]["dob"] = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")
            students[sid]["subjects"] = [s.strip() for s in subjects]

            print("Student information updated successfully!")
        else:
            print("Student not found.")

    elif choice == "4":
        sid = int(input("Enter Student ID to delete: "))

        if sid in students:
            del students[sid]
            print("Student deleted successfully!")
        else:
            print("Student not avialble.")

    elif choice == "5":
        subject_set = set()

        for s in students.values():
            for sub in s["subjects"]:
                subject_set.add(sub)

        if subject_set:
            print("--- Subjects Offered ---")
            for sub in subject_set:
                print(sub)
        else:
            print("No subjects available.")

    elif choice == "6":
        print("Thank you for using the Student Data Organizer. Goodbye!")
        break

    else:

        print("Invalid choice. Please try again.")
