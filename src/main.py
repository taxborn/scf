import json
import models.student as stud


def main():
    student_data = json.load(open("students.json"))
    students = []

    for student in student_data["students"]:
        student_id = student["id"]
        courses = []

        for course in student["courses"]:
            courses.append(
                (course["name"], course["grade"], course["credits"]))

        std = stud.Student(student_id, courses)
        students.append(std)

    for student in students:
        print(student.gpa)


if __name__ == "__main__":
    main()
