# L6_L7_44 — Scholarship Awards

## Lab 6: Code and Branch Coverage Analysis

### Objective

To test the Scholarship Awards application using pytest and measure statement and branch coverage using coverage.py.

### About the Application

The application calculates scholarship award amounts based on category, marks, income level and renewal status. It also checks applicant eligibility and determines application status.

### Files

| File | Description |
|---|---|
| `scholarship_awards.py` | Python module under test |
| `test_scholarship_awards.py` | Starter test file |
| `CodeCoverageTest_PES2UG24CS352_application.py` | Code coverage test cases |
| `BranchCoverageTest_PES2UG24CS352_application.py` | Branch coverage test cases |
| `SE1.png` – `SE6.png` | Lab screenshots and test evidence |

### Tools Used

- Python 3.13
- pytest
- coverage.py

### Running the Tests

Run these commands from the Lab 6 directory.

**Code coverage tests**

```powershell
python -m pytest CodeCoverageTest_PES2UG24CS352_application.py -v
python -m coverage run -m pytest CodeCoverageTest_PES2UG24CS352_application.py
python -m coverage report -m
```

**Branch coverage tests**

```powershell
python -m pytest BranchCoverageTest_PES2UG24CS352_application.py -v
python -m coverage run --branch -m pytest BranchCoverageTest_PES2UG24CS352_application.py
python -m coverage report -m
```

### Results

**Code coverage**
- Tests passed: 12
- Statement coverage: 100%

**Branch coverage**
- Tests passed: 35
- Statement coverage: 100%
- Branch coverage: 100%
- Partial branches: 0

### Conclusion

Separate test suites were created for code coverage and branch coverage. All 12 code coverage tests and 35 branch coverage tests passed, with 100% statement and branch coverage reported.

Lab 7 will be added to this repository separately. Refer to the lab handout for the complete requirements.