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
| TC_03 | Testing required fields | None | Click on login without credentials | A red "Required" should appear under empty fields |
| TC_04 | Navigatig to password forgotten | None | Click on Forgot your password | Navigation to the password forgotten page should be correct
| TC_05 | Password Forgotten | Be on password forgotten page | Enter username, click Reset Password | An email is sent to the matching account |
|TC_06   | Dashboard   | User is logged in   | Verify presence of all elements   | Elements are : Time at Work, My Actions, Quick Launch, Buzz Latest Posts, Employees on Leave Today, Employee Distribution by Sub Unit, Employee Distribution by Location|
|TC_07| Dashboard side panel | User is logged in | Count number of expected links and their names| All of the expected links display and their names match
|TC_08 | Dashboard side panel filtering | User is logged in | Input value "Admin" in the search filter on the side panel | The filtered list of options only consists of the "Admin" option | 

# Defect Management

Anomalies will be included in the Defect_report.md file

# Schedule 

From March 24th to March 27th.

# Deliverables

- Test cases
- Test reports
- Final test summary report