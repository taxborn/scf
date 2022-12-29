class Professor:
    def __init__(self, name, courses):
        self.name = name
        self.availability = None  # Not sure how to type this
        self.courses = courses
        self.credit_load: int = self.get_credit_load()

    def get_credit_load(self) -> int:
        credits = 0

        for course in self.courses:
            credits += course.credits

        return credits
