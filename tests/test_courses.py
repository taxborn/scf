import src.models.course as course


def test_specifying_math_coursses():
    clazz = course.Course("MATH-122", "C+")

    assert clazz.is_math


def test_specifying_math_coursses_2():
    clazz = course.Course("CS-122", "C+")

    assert not clazz.is_math
