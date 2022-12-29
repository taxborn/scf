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
