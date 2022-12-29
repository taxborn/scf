class Section:
    def __init__(self, class_name: str, section_id: int, num_students: int):
        self.professor = None
        # TODO: Should probably store the actual Course object
        self.class_name = class_name
        self.section_id = section_id
        # Should also be in the Course object?
        self.num_students = num_students

    def setProfessor(self, professor):
        self.professor = professor
