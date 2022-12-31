import uuid
import random


def main():
    f1 = open("students2.json", "w")
    # write the header
    f1.write("{\"students\":[")

    grades = ["A", "A-", "B+", "B", "B-",
              "C+", "C", "C-", "D+", "D", "D-", "F"]

    for i in range(5):
        # the students id
        f1.write("{\"id\": \"" + uuid.uuid4().hex + "\",")
        # courses header
        f1.write("\"courses\":[")
        a = random.randint(0, 5)
        courses = ["MATH-121", "CIS-115", "CIS-121",
                   "CIS-122", "CIS-223", "CIS-224"]

        if a == 0:
            b = random.randint(0, len(grades) - 1)
            # no class history, an incoming freshman
            f1.write(
                "{\"name\":\"MATH-098\",\"grade\":\"" + grades[b] + "\",\"credits\":4}")
        else:
            b = random.randint(0, len(courses) - 1)
            for j in range(b):
                f1.write(
                    "{\"name\":\"" + courses[j] + "\",\"grade\":\"" + grades[b] + "\",\"credits\":4}")

                if j != b - 1:
                    f1.write(",")

                f1.write("\n")
        f1.write("]\n}")
        if i != 4:
            f1.write(",\n")

            # close the header
    f1.write("]}")
    # close the file
    f1.close()


if __name__ == "__main__":
    main()
