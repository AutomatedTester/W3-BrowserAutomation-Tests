# -*- mode: python; fill-column: 100; comment-column: 100; -*-

import unittest

import base_test

class ElementLocationTest(base_test.WebDriverBaseTest):

    ELEMENTS_PATH = "element_location/elements.html"

    def testFindElementById(self):
        self.driver.get(self.webserver.where_is(self.ELEMENTS_PATH))
        e = self.driver.find_element_by_id("id")
        self.assertEquals("id", e.text)


    def testFindElementByName(self):
        self.driver.get(self.webserver.where_is(self.ELEMENTS_PATH))
        e = self.driver.find_element_by_name("name")
        self.assertEquals("name", e.text)


    def testFindElementByCssSelector(self):
        self.driver.get(self.webserver.where_is(self.ELEMENTS_PATH))
        e = self.driver.find_element_by_css_selector("#id")
        self.assertEquals("id", e.text)


    def testFindElementByLinkText(self):
        self.driver.get(self.webserver.where_is(self.ELEMENTS_PATH))
        e = self.driver.find_element_by_link_text("link text")
        self.assertEquals("link text", e.text)


    def testFindElementByPartialLinkText(self):
        self.driver.get(self.webserver.where_is(self.ELEMENTS_PATH))
        e = self.driver.find_element_by_partial_link_text("link tex")
        self.assertEquals("link text", e.text)


    def testFindElementByXPath(self):
        self.driver.get(self.webserver.where_is(self.ELEMENTS_PATH))
        e = self.driver.find_element_by_xpath("//*[@id='id']")
        self.assertEquals("id", e.text)


if __name__ == '__main__':
    unittest.main()
