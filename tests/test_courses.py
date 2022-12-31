import src.models.course as course


def test_math_is_math():
    calc2 = course.Course("MATH-122", 4, "C-")

    assert calc2.is_math


def test_specifying_mathiness_to_true():
    intro_to_us_history = course.Course("POL-111", 4, "C-", True)

    assert intro_to_us_history.is_math


def test_specifying_mathiness_to_false():
    calc2 = course.Course("MATH-122", 4, "C-", False)

    assert not calc2.is_math


def test_stats_is_cooerced_to_math():
    probs_and_stats = course.Course("STAT-354", 4, "C-")

    assert probs_and_stats.is_math


def _115_course_object():
    CIS115 = course.Course("CIS-115", 4, "C", False)
    CIS121 = course.Course("CIS-121", 4, "C", False)
    CIS122 = course.Course("CIS-122", 4, "C", False)
    CIS223 = course.Course("CIS-223", 4, "C", False)
    CIS224 = course.Course("CIS-224", 4, "C", False)

    course.Course.create_course_sequence(
        [CIS115, CIS121, CIS122, CIS223, CIS224])

    return CIS121


def test_create_course_sequence():
    CIS115 = course.Course("CIS-115", 4, "C", False)
    CIS121 = course.Course("CIS-121", 4, "C", False)
    CIS122 = course.Course("CIS-122", 4, "C", False)
    CIS223 = course.Course("CIS-223", 4, "C", False)
    CIS224 = course.Course("CIS-224", 4, "C", False)
    CIS121.create_course_sequence([CIS115, CIS121, CIS122, CIS223, CIS224])

    assert CIS121.course_sequence == [CIS115, CIS121, CIS122, CIS223, CIS224]
