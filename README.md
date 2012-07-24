# W3C Browser Automation Specification Tests

In this repository you will find all of the 

## How to run the tests

1. It is highly recommended that you use a virtualenv. Install it via 
    `<sudo> easy_install virtualenv` or `<sudo> pip install virtualenv`
2. `virtualenv webdriver-tests`
3. `cd webdriver-tests`
4. `. bin/activate`
5. `cd ../`
6. `easy_install selenium` or `pip install selenium`
7. `python test_example.py`

## Updating Configuration

The `webdriver.cfg` file holds any configuration that the tests might require. Change the value of browser to your
needs. This will then be picked up by WebDriverBaseTest when tests are run.

## How to write tests
1. Create a test file per section
2. For each test there needs to be a corresponding HTML file that will be used for testing. HTML Files are not to be
   reused between tests.
3. Test name should explain the intention of the test e.g. `def testShouldNavigateAndReturnTitle(self):`
