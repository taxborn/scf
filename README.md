# Winter project
Winter 2022 project. Utilizes [Python](https://www.python.org/) and
[Pip](https://pypi.org/project/pip/). This currently utilizes test data
in [students.json](./students.json), which is generated programatically from 
[json-generator.com](https://app.json-generator.com), with the template used 
stored in [students_generator.js](./students_generator.js).

# Running the code
Currently the only requirements are [pytest](https://docs.pytest.org/en/7.2.x/)

Other than that, just run the main script:
```
python src/main.py
```

# Tests
The test suite utilizes [pytest](https://docs.pytest.org/en/7.2.x/). To execute
the tests, run:
```
pytest
```
