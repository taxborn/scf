import uuid
import random

grades = ["A", "A-", "B+", "B", "B-",
          "C+", "C", "C-", "D+", "D", "D-", "F"]
courses = [("MATH-098", 3), ("MATH-121", 4), ("CIS-115", 4),
           ("CIS-121", 4), ("CIS-122", 4), ("CIS-223", 4), ("CIS-224", 4)]


def main():
    # open the file
    f1 = open("students.json", "w")
    # write the header
    f1.write("{\"students\":[")

    # The number of existing students in the major
    number_of_existing_students = 300
    # The number of incoming freshman
    number_of_incoming_freshman = 100
    # The probability a student wikk retake a course
    retake_prob = 0.05
    # The probability the student has previous programming experience
    prog_exp_prob = 0.20

    generate_existing_students(
        f1, number_of_existing_students, retake_prob)
    generate_incoming_students(
        f1, number_of_incoming_freshman, prog_exp_prob)

    # close the header
    f1.write("]}")
    # close the file
    f1.close()


def student_header(exp: bool = True):
    string = ""
    string += "{{\"id\": \"{}\",\n".format(uuid.uuid4().hex)
    string += "\"programming_experience\": {},\n".format(str(exp).lower())
    # TODO: Major?
    string += "\"courses\": [\n"
    return string


def generate_existing_students(file, existing, retake_prob):
    for i in range(existing):
        # student header
        file.write(student_header())
        # This determines how far they go in the courses
        num_of_courses = random.randint(2, len(courses))
        retake_roll = random.randint(0, 99)

        for course in range(num_of_courses):
            # Give the course a chance of being retaken.
            if retake_roll <= retake_prob * 100:
                file.write(print_course(course, num_of_courses, True))
                # we always want to print a comma
                file.write(",")

            file.write(print_course(course, num_of_courses))

        file.write("]\n},")


def generate_incoming_students(file, number_incoming, prob_has_programming):
    for i in range(number_incoming):
        # when a student is coming in, they may or may not have programming
        # experience
        programming_exp = random.randint(0, 99)
        has_experience = programming_exp < prob_has_programming * 100
        file.write(student_header(has_experience))

        # This determines how far they go in the courses
        # If they do not have experience, they are placed in CIS-115 no matter
        # their math level
        if has_experience:
            # TODO: Then consider their math level
            courses_student_takes = random.randint(2, 4)
        else:
            courses_student_takes = 3

        for course in range(courses_student_takes):
            file.write(print_course(course, courses_student_takes))
            # For each course, generate a grade

            file.write("\n")
        file.write("]\n}")

        if i != number_incoming - 1:
            file.write(",\n")


def print_course(course, courses_student_takes, ignore_trailing: bool = False):
    grade = random.randint(0, len(grades) - 1)

    string = "{\"name\":\"" + courses[course][0] + "\",\"grade\":\"" + \
        grades[grade] + "\",\"credits\":" + str(courses[course][1]) + "}"

    if course != courses_student_takes - 1 and not ignore_trailing:
        string += ",\n"

    return string


if __name__ == "__main__":
    main()
