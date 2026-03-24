# Goals

- Verify that the system meets requirements
- Identify defects
- Ensure product quality

# Scope of testing

- Login Page, Dashboard, Time, Interviews.

# Test strategy

- Automated testing

# Test Environment

- Hardware
    - Windows
- Software
    - Edge Browser
- Tools
    - Selenium Python

# Entry and Exit Criteria

- Entry
    - Code is ready for testing
    - Environment is set up

- Exit criteria
    - All tests executed
    - Acceptable pass rate achieved

# Test Cases

| ID  | Feature  | Precondition  | Steps  | Expected Result  |
|---|---|---|---|---|
|TC_01   | Login   | Account is created  | Enter credentials, press login  | User is logged in, dashboard is displayed   |
| TC_02    | Login - Failed   | None  | Enter invalid credentials, press login  | User stays on login page, error is displayed   |
| TC_03 | Password Forgottent | None | Click on Forgot your password, enter username | An email is sent to the matching account |
|TC_04   | Dashboard   | User is logged in   | Verify presence of all elements   | Elements are : Time at Work, My Actions, Quick Launch, Buzz Latest Posts, Employees on Leave Today, Employee Distribution by Sub Unit, Employee Distribution by Location|

# Defect Management

Anomalies will be included in the defect_report.md file

# Schedule 

From March 24th to March 27th.

# Deliverables

- Test cases
- Test reports
- Final test summary report