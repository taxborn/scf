class Course:
    def __init__(self, course_name, credits, min_grade,
                 is_math: bool | None = None):
        self.course_name = course_name
        self.credits = credits
        # The minimum grade needed to consider
        self.min_grade = min_grade
        self.is_math = self.is_math_course(is_math)
        # TODO: Priority level B: check if a student tried to register but was
        # waitlisted, was full, etc..
        # self.attempted_to_register = False
        # TODO: figure out a way to attach semester taken for the course,
        # shouldn't be too hard, but utilizing the random data generator might
        # make this weird for working with test data. Might need to figure out
        # a way to programatically generate the test data.

    def is_math_course(self, is_math: bool | None = None) -> bool:
        """
        Returns true if it is a math course otherwise is a math course and
        returns false otherwise
        """
        # Check if we have a parameter passed to specify if it is a math course
        if is_math is not None:
            return is_math

        # Otherwise if the course name starts with "MATH" or "STAT", then we
        # know it's a math course
        if self.course_name.upper().startswith(("MATH", "STAT")):
            return True

        # Otherwise, return False
        return False
