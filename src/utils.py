import json
from models.student import Student
from models.course import Course


def get_list_of_students(path: str, courses: list[Course]) -> list[Student]:
    """
    Get the list of students. This can be arbitrary and have many different
    back-ends, it just needs to return a list of Student objects
    """
    student_data = json.load(open(path))
    students = []

    # Loop over the "students" data in the JSON
    for student in student_data["students"]:
        crss = []

        for course in student["courses"]:
            if course["name"] not in [course.course_name for course in courses]:
                # Probably can delete this branch now, I don't think it
                # will occur but might as well keep it and see what happens
                print("BADBADBADBADBADBABDABDBADBADABAD")
                print("potential new course found: " + course["name"])
            else:
                crs = Course.get_course_by_name(course["name"], courses)
                crss.append((crs, course["grade"]))

        # Check if the student has a course list. Not needed now, might want
        # later for error checking.
        # if len(courses) == 0:
        #     raise Error
        # Append the generated student the the list
        students.append(Student(student["id"], crss))

    return students
