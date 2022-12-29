import src.models.student as student


def test_4_0_student():
    stud = student.Student(
        "A", [("MATH-122", "A", 4), ("MATH-122", "C", 4), ("CIS-121", "A", 4)])
    assert stud.gpa == 4.0


def test_3_7_student():
    stud = student.Student(
        "A", [("MATH-122", "A-", 4), ("MATH-122", "C", 4), ("CIS-121", "A-", 4)])
    assert stud.gpa == 3.67


def test_rand_student():
    stud = student.Student(
        "A", [("MATH-122", "B-", 4), ("MATH-122", "C", 4),
              ("CIS-121", "C+", 4), ("CIS-121", "D", 4)])
    assert stud.gpa == 2.5
