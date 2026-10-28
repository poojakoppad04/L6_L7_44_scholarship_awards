# L6_L7 — Scholarship Awards

## Lab 6: Code and Branch Coverage Analysis

### Objective

The objective of this lab is to test the Scholarship Awards application using pytest and measure its statement and branch coverage using coverage.py.

### About the Application

The application calculates scholarship award amounts based on category, marks, income level and renewal status. It also checks applicant eligibility and determines application status.

### Files

| File | Description |
|---|---|
| `scholarship_awards.py` | Python module being tested |
| `test_scholarship_awards.py` | Starter test file |
| `CodeCoverageTest_PES2UG24CS352_application.py` | Test cases for statement/code coverage |
| `BranchCoverageTest_PES2UG24CS352_application.py` | Test cases for branch coverage |
| `SE1.png` – `SE6.png` | Lab screenshots and test evidence |

### Tools Used

- Python 3.13
- pytest
- coverage.py

### Running the Tests

Run the following commands from the Lab 6 directory.

**1. Code Coverage Tests**

```powershell
python -m pytest CodeCoverageTest_PES2UG24CS352_application.py -v
python -m coverage run -m pytest CodeCoverageTest_PES2UG24CS352_application.py
python -m coverage report -m
```

**2. Branch Coverage Tests**

```powershell
python -m pytest BranchCoverageTest_PES2UG24CS352_application.py -v
python -m coverage run --branch -m pytest BranchCoverageTest_PES2UG24CS352_application.py
python -m coverage report -m
```

### Results

**Code Coverage**
- Tests passed: 12
- Statement coverage: 100%

**Branch Coverage**
- Tests passed: 35
- Statement coverage: 100%
- Branch coverage: 100%
- Partial branches: 0

### Conclusion

The Scholarship Awards application was tested using separate test suites for code coverage and branch coverage. All 12 code coverage tests and 35 branch coverage tests passed. The reported statement and branch coverage reached 100%.

Refer to the lab handout for the complete requirements. Lab 7 will be added to this repository separately.
