class Student:
    def __init__(self, student_id, course_history, dfw_rate):
        # I doubt we are getting names, so I figure some type of identifier is
        # necessary?
        self.student_id = student_id
        # A list of tuples in the format [(Course, Grade, Credits)]. e.g.
        # ("MATH-122", "A")
        self.course_history: list[tuple[str, str, int]] = course_history
        # percentage of students with grade <= D, maybe this should be a
        # variable in class.
        self.dfw_rate
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
