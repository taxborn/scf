class Classes:

    def __init__(self, class_name, grade_constraint, is_computing):
        self.class_name = class_name
        self.grade_constraint = grade_constraint
        self.is_computing = is_computing

    def is_computing_course(self):
        """Returns true if computing course otherwise is a math course and returns false"""
        return self.is_computing == True


if __name__ == "__main__":
    c1 = Classes("Math 121", "C-", False)
    print(c1.is_computing)
