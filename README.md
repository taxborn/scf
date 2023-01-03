# Winter project
Winter 2022 project. Utilizes [Python](https://www.python.org/) and
[Pip](https://pypi.org/project/pip/). 

# Running the code
Currently the only requirements are [pytest](https://docs.pytest.org/en/7.2.x/),
which can be installed with the command:
```
pip install -r requirements.txt
```

Other than that, just run the main script:
```
python src/main.py
```

# Generating student data
Student data is generated in a configurable python script, located at [./student_generator.py](./student_generator.py). Running that generates `student-{cs, cit, mis, hi}.json` files, each with students of the respective major.

# Generating CSV of student data
CSV generation is done in another helper script, located at [./json-to-csv.py](./json-to-csv.py). Running that will look for the `student-{cs, cit, mis, hi}.json` files with student data, and compile to one `compiled_students.csv` file.

# Tests
The test suite utilizes [pytest](https://docs.pytest.org/en/7.2.x/). To execute
the tests, run:
```
pytest
```
