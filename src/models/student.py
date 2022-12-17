

class Student:

    def __init__(self, student_id, course_history):
        self.gpa = None #get_gpa()
        self.student_id = student_id  # I doubt we are getting names so I figure some type of identifier is necessary?
        self.course_history = course_history  # Tuple
        self.dfw_rate  # percentage of students with grade <= D, maybe this should be a variable in class.

    def get_gpa(self) -> float:
        """
        Calculates gpa given a tuple represented by (class, gpa)
        """
        grade_dict = {"A": 4, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33,
                   "D": 1.0, "F": 0}

        gpa = 0
        for grade in self.course_history:
            gpa += grade_dict[grade[1]]
        self.gpa = gpa/len(self.course_history)
        return self.gpa