from models.course import Course


class Student:
    def __init__(self, student_id, course_history):
        # I doubt we are getting names, so I figure some type of identifier is
        # necessary?
        self.student_id = student_id
        # A list of tuples in the format [(Course Object, Grade)]. e.g.
        # (Course("MATH-122", 4, "C-"), "A")
        self.course_history = course_history
        # percentage of students with grade <= D, maybe this should be a
        # variable in class.
        self.dfw_rate = self.calculate_dfw_rate()
        self.gpa = self.calculate_gpa()

        self.programming_experience = None
        self.precalc = None  # has_precalc():

    def calculate_gpa(self) -> float:
        """
        Calculates the GPA of a Student. This takes into account that a student
        may have taken a course many times, and only counts their higest grade
        achieved in that course.
        """
        if len(self.course_history) == 0:
            return 0
        grade_map = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0,
                     "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33,
                     "D": 1.0, "D-": 0.67, "F": 0, "P": 0, "F": 0}
        class_history = {}
        grade_points = 0

        # Fill the dictionary with { "course": [grade(s) the student got)
        for (course, grade) in self.course_history:
            class_history.setdefault(course.course_name,
                                     []).append((grade, course.credits))

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

    def calculate_dfw_rate(self) -> float:
        """
        Sets the DFW (D / F / Withdraw) rate of the student.

        Current ideas: Getting # of classes retaken (number of duplicates in
        self.course_history) as a proportion of total classes taken.
        """
        if len(self.course_history) == 0:
            # Not sure if you start with a 0.0 or 4.0, going to assume 0.0 for
            # now.
            return 0
        dfw = 0

        for course in self.course_history:
            # Check if the grade was a D/F
            if course[1] in ["W", "F", "D-", "D", "D+"]:
                dfw += 1

        return dfw / len(self.course_history)

    def get_start_class(self) -> bool:
        """Decide whether student should start in CIS115 or CIS121"""
        if self.programming_experience:
            # TODO: check if enrolled class is MATH 115 or ahead. If true
            # student can take CIS 121, else can
            # if math enrollment >= MATH115: return True
            # else: return False
            return True
        else:
            return False

    # TODO
    # - Check if student can move to next class (Check if it has defined prereqs from Course class)
    def has_precalc(self):
        pass

    def get_courses(self, start: str) -> dict[str, list[str]]:
        """
        Gets all the courses that have the starting course name. E.g. :
        student.get_courses("MATH") gives you a dictionary of all the
        math classes the student took and their grades

        TODO: Add semester
        """
        class_history = {}
        # Fill the dictionary with { course obj: [grade(s) the student got] }
        for (course, grade) in self.course_history:
            if course.course_name.upper().startswith(start.upper()):
                class_history.setdefault(course, []).append(grade)

        return class_history

    def highest_course_taken(self, starting_course_name: str, courses, recursed=False):
        """
        Get the highest course the student has taken of a given major. We can
        assume a linear progression since most students follow the path (?). To
        compute this, we also assume that the course(s) have been populated
        with their prerequisites and their respective classes they are
        prerequisites of.

        TODO: Fix wording?
        """
        course = Course.get_course_by_name(
            starting_course_name, courses)

        # Check if the course is in the courses
        if course is None:
            return None

        # Searches along the path of the same major classes (CIS will only
        # search along other CIS courses)
        to_search = self.get_courses(
            course.course_name.split("-")[0]).keys()

        if course not in to_search:
            return None

        if len(course.see_prereq_for()) == 0:
            # this is the last class in the sequence
            return course

        # Check if the course is a prereq for something
        if len(course.see_prereq_for()) > 0:
            if course.see_prereq_for()[0] in to_search:
                return self.highest_course_taken(
                    course.see_prereq_for()[0].course_name, courses, True)

            return course

        return None
