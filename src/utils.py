import json
from models.student import Student
from models.course import Course


def get_list_of_students(path: str) -> list[Student]:
    """
    Get the list of students. This can be arbitrary and have many different
    back-ends, it just needs to return a list of Student objects
    """
    student_data = json.load(open(path))
    students = []
    courses = []

    # Loop over the "students" data in the JSON
    for student in student_data["students"]:
        courses = []

        for course in student["courses"]:
            crs = Course(course["name"], course["credits"], "C-")
            if crs not in courses:
                courses.append((crs, course["grade"]))

        # Check if the student has a course list. Not needed now, might want
        # later for error checking.
        # if len(courses) == 0:
        #     raise Error
        # Append the generated student the the list
        students.append(Student(student["id"], courses))

    return students, courses
