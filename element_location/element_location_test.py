# -*- mode: python; fill-column: 100; comment-column: 100; -*-

import unittest
import base_test

class ElementLocationTest(base_test.WebDriverBaseTest):

    def setUp(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))

    def test_find_element_by_id(self):
        e = self.driver.find_element_by_id("id")
        self.assertEquals("id", e.text)


    def test_find_element_by_name(self):
        e = self.driver.find_element_by_name("name")
        self.assertEquals("name", e.text)


    def test_find_element_by_css_selector(self):
        e = self.driver.find_element_by_css_selector("#id")
        self.assertEquals("id", e.text)


    def test_find_element_by_link_text(self):
        e = self.driver.find_element_by_link_text("link text")
        self.assertEquals("link text", e.text)


    def test_find_element_by_partial_link_text(self):
        e = self.driver.find_element_by_partial_link_text("link tex")
        self.assertEquals("link text", e.text)


    def test_find_element_by_xpath(self):
        e = self.driver.find_element_by_xpath("//*[@id='id']")
        self.assertEquals("id", e.text)

if __name__ == "__main__":
    unittest.main()
