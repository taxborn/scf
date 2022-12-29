import json
from models.student import Student


def main():
    # Used https://app.json-generator.com/zT_NwqNKE-l1 to generate the random
    # data. Currently use this template in `students_generator.js`.

    students = get_list_of_students("students.json")

    # calculateNumberInCIS121(students, number incoming)

    for student in students:
        print("Id={} GPA={}".format(student.student_id, student.gpa))


def get_list_of_students(path: str) -> list[Student]:
    """
    Get the list of students. This can be arbitrary and have many different
    back-ends, it just needs to return a list of Student objects
    """
    student_data = json.load(open(path))
    students = []

    # Loop over the "students" data in the JSON
    for student in student_data["students"]:
        courses = []

        for course in student["courses"]:
            # TODO: Create a Course class from this
            courses.append(
                (course["name"], course["grade"], course["credits"]))

        # Check if the student has a course list. Not needed now, might want
        # later for error checking.
        # if len(courses) == 0:
        #     raise Error
        # Append the generated student the the list
        students.append(Student(student["id"], courses))

    return students


if __name__ == "__main__":
    main()
