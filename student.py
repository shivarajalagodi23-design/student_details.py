import sys


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def display_result(name, marks):
    grade = calculate_grade(marks)
    print("Student:", name)
    print("Marks:", marks)
    print("Grade:", grade)


name = input("Enter student name: ")
marks = input("Enter marks: ")

if name == "":
    name = "Student"

if marks == "":
    marks = 75
else:
    marks = int(marks)

display_result(name, marks)
