import src.models.section as section
import src.models.professor as professor
import src.models.course as course


def test_section_professor():
    sec1 = section.Section("MATH-121", 1, 25)
    calc1 = course.Course("MATH-121", 4, "C-")
    calc2 = course.Course("MATH-122", 4, "C-")
    calc3 = course.Course("MATH-223", 4, "C-")

    prof = professor.Professor("Lin", [calc1, calc2, calc3])
    sec1.setProfessor(prof)

    assert sec1.professor.credit_load == 12
