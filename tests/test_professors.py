import src.models.professor as professor
import src.models.course as course


def test_correct_course_load_computation():
    calc1 = course.Course("MATH-121", 4, "C-")
    calc2 = course.Course("MATH-122", 4, "C-")
    calc3 = course.Course("MATH-223", 4, "C-")

    prof = professor.Professor("Lin", [calc1, calc2, calc3])

    assert prof.credit_load == 12
