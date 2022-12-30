class Section:
    # TODO: Re-add typing to class objects. Currently importing other classes
    # causes issues with pytest
    def __init__(self, course, section_id: int, num_students: int, professor=None):
        self.professor = professor
        self.course = course
        self.section_id = section_id
        # Should also be in the Course object?
        self.num_students = num_students

    def setProfessor(self, professor):
        self.professor = professor
