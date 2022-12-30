import src.models.student as student
import src.models.course as course


def test_4_0_student():
    math122 = course.Course("MATH-122", 4, "C-")
    cis121 = course.Course("CIS-121", 4, "C-")

    stud = student.Student(
        "A", [(math122, "A"), (math122, "B-"), (cis121, "A")])
    assert stud.gpa == 4.0


def test_3_7_student():
    math122 = course.Course("MATH-122", 4, "C-")
    cis121 = course.Course("CIS-121", 4, "C-")

    stud = student.Student(
        "A", [(math122, "A-"), (math122, "C+"), (cis121, "A-")])
    assert stud.gpa == 3.67


def test_rand_student():
    math122 = course.Course("MATH-122", 4, "C-")
    cis121 = course.Course("CIS-121", 4, "C-")

    stud = student.Student(
        "A", [(math122, "B-"), (math122, "C"), (cis121, "C+"), (cis121, "D")])

    assert stud.gpa == 2.5
