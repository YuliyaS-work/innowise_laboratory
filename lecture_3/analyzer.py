"""
This program manages and analyzes student grades.

Features:
1. Add a new student
2. Add a grades for a student
3. Show report (all students)
4. Find top performer
5. Exit
"""

import math

# The list of dictionaries with students data: names and the list of grades
students: list[dict[str, list[int]]] = []

def get_average(student_grades: list[int]) -> float:
    """Return rounded average of grades."""
    average = sum(student_grades) / len(student_grades)
    return math.floor(average * 10 + 0.5) / 10

def add_student() -> None:
    """Add a new student to the list students."""
    while True:
        name = input("Enter student name: ").strip()
        # Validate that the name contains only letters, digits, spaces, hyphens
        if name.replace(" ", "").replace("-", "").isalnum():
            # Check if the student exists in the list
            if any(student.get("name") == name.title() for student in students):
                print("This student is in the list.")
            else:
                # Create a new student record with an empty grades list
                student = {"name": name.title(), "grades": []}
                students.append(student)
            break
        else:
            print("Please, enter a valid name.")


def add_grades() -> None:
    """Add grades for an existing student."""
    name = input("Enter student name: ").strip().title()
    for student in students:
        if student.get("name") == name:
            while True:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade.strip().lower() == 'done':
                    break
                try:
                    grade_int = int(grade)
                    if 0 <= grade_int <= 100:
                        student["grades"].append(grade_int)
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break
    else:
        print(
            "This student isn't in the list. "
            "Please, add a new student or enter a valid name."
        )


def generate_report() -> None:
    """Generate a report with averages for all students."""
    if students:
        averages: list[float] = []
        print("--- Student Report ---")
        for student in students:
            # Calculate the average grade for each student
            try:
                student_average = get_average(student["grades"])
                averages.append(student_average)
                print(f"{student['name']}'s average grade is {student_average}")
            except ZeroDivisionError:
                print(f"{student['name']}'s average grade is N/A")

        # Show max, min, overall average across all students
        if averages:
            print("-" * 25)
            print(f"Max Average: {max(averages)}")
            print(f"Min Average: {min(averages)}")
            print(f"Overall Average: {get_average(averages)}")
        else:
            print("The students have no grades.")
    else:
        print("There are no students in the list.")


def find_top_student() -> None:
    """Find the student with the highest average grade."""
    # Filter only students who have at least one grade
    graduated_students = [student for student in students if student["grades"]]

    # Find the student with the maximum average grade
    if graduated_students:
        top_student = max(
            graduated_students,
            key=lambda student: get_average(student["grades"])
        )
        print(
            f"The student with the highest average is {top_student['name']} "
            f"with a grade of {get_average(top_student['grades'])}"
        )
    else:
        print("There are no students with grades.")


# Main loop displays menu and handles user's choices
while True:
    print("--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_grades()
    elif choice == '3':
        generate_report()
    elif choice == "4":
        find_top_student()
    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid input. Please enter a valid choice.")
        continue