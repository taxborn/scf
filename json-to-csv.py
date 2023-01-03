# Python program to convert
# JSON file to CSV
import json
import csv

# Opening JSON file and loading the data
# into the variable data
with open('students-cs.json') as json_file:
    cs_data = json.load(json_file)
with open('students-cit.json') as json_file:
    cit_data = json.load(json_file)
with open('students-mis.json') as json_file:
    mis_data = json.load(json_file)
with open('students-hi.json') as json_file:
    hi_data = json.load(json_file)

cs_students = cs_data['students']
cit_students = cit_data['students']
mis_students = mis_data['students']
hi_students = hi_data['students']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)


def print_student(student):
    output = []
    output.append(student["id"])
    output.append(student["programming_experience"])

    # Writing data of CSV
    for course in student["courses"]:
        output.append("({}: {})".format(course["name"], course["grade"]))

    csv_writer.writerow(output)


# Counter variable used for writing
# headers to the CSV file
count = 0

for student in cs_students:
    if count == 0:
        # Writing headers of CSV file
        header = student.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV
    print_student(student)

for student in cit_students:
    print_student(student)

for student in mis_students:
    print_student(student)

for student in hi_students:
    print_student(student)


data_file.close()
