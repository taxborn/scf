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


def test_retaking_impacts_DFW():
    math122 = course.Course("MATH-122", 4, "C-")
    cis121 = course.Course("CIS-121", 4, "C-")

    stud = student.Student(
        "A", [(math122, "A"), (math122, "B-"), (cis121, "A")])

    assert stud.dfw_rate == 1/3


def test_retaking_and_grades_impacts_DFW():
    math122 = course.Course("MATH-122", 4, "C-")
    cis121 = course.Course("CIS-121", 4, "C-")

    stud = student.Student(
        "A", [(math122, "A"), (math122, "D"), (cis121, "A")])

    assert stud.dfw_rate == 2/3


def test_getting_math_classes():
    math122 = course.Course("MATH-122", 4, "C-")
    cis121 = course.Course("CIS-121", 4, "C-")

    stud = student.Student(
        "A", [(math122, "A"), (math122, "D"), (cis121, "A")])

    math_classes = stud.get_courses("MATH")

    # One class, taken twice
    assert len(math_classes) == 1
    assert len(math_classes["MATH-122"]) == 2


def test_creating_course_sequences():
    CIS115 = course.Course("CIS-115", 4, "C")
    CIS121 = course.Course("CIS-121", 4, "C")
    CIS122 = course.Course("CIS-122", 4, "C")
    CIS223 = course.Course("CIS-223", 4, "C")
    CIS224 = course.Course("CIS-224", 4, "C")
    MATH121 = course.Course("MATH-121", 4, "C")
    CIS121.add_prereq(MATH121)

    course.Course.create_course_sequence(
        [CIS115, CIS121, CIS122, CIS223, CIS224])

    stud = student.Student("AAA", [(CIS115, "B"), (CIS121, "C-"),
                                   (CIS122, "A"), (CIS223, "D")])

    print("Highest course taken: " +
          stud.highest_course_taken(CIS115).course_name)
