import math


class Course:
    def __init__(self, course_name, credits, min_grade,
                 is_math: bool | None = None):
        self.course_name = course_name
        self.credits = credits
        # The minimum grade needed to consider
        self.min_grade = min_grade
        self.is_math = self.is_math_course(is_math)
        self.prereqs: list[Course] = []
        self.prereq_for: list[Course] = []
        self.class_size = 0
        self.failure_rate = None
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

    def create_course_sequence(courses: list):
        """
        Given a list of courses, it links the each course with it's next
        and previous ones. It will link the i - 1's course as a prereq to
        course i, and course i will be made a prereq for course i + 1.
        """
        for (i, course) in enumerate(courses):
            if i != 0:
                course.add_prereq(courses[i - 1])

            if i != len(courses) - 1:
                course.add_prereq_for(courses[i + 1])

    def get_course_by_name(crs_name, courses):
        for course in courses:
            if course.course_name == crs_name:
                return course

        return None

    def get_failure_rate(self):
        return self.failure_rate

    def set_failure_rate(self, num: float):
        self.failure_rate = num

    def update_course_sizes(students, courses):
        for student in students:
            # print("student: Id={} GPA={} DFW={}".format(student.student_id, student.gpa, student.dfw_rate))
            # print("has taken " + str(len(student.course_history)) + " classes.\n")
            # get the students highest course
            highest_cis = student.highest_course_taken("CIS-115", courses)
            if highest_cis:
                highest_cis.class_size += 1
            """
            highest_math = student.highest_course_taken("MATH-121", courses)
            if highest_math:
                highest_math.class_size += 1
            """

    def add_prereq(self, course):
        """Adds given course to prereq list."""
        self.prereqs.append(course)

    def see_prereqs(self):
        """Returns list of Course objects prerequisite classes."""
        return [course for course in self.prereqs]

    def add_prereq_for(self, course):
        """Add to the list of courses that the course is a prerequisite for."""
        self.prereq_for.append(course)

    def see_prereq_for(self):
        """Returns a list of Course objects the course is a prerequisite for"""
        return [course for course in self.prereq_for]

    def get_number_of_sections(self):
        # TODO: Ceiling this? Floor it?
        return math.ceil(self.class_size / 25)

    def print_course(self):
        print("Course \"{}\":\n- Needed Spaces: {}.\n- Corresponding sections with 25 students: {}.\n".format(
            self.course_name, self.class_size, self.get_number_of_sections()))

    def get_prereqs_population(self):
        return self.prereqs[0].class_size
