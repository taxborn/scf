class Student:
    def __init__(self, student_id, course_history):
        # I doubt we are getting names, so I figure some type of identifier is
        # necessary?
        self.student_id = student_id
        # A list of tuples in the format [(Course, Grade, Credits)]. e.g.
        # ("MATH-122", "A", 4)
        # TODO: Change this to a list of tuples, containing the Course class
        # and the grade the student got.
        self.course_history: list[tuple[str, str, int]] = course_history
        # percentage of students with grade <= D, maybe this should be a
        # variable in class.
        # TODO: Calculate based off of what? number of classes retaken?
        self.dfw_rate = self.calculate_dfw_rate()
        self.gpa = self.calculate_gpa()

        self.programming_experience = None
        self.precalc = None  # has_precalc():

    def calculate_gpa(self):
        """
        Calculates the GPA of a Student. This takes into account that a student
        may have taken a course many times, and only counts their higest grade
        achieved in that course.
        """
        grade_map = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0,
                     "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33,
                     "D": 1.0, "D-": 0.67, "F": 0, "P": 0, "F": 0}
        class_history = {}
        grade_points = 0

        # Fill the dictionary with { "course": [grade(s) the student got)
        for (course, grade, credits) in self.course_history:
            class_history.setdefault(course, []).append((grade, credits))

        for courses in class_history:
            # class info is an array containing [(Grade, Credits)], e.g.
            # [("A", 4), ("B+", 4)]
            classes_list = class_history[courses]
            highest_grade = 0

            # loops over each grade found for a course
            for course in classes_list:
                # gets the highest grade between the current highest and the
                # grade being checked
                highest_grade = max(highest_grade, grade_map[course[0]])

            # grade points = grade_from_map * credits
            grade_points += highest_grade * classes_list[0][1]

        # len(dic) is how many successful classes taken,
        # tbd why I need to divide by 4 but it works
        return grade_points / len(class_history) / 4.0

    def calculate_dfw_rate(self):
        """
        Sets the DFW (D / F / Withdraw) rate of the student.

        Current ideas: Getting # of classes retaken (number of duplicates in self.course_history)
        """
        return 0

    def get_start_class(self) -> bool:
        """Decide whether student should start in CIS115 or CIS121"""
        if self.programming_experience:
            # TODO: check if enrolled class is MATH 115 or ahead. If true student can take CIS 121, else can
            # if math enrollment >= MATH115: return True
            # else: return False
        else:
            return False

    # TODO
    def has_precalc(self):
        pass
