class Student:
    def __init__(self, student_id: str, course_history, dfw_rate: float, programming_experience: bool):
        # I doubt we are getting names, so I figure some type of identifier is
        # necessary?
        self.student_id = student_id
        # A list of tuples in the format [(Course, Grade, Credits)]. e.g.
        # ("MATH-122", "A")
        self.course_history: list[tuple[str, str, int]] = course_history
        # percentage of students with grade <= D, maybe this should be a
        # variable in class.
        self.dfw_rate = dfw_rate
        self.programming_experience = programming_experience
        self.precalc = None  # has_precalc():
        self.gpa = None  # get_gpa()

    def get_gpa(self) -> float:
        """
        Calculates the GPA of a Student. Calculates off of self.course_history
        """
        grade_points = 0
        # TODO: How to handle W/Z/I?
        grade_dict = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0,
                      "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33,
                      "D": 1.0, "D-": 0.67, "F": 0, "P": 0, "F": 0}

        for course in self.course_history:
            # TODO: Create a cleaning function to remove courses that were
            # repeated, and take the highest results.

            # TODO: Take into account P/F classes grades.
            #                Credits                Grade
            grade_points += course[2] * grade_dict[course[1]]

        gpa = grade_points / len(self.course_history)
        self.gpa = gpa
        return gpa

    def get_start_class(self) -> bool:
        """Decide whether student should start in CIS115 or CIS121"""
        if self.programming_experience:
            # TODO: check if enrolled class is MATH 115 or ahead. If true student can take CIS 121, else can
            # if math enrollment >= MATH115: return True
            # else: return False
        else:
            return False

    #TODO
    def has_precalc(self):
        pass

    #TODO
    def highest_grade(self) -> str:
        pass