import utils
from models.course import Course

"""
Coures for use in the lower functions
"""
math098 = Course("MATH-098", 4, "C-")
math115 = Course("MATH-115", 4, "C-")
math121 = Course("MATH-121", 4, "C-")
math122 = Course("MATH-122", 4, "C-")
math247 = Course("MATH-247", 4, "C-")
math280 = Course("MATH-280", 4, "C-")
cis115 = Course("CIS-115", 4, "C-")
cis121 = Course("CIS-121", 4, "C-")
cis122 = Course("CIS-122", 4, "C-")
cis223 = Course("CIS-223", 4, "C-")
cis224 = Course("CIS-224", 4, "C-")

"""
Parameters used in running the capacity projection
"""
cs_starting_size = 100
mis_starting_size = 50
cit_starting_size = 50
hi_starting_size = 10
semesters_to_simulate = 3


def main():
    print(f"{'':-^50}")
    string = "Which major do you want to run stats for?"
    print(f"{string:^50}")
    print("\n\t1. CS\n\t2. MIS\n\t3. CIT\n\t4. HI\n\t5. All department majors")
    inp = int(input("\nSelect option: "))
    print(f"\n{'':-^50}")

    if inp == 1:
        CS()
    elif inp == 2:
        MIS()
    elif inp == 3:
        CIT()
    elif inp == 4:
        HI()
    elif inp == 5:
        all()
    else:
        print("Invalid input")


def CS():
    # Step 0: Set course failure rates, each index corresponds to the index in courses.
    core_failure_rates = [.1, .1, .1, .1, .1]
    core_courses = [cis115, cis121, cis122, cis223, cis224]
    math_failure_rates = [.1, .1, .1, .1, .1, .1]
    math_courses = [math098, math115, math121, math122, math247, math280]

    # Step 1: Create the courses

    # Step 2: Create a course sequence. All this is doing is hooking each
    # Course up to one another

    data_printer("students-cs.json", core_courses, math_courses,
                 core_failure_rates, math_failure_rates, cs_starting_size)


def MIS():
    # Step 0: Set course failure rates, each index corresponds to the index in courses.
    core_failure_rates = [.1, .1, .1, .1, .1, .1]
    math_failure_rates = [.1, .1]

    # Step 1: Create a course sequence. All this is doing is hooking each
    # Course up to one another
    core_courses = [cis115, cis121, cis122, cis223]
    math_courses = [math098, math115, math121]

    data_printer("students-mis.json", core_courses, math_courses,
                 core_failure_rates, math_failure_rates, mis_starting_size)


def CIT():
    # Step 0: Set course failure rates, each index corresponds to the index in courses.
    core_failure_rates = [.1, .1, .1, .1, .1]
    core_courses = [cis115, cis121, cis122, cis223, cis224]
    math_failure_rates = [.1, .1, .1]
    math_courses = [math098, math115, math121]
    # Step 1: Create a course sequence. All this is doing is hooking each
    # Course up to one another
    data_printer("students-cit.json", core_courses, math_courses,
                 core_failure_rates, math_failure_rates, cit_starting_size)


def HI():
    # https://www.mnsu.edu/academics/academic-catalog/undergraduate/health-informatics/health-informatics-bs/#:~:text=The%20Health%20Informatics%20program%20prepares,delivery%2C%20management%2C%20and%20research.
    # Step 0: Set course failure rates, each index corresponds to the index in courses.
    core_failure_rates = [.1, .1, .1, .1]
    core_courses = [cis115, cis121, cis122, cis223]
    math_failure_rates = [.1, .1, .1]
    math_courses = [math098, math115, math121]

    # Step 1: Create a course sequence. All this is doing is hooking each
    # Course up to one another

    data_printer("students-hi.json", core_courses, math_courses,
                 core_failure_rates, math_failure_rates, hi_starting_size)


