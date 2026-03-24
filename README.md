# Introduction

As part of my training for Sogeti, I was asked to do some automated tests. This project will demonstrate my ability on this subject using Selenium and Python. The website will be [Orange HRM](https://opensource-demo.orangehrmlive.com/).

# Coding philosophy and structure

I will be using OOP with Page Object Model. Therefore, folder structure will be as follows:
<br>
├── pages/<br>
└── tests/<br>
└──locators/<br>
└──utils/<br>
└──config/<br>

Pages will contain page classes matching the different pages of the website.
Tests will contain the scripts running the automated tests.
Locators will contain different id/xpath to use in pages.
Utils will contain reusable non-page logic.
Config will contain useful global constants.


# Run the code

1. pip install -r requirements.txt
2. set up a secrets.env for login and password
3. run the tests from project root folder with ```pytest tests/ --html=reports/report.html -v```




