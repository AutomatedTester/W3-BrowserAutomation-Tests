import unittest

import base_test

class ElementLocationTest(base_test.WebDriverBaseTest):

    def testShouldFindElementById(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_id("myid")
        self.assertEquals("myidtext", e.text)


if __name__ == '__main__':
    unittest.main()
