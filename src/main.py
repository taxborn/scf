import utils
from models.student import Student
from models.course import Course


def main():
    # Used https://app.json-generator.com/zT_NwqNKE-l1 to generate the random
    # data. Currently use this template in `students_generator.js`.
    math121 = Course("MATH-121", 4, "C-")
    cis115 = Course("CIS-115", 4, "C-")
    cis121 = Course("CIS-121", 4, "C-")
    cis122 = Course("CIS-122", 4, "C-")
    cis223 = Course("CIS-223", 4, "C-")
    cis224 = Course("CIS-224", 4, "C-")
    courses = [math121, cis115, cis121, cis122, cis223, cis224]
    Course.create_course_sequence(courses)
    students = utils.get_list_of_students("students2.json", courses)

    for student in students:
        print("student: Id={} GPA={} DFW={}".format(
            student.student_id, student.gpa, student.dfw_rate))

        print("math classes: {}".format(student.get_courses("MATH")))
        print("cis classes: {}\n".format(student.get_courses("CIS")))

        # get the students highest course
        print(student.highest_course_taken("CIS-115", courses))

    # cis121students = calculateNumberInCIS121(students, number incoming)


if __name__ == "__main__":
    main()
