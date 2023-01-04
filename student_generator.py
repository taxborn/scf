import os
import uuid
import random

grades = ["A", "A-", "B+", "B", "B-",
          "C+", "C", "C-", "D+", "D", "D-", "F"]

math_courses = [("MATH-098", 4), ("MATH-115", 4), ("MATH-121", 4),
                ("MATH-122", 4), ("MATH-247", 4), ("MATH-280", 4)]
cis_courses = [("CIS-115", 4), ("CIS-121", 4), ("CIS-122", 4),
               ("CIS-223", 4), ("CIS-224", 4)]
"""
Generator variables
"""
retake_probability = 0.05
prob_programming_exp = 0.20


def main():

    # The number of existing and incoming Computer Science majors
    existing_cs, incoming_cs = 70, 106
    # The number of existing and incoming Management Information Science majors
    existing_mis, incoming_mis = 54, 17
    # The number of existing and incoming Computer Information Technology majors
    existing_cit, incoming_cit = 224, 64
    # The number of existing and incoming Health Informatic majors
    existing_hi, incoming_hi = 8, 1

    generate_cs_students("students-cs.json", existing_cs, incoming_cs)
    generate_mis_students("students-mis.json", existing_mis, incoming_mis)
    generate_cit_students("students-cit.json", existing_cit, incoming_cit)
    generate_hi_students("students-hi.json", existing_hi, incoming_hi)


def generate_cs_students(filename, existing_students, incoming_students):
    # Remove the file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    # open the file
    file = open(filename, "w")

    # write the header
    file.write("{\"students\":[\n")

    """
    Generate the existing CS students
    """
    for i in range(existing_students):
        # student header
        file.write(student_header())
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(2, len(math_courses))
        num_of_cis_classes = random.randint(1, len(cis_courses))

        # Generate the math courses
        generate_math(file, num_of_math_classes, existing_students)

        file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, existing_students)

        file.write("]\n},\n")

    """
    Generate the incoming CS students
    """
    for i in range(incoming_students):
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, len(math_courses))
        num_of_cis_classes = random.randint(1, len(cis_courses) - 1)

        # when a student is coming in, they may or may not have programming
        # experience
        programming_exp = random.randint(0, 99)
        has_experience = programming_exp < prob_programming_exp * 100
        file.write(student_header(has_experience))

        # This determines how far they go in the courses
        # If they do not have experience, they are placed in CIS-115 no matter
        # their math level
        if has_experience:
            # TODO: Then consider their math level. For now gives what a 50/50 chance of being 115 or 121
            num_of_cis_classes = 1
        else:
            num_of_cis_classes = 0

        # Generate the math courses
        generate_math(file, num_of_math_classes, incoming_students, False)

        if num_of_cis_classes > 0:
            file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, incoming_students, False)

        if i != incoming_students - 1:
            file.write("]\n},\n")
        else:
            file.write("]\n}\n")

    # close the header
    file.write("]}")
    # close the file
    file.close()


def generate_mis_students(filename, existing_students, incoming_students):
    # Remove the file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    # open the file
    file = open(filename, "w")

    # write the header
    file.write("{\"students\":[\n")

    """
    Generate the existing MIS students
    """
    for i in range(existing_students):
        # student header
        file.write(student_header())
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, 3)
        num_of_cis_classes = random.randint(1, len(cis_courses) - 1)

        # Generate the math courses
        generate_math(file, num_of_math_classes, existing_students)

        file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, existing_students)

        file.write("]\n},\n")

    """
    Generate the incoming MIS students
    """
    for i in range(incoming_students):
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, 3)
        num_of_cis_classes = random.randint(1, len(cis_courses) - 1)

        # when a student is coming in, they may or may not have programming
        # experience
        programming_exp = random.randint(0, 99)
        has_experience = programming_exp < prob_programming_exp * 100
        file.write(student_header(has_experience))

        # This determines how far they go in the courses
        # If they do not have experience, they are placed in CIS-115 no matter
        # their math level
        if has_experience:
            # TODO: Then consider their math level. For now gives what a 50/50 chance of being 115 or 121
            num_of_cis_classes = 1
        else:
            num_of_cis_classes = 0

        # Generate the math courses
        generate_math(file, num_of_math_classes, incoming_students, False)

        if num_of_cis_classes > 0:
            file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, incoming_students, False)

        if i != incoming_students - 1:
            file.write("]\n},\n")
        else:
            file.write("]\n}\n")

    # close the header
    file.write("]}")
    # close the file
    file.close()


