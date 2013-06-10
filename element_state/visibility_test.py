import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import base_test

class VisibilityTest(base_test.WebDriverBaseTest):
    def test_0x0_pixel_element(self):
        self.driver.get(self.webserver.where_is("visibility/0x0-pixels.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertFalse(el.is_displayed())

    def test_1x1_pixel_element(self):
        self.driver.get(self.webserver.where_is("visibility/1x1-pixels.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())

    def test_display_block(self):
        self.driver.get(self.webserver.where_is("visibility/display-block.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())

    def test_display_none(self):
        self.driver.get(self.webserver.where_is("visibility/display-none.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertFalse(el.is_displayed())

    def test_visibility_hidden(self):
        self.driver.get(self.webserver.where_is("visibility/visibility-hidden.html"))
        el = self.driver_find_element_by_tag_name("p")
        self.assertFalse(el.is_displayed())

    def test_visibility_visible(self):
        self.driver.get(self.webserver.where_is("visibility/visibility-visible.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())

if __name__ == "__main__":
    unittest.main()
