import professor as prof
class Sections:

    def __init__(self, class_name, section_id, num_students):
        self.professor = None
        self.class_name = class_name
        self.section_id = section_id
        self.num_students = num_students

    def setProffesor(self, professor: type[prof.Professor]):
        self.professor = professor

if __name__ == "__main__":
    s1 = Sections("Math 121", 1,25)
    p1 = prof.Professor(12, 4)
    s1.setProffesor(p1)

    print(s1.professor.getCreditLoad())
