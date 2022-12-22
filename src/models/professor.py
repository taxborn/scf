class Professor:
    def __init__(self, availability, courses):
        self.availability = availability
        # A list of tuple tuple of (Class, credits)
        self.courses = courses
        self.credit_load = getCreditLoad()

    def getCreditLoad(self):
        credits = 0

        for clazz in self.courses:
            credits += clazz[1]

        return credits
