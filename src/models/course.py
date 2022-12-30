class Course:
    def __init__(self, course_name, credits, min_grade,
                 is_math: bool | None = None):
        self.course_name = course_name
        self.credits = credits
        # The minimum grade needed to consider
        self.min_grade = min_grade
        self.is_math = self.is_math_course(is_math)
        # Course sequencing
        self.course_sequence = None
        self.prereqs: list[Course] = []
        self.prereq_for: list[Course] = []
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

    def create_course_sequence(self, courses: list):
        """Encapsulates a course sequence as a list."""
        self.course_sequence = courses

    def add_prereq(self, course):
        """Adds given course to prereq list."""
        self.prereqs.append(course)

    def see_prereqs(self):
        """Returns list of Course objects prerequisite classes."""
        return [course for course in self.prereqs]

    def set_prereq_given_course_sequence(self):
        """Given the sequence, it's prior index is appended to prereq list."""
        for i in range(len(self.course_sequence)):
            if self.course_sequence[i].course_name == self.course_name:
                self.prereqs.append(self.course_sequence[i-1])
                break
        return self.prereqs

    def add_prereq_for(self, course):
        """Add to the list of courses that the course is a prerequisite for."""
        self.prereq_for.append(course)

    def see_prereq_for(self):
        """Returns a list of Course objects the course is a prerequisite for"""
        return [course for course in self.prereq_for]

    def set_prereq_for_given_course_sequence(self):
        """Given the sequence, its next index is appended to prereq_for list"""
        for i in range(len(self.course_sequence)):
            if self.course_sequence[i].course_name == self.course_name:
                self.prereq_for.append(self.course_sequence[i+1])
                break
        return self.prereq_for