def all():
    """
    This is really ugly and should be rewritten, but works for now
    """

    """
    CS
    """

    # CS Major classes
    math_courses = [math098, math115, math121, math122, math247, math280]
    core_courses = [cis115, cis121, cis122, cis223, cis224]

    # Construct their sequences
    Course.create_course_sequence(core_courses)
    Course.create_course_sequence(math_courses)

    # Merge the courses to one list
    courses = math_courses + core_courses

    students_cs = utils.get_list_of_students("students-cs.json", courses)

    loading = f"Loaded {len(students_cs)} Computer Science students"
    print(f"|{loading:^48}|")

    # Populate each course with their respective class sizes.
    Course.update_course_sizes(students_cs, courses)

    """
    CIT
    """

    # CIT Major classes
    core_courses = [cis115, cis121, cis122, cis223, cis224]
    math_courses = [math098, math115, math121]

    # Construct their sequences
    Course.create_course_sequence(core_courses)
    Course.create_course_sequence(math_courses)

    # Merge the courses to one list
    courses = math_courses + core_courses

    students_cit = utils.get_list_of_students("students-cit.json", courses)

    loading = f"Loaded {len(students_cit)} CIT students"
    print(f"|{loading:^48}|")

    # Populate each course with their respective class sizes.
    Course.update_course_sizes(students_cit, courses)

    """
    MIS
    """

    # MIS Major classes
    core_courses = [cis115, cis121, cis122, cis223, cis224]
    math_courses = [math098, math115, math121]

    # Construct their sequences
    Course.create_course_sequence(core_courses)
    Course.create_course_sequence(math_courses)

    # Merge the courses to one list
    courses = math_courses + core_courses

    students_mis = utils.get_list_of_students("students-mis.json", courses)

    loading = f"Loaded {len(students_mis)} MIS students"
    print(f"|{loading:^48}|")

    # Populate each course with their respective class sizes.
    Course.update_course_sizes(students_mis, courses)

    """
    HI
    """

    # HI Major classes
    core_courses = [cis115, cis121, cis122, cis223, cis224]
    math_courses = [math098, math115, math121]

    # Construct their sequences
    Course.create_course_sequence(core_courses)
    Course.create_course_sequence(math_courses)

    # Merge the courses to one list
    courses = math_courses + core_courses

    students_hi = utils.get_list_of_students("students-hi.json", courses)

    loading = f"Loaded {len(students_hi)} Health Informatics students"
    print(f"|{loading:^48}|")

    # Populate each course with their respective class sizes.
    Course.update_course_sizes(students_hi, courses)

    students = students_cs + students_cit + students_mis + students_hi

    loading = f"For a total of {len(students)} students"
    print(f"|{loading:^48}|")
    print(f"|{'':-^48}|")
    loading = f"Simulating {semesters_to_simulate} semesters into the future"
    print(f"|{loading:^48}|")
    print(f"{'':-^50}\n")

    # Create an array of all courses
    courses = [math098, math115, math121, math122, math247,
               math280, cis115, cis121, cis122, cis223, cis224]

    # Their failure rates
    failure_rates = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
    set_course_failure_rates(courses, failure_rates)

    new_size = cs_starting_size + mis_starting_size + \
        cit_starting_size + hi_starting_size

    # Step 5: Simulate semesters
    for i in range(semesters_to_simulate):
        math098.course_size += new_size
        cis115.course_size += new_size

        print(f"{'':-^50}")
        message = f"Projecting course sizes {i + 1} semester(s) out"
        print(f"|{message:^48}|")
        print(f"{'':-^50}\n")
        courses = course_updater(courses)

        course_printer(courses)


def data_printer(file, core_courses, math_courses, core_failure_rates, math_failure_rates, start_size):
    Course.create_course_sequence(core_courses)
    Course.create_course_sequence(math_courses)
    core_courses += math_courses

    # Step 3: Construct a list of students. This is currently loaded inmain
    # from the students.json file, which is generated by student_generator.py
    # file. It will soon be able to be parameterized to simulate random data
    students_core = utils.get_list_of_students(file, core_courses)

    loading = f"Loaded {len(students_core)} students"
    print(f"|{loading:^48}|")
    loading = f"With {start_size} students incoming / semester"
    print(f"|{loading:^48}|")
    loading = f"Simulating {semesters_to_simulate} semesters into the future"
    print(f"|{loading:^48}|")

    # Step 4: Populate each course with their respective class sizes.
    Course.update_course_sizes(students_core, core_courses)

    set_course_failure_rates(
        core_courses, core_failure_rates + math_failure_rates)

    core_courses[0].course_size = start_size
    math_courses[0].course_size = start_size

    # Step 5: Simulate semesters
    for i in range(semesters_to_simulate):
        print(f"{'':-^50}")
        message = f"Projecting course sizes {i + 1} semester(s) out"
        print(f"|{message:^48}|")
        print(f"{'':-^50}\n")
        core_courses = course_updater(core_courses)
        math_courses = course_updater(math_courses)
        core_courses[0].course_size = start_size
        math_courses[0].course_size = start_size
        course_printer(core_courses)


def course_updater(courses):
    # TODO Could add and update semester here
    # Step 5: Simulate a core class semester
    for i in range(len(courses) - 1, 0, -1):
        # Update the population here through indexing
        # Switch 0.75 here with the classes failure rate
        courses[i].course_size = int(
            (1 - courses[i].get_failure_rate()) * courses[i - 1].course_size)
    return courses


def set_course_failure_rates(courses: list, failure_rates: list):
    for i in range(len(courses)):
        courses[i].set_failure_rate(failure_rates[i])
    return courses


def course_printer(courses: list):
    for course in courses:
        course.print_course()


if __name__ == "__main__":
    main()
