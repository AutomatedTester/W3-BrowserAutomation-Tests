import base_test
import unittest

class ExampleTest(base_test.WebDriverBaseTest):

    def testShouldNavigateAndReturnTitle(self):
        location = self.webserver.where_is('example.html')
        self.driver.get(location)
        self.assertEqual("Example", self.driver.title)

if __name__ == '__main__':
    unittest.main()
