import json
import models.student.Student as Student


def main():
    students = get_list_of_students("students.json")

    # calculateNumberInCIS121(students, number incoming)

    for student in students:
        print("Id={} GPA={}".format(student.student_id, student.gpa))


def get_list_of_students(path: str) -> list[Student]:
    student_data = json.load(open(path))
    students = []

    for student in student_data["students"]:
        student_id = student["id"]
        courses = []

        for course in student["courses"]:
            # TODO: Create a Course class from this
            courses.append(
                (course["name"], course["grade"], course["credits"]))

        std = Student(student_id, courses)
        students.append(std)

    return students


if __name__ == "__main__":
    main()
