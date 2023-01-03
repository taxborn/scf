# Python program to convert
# JSON file to CSV
import os
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

filename = "compiled_students.csv"

# Remove the file if it exists
if os.path.exists(filename):
    os.remove(filename)

# now we will open a file for writing
data_file = open(filename, "w")

# create the csv writer object
csv_writer = csv.writer(data_file)


def print_student(major, student):
    output = []
    output.append(student["id"])
    output.append(major)
    output.append(student["programming_experience"])

    # Writing data of CSV
    for course in student["courses"]:
        output.append("({}: {})".format(course["name"], course["grade"]))

    csv_writer.writerow(output)


# Counter variable used for writing
# headers to the CSV file
count = 0
header = ["Student ID", "Major", "Programming Experience?",
          "Courses (Course name, Grade Achieved)"]
csv_writer.writerow(header)

for student in cs_students:
    # Writing data of CSV
    print_student("CS", student)

for student in cit_students:
    print_student("CIT", student)

for student in mis_students:
    print_student("MIS", student)

for student in hi_students:
    print_student("HI", student)


data_file.close()
