class Course:
    def __init__(self, course_name, credits, min_grade,
                 is_math: bool | None = None):
        self.course_name = course_name
        self.credits = credits
        # The minimum grade needed to consider
        self.min_grade = min_grade
        # A way to differentiate
        self.is_math = self.is_math_course(is_math)
        # Course sequencing
        self.course_sequence = None
        self.prereqs: list[Course] = []
        self.prereq_for: list[Course] = []

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

    def create_course_sequence(self, courses: list):
        self.course_sequence = courses

    def add_prereq(self, course):
        self.prereqs.append(course)

    def see_prereqs(self):
        return [course for course in self.prereqs]

    def set_prereq_given_course_sequence(self):
        for i in range(len(self.course_sequence)):
            if self.course_sequence[i].course_name == self.course_name:
                self.prereqs.append(self.course_sequence[i-1])
                break
        return self.prereqs

    def add_prereq_for(self, course):
        self.prereq_for.append(course)

    def see_prereq_for(self):
        return [course for course in self.prereq_for]

    def set_prereq_for_given_course_sequence(self):
        for i in range(len(self.course_sequence)):
            if self.course_sequence[i].course_name == self.course_name:
                self.prereq_for.append(self.course_sequence[i+1])
                break
        return self.prereq_for