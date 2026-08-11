import sys

student_records = {}

def display_menu():
    print("\n-- Student Records Management ---")
    print("1. Add a New Student (Create)")
    print("2. Search for a Student (Read)")
    print("3. Update Student Skills (Update)")
    print("4. View All Students (Display)")
    print("5. Exit")
    return input("Select an option (1-5): ")

def add_student():
    print("\n-- Add Student --")
    student_id = input("Enter Student ID: ").strip()

    if student_id in student_records:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()

    
    course = input("Enter Course: ").strip().upper()
    section = input("Enter Section: ").strip().upper()
    course_info = (course, section)

    skills_input = input("Enter skills separated by commas: ")
    skills_lists = [skill.strip() for skill in skills_input.split(',')]

    student_records[student_id] = {
        "name": name,
        "course_info": course_info,
        "skills": skills_lists
    }
    print(f"Student {name} added successfully!")

def view_student():
    print("\n-- Search Student --")
    student_id = input("Enter Student ID to search: ").strip()

    record = student_records.get(student_id)

    if record:
        print(f"\nRecord found for {student_id}:")
        print(f"Name: {record['name']}")
        print(f"Course & Section: {record['course_info'][0]} - {record['course_info'][1]}")
        print(f"Skills: {', '.join(record['skills'])}")

    else:
        print("Student not found.")

def update_student():
    print("\n-- Update Student Skills --")
    student_id = input("Enter Student ID to update: ").strip()

    if student_id in student_records:
        new_skill = input("Enter a new skill to add: ").strip()
        student_records[student_id]["skills"].append(new_skill)
        print(f"Skill '{new_skill}' added to {student_records[student_id]['name']}'s record.")

    else:
        print("Student not found.")

def display_all():
    print("\n-- All Student Records --")
    if not student_records:
        print("No records available")
        return

    for s_id, data in student_records.items():
        print(f"ID: {s_id} | Name: {data['name']} | Section: {data['course_info']} | Skills: {data['skills']}")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            display_all()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()