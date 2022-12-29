class Course:
    def __init__(self, course_name, credits, min_grade,
                 is_math: bool | None = None):
        self.course_name = course_name
        self.credits = credits
        # The minimum grade needed to consider
        self.min_grade = min_grade
        # A way to differentiate
        self.is_math = self.is_math_course(is_math)

    def is_math_course(self, is_math: bool | None = None) -> bool:
        """
        Returns true if it is a math course otherwise is a math course and
        returns false otherwise
        """
        # Check if we have a parameter passed to specify if it is a math course
        if is_math is not None:
            return is_math

        # Otherwise if the course name starts with "MATH", then we know it's a
        # math course
        if self.course_name.upper().startswith(("MATH", "STAT")):
            return True

        # Otherwise, return False
        return False
