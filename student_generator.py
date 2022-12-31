import uuid
import random


def main():
    grades = ["A", "A-", "B+", "B", "B-",
              "C+", "C", "C-", "D+", "D", "D-", "F"]

    courses = [("MATH-098", 3), ("MATH-121", 4), ("CIS-115", 4),
               ("CIS-121", 4), ("CIS-122", 4), ("CIS-223", 4), ("CIS-224", 4)]

    # open the file
    f1 = open("students.json", "w")
    # write the header
    f1.write("{\"students\":[")

    number_of_existing_students = 300
    number_of_incoming_freshman = 100
    probability_to_retake = 0.05
    probability_to_have_programming_experience = 0.20

    for i in range(number_of_existing_students):
        # the students id
        f1.write("{\"id\": \"" + uuid.uuid4().hex + "\",\n")
        # if the student exists, let's give them programming experience
        f1.write("\"programming_experience\": true,")
        # courses header
        f1.write("\"courses\":[")

        # This determines how far they go in the courses
        courses_student_takes = random.randint(2, len(courses))
        grade = random.randint(0, len(grades) - 1)

        retake_roll = random.randint(0, 100)
        for course in range(courses_student_takes):
            # Give the course a chance of being retaken.
            if retake_roll <= probability_to_retake * 100:
                # Regenerate the grade index
                grade = random.randint(0, len(grades) - 1)

                f1.write(
                    "{\"name\":\"" + courses[course][0] + "\",\"grade\":\"" +
                    grades[grade] + "\",\"credits\":" + str(courses[course][1]) + "}")

                f1.write(",")
            f1.write(
                "{\"name\":\"" + courses[course][0] + "\",\"grade\":\"" +
                grades[grade] + "\",\"credits\":" + str(courses[course][1]) + "}")

            if course != courses_student_takes - 1:
                f1.write(",\n")

        f1.write("]\n}")

        if i != number_of_existing_students and number_of_incoming_freshman > 0:
            f1.write(",\n")

    for i in range(number_of_incoming_freshman):
        # the students id
        f1.write("{\"id\": \"" + uuid.uuid4().hex + "\",\n")
        # if the student exists, let's give them programming experience
        programming_exp = random.randint(0, 9)

        if programming_exp < probability_to_have_programming_experience * 10:
            # if the incoming student has programming experience, it depends
            # on their math level. if in MATH-115 (precalc) or higher,
            # Place in 121 if they want.
            f1.write("\"programming_experience\": true,")
        else:
            # if they don't have programming experience, they start at CIS-115
            # no matter what
            f1.write("\"programming_experience\": false,")
        # courses header
        f1.write("\"courses\":[")

        # This determines how far they go in the courses
        courses_student_takes = random.randint(2, len(courses) - 1)
        grade = random.randint(0, len(grades) - 1)

        for course in range(courses_student_takes):
            f1.write(
                "{\"name\":\"" + courses[course][0] + "\",\"grade\":\"" +
                grades[grade] + "\",\"credits\":" + str(courses[course][1]) + "}")

            if course != courses_student_takes - 1:
                f1.write(",")

            f1.write("\n")
        f1.write("]\n}")
        if i != number_of_incoming_freshman - 1:
            f1.write(",\n")

            # close the header
    f1.write("]}")
    # close the file
    f1.close()


if __name__ == "__main__":
    main()