def generate_cit_students(filename, existing_students, incoming_students):
    # Remove the file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    # open the file
    file = open(filename, "w")

    # write the header
    file.write("{\"students\":[\n")

    """
    Generate the existing CIT students
    """
    for i in range(existing_students):
        # student header
        file.write(student_header())
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, 3)
        num_of_cis_classes = random.randint(1, len(cis_courses))

        # Generate the math courses
        generate_math(file, num_of_math_classes, existing_students)

        file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, existing_students)

        file.write("]\n},\n")

    """
    Generate the incoming CIT students
    """
    for i in range(incoming_students):
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, 3)
        num_of_cis_classes = random.randint(1, len(cis_courses) - 1)

        # when a student is coming in, they may or may not have programming
        # experience
        programming_exp = random.randint(0, 99)
        has_experience = programming_exp < prob_programming_exp * 100
        file.write(student_header(has_experience))

        # This determines how far they go in the courses
        # If they do not have experience, they are placed in CIS-115 no matter
        # their math level
        if has_experience:
            # TODO: Then consider their math level. For now gives what a 50/50 chance of being 115 or 121
            num_of_cis_classes = 1
        else:
            num_of_cis_classes = 0

        # Generate the math courses
        generate_math(file, num_of_math_classes, incoming_students, False)

        if num_of_cis_classes > 0:
            file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, incoming_students, False)

        if i != incoming_students - 1:
            file.write("]\n},\n")
        else:
            file.write("]\n}\n")

    # close the header
    file.write("]}")
    # close the file
    file.close()


def generate_hi_students(filename, existing_students, incoming_students):
    # Remove the file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    # open the file
    file = open(filename, "w")

    # write the header
    file.write("{\"students\":[\n")

    """
    Generate the existing HI students
    """
    for i in range(existing_students):
        # student header
        file.write(student_header())
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, 3)
        num_of_cis_classes = random.randint(1, len(cis_courses) - 2)

        # Generate the math courses
        generate_math(file, num_of_math_classes, existing_students)

        file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, existing_students)

        file.write("]\n},\n")

    """
    Generate the incoming HI students
    """
    for i in range(incoming_students):
        # This determines how far they go in the courses
        num_of_math_classes = random.randint(1, 3)
        num_of_cis_classes = random.randint(1, len(cis_courses) - 1)

        # when a student is coming in, they may or may not have programming
        # experience
        programming_exp = random.randint(0, 99)
        has_experience = programming_exp < prob_programming_exp * 100
        file.write(student_header(has_experience))

        # This determines how far they go in the courses
        # If they do not have experience, they are placed in CIS-115 no matter
        # their math level
        if has_experience:
            # TODO: Then consider their math level. For now gives what a 50/50 chance of being 115 or 121
            num_of_cis_classes = 1
        else:
            num_of_cis_classes = 0

        # Generate the math courses
        generate_math(file, num_of_math_classes, incoming_students, False)

        if num_of_cis_classes > 0:
            file.write(",\n")

        # Generate the CIS courses
        generate_cis(file, num_of_cis_classes, incoming_students, False)

        if i != incoming_students - 1:
            file.write("]\n},\n")
        else:
            file.write("]\n}\n")

    # close the header
    file.write("]}")
    # close the file
    file.close()


def generate_math(file, num_of_math_classes, num_of_students, existing=True):
    for course in range(num_of_math_classes):
        retake_roll = random.randint(0, 99)
        initial_grade = random.randint(0, len(grades) - 1)
        string = "{\"name\":\"" + math_courses[course][0] + \
            "\",\"grade\":\"" + grades[initial_grade] + "\",\"credits\":" + \
            str(math_courses[course][1]) + "}"

        file.write(string)
        # Give the course a chance of being retaken, or if the initial class' grade was low enough
        if existing and (retake_roll <= retake_probability * 100 or initial_grade > 6):
            # we always want to print a comma before a retake
            file.write(",")
            grade = random.randint(0, initial_grade)
            string = "{\"name\":\"" + math_courses[course][0] + \
                "\",\"grade\":\"" + grades[grade] + "\",\"credits\":" + \
                str(math_courses[course][1]) + "}"

            file.write(string)

        if course != num_of_math_classes - 1:
            file.write(",\n")


def generate_cis(file, num_of_cis_classes, num_of_students, existing=True):
    for course in range(num_of_cis_classes):
        retake_roll = random.randint(0, 99)
        initial_grade = random.randint(0, len(grades) - 1)
        string = "{\"name\":\"" + cis_courses[course][0] + \
            "\",\"grade\":\"" + grades[initial_grade] + "\",\"credits\":" + \
            str(cis_courses[course][1]) + "}"

        file.write(string)

        # Give the course a chance of being retaken, or if the initial class' grade was low enough
        if existing and (retake_roll <= retake_probability * 100 or initial_grade > 6):
            # we always want to print a comma before a retake
            file.write(",")
            grade = random.randint(0, initial_grade)
            string = "{\"name\":\"" + cis_courses[course][0] + \
                "\",\"grade\":\"" + grades[grade] + "\",\"credits\":" + \
                str(cis_courses[course][1]) + "}"

            file.write(string)

        if course != num_of_cis_classes - 1:
            file.write(",\n")


def student_header(exp: bool = True):
    string = ""
    string += "{{\"id\": \"{}\",\n".format(uuid.uuid4().hex)
    string += "\"programming_experience\": {},\n".format(str(exp).lower())
    # TODO: Major?
    string += "\"courses\": [\n"
    return string


if __name__ == "__main__":
    main()
