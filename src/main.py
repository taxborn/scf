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


if __name__ == "__main__":
    main()
