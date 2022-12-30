import json
from models.student import Student
from models.course import Course
import utils


def main():
    # Used https://app.json-generator.com/zT_NwqNKE-l1 to generate the random
    # data. Currently use this template in `students_generator.js`.
    students = utils.get_list_of_students("students.json")

    for student in students:
        print("student: Id={} GPA={} DFW={}".format(
            student.student_id, student.gpa, student.dfw_rate))

        print("math classes: {}".format(student.get_courses("MATH")))
        print("cis classes: {}\n".format(student.get_courses("CIS")))

    # cis121students = calculateNumberInCIS121(students, number incoming)

def main2():
    CIS115 = Course("CIS-115", 4, "C", False)
    CIS121 = Course("CIS-121", 4, "C", False)
    CIS122 = Course("CIS-122", 4, "C", False)
    CIS223 = Course("CIS-223", 4, "C", False)
    CIS224 = Course("CIS-224", 4, "C", False)
    MATH121 = Course("MATH-121", 4, "C", True)

    CIS121.create_course_sequence([CIS115, CIS121, CIS122, CIS223, CIS224])

    CIS121.add_prereq(MATH121)

    print(CIS121.see_prereqs())

    print(CIS121.set_prereq_given_course_sequence())

    print(CIS121.set_prereq_for_given_course_sequence())







if __name__ == "__main__":
    main2()
