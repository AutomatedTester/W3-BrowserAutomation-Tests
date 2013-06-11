import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import base_test

class NaturalNonVisibleElementsTest(base_test.WebDriverBaseTest):
    def test_0x0_pixel_element_is_not_visible(self):
        self.driver.get(self.webserver.where_is("element_state/0x0-pixels.html"))
        el = self.driver.find_element_by_tag_name("div")
        self.assertFalse(el.is_displayed())

    def test_0x0_pixel_text_node_is_visible(self):
        self.driver.get(self.webserver.where_is("element_state/0x0-pixels-text-node.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())

    def test_1x1_pixel_element(self):
        self.driver.get(self.webserver.where_is("element_state/1x1-pixels.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())

class DisplayTest(base_test.WebDriverBaseTest):
    def test_display_block(self):
        self.driver.get(self.webserver.where_is("element_state/display-block.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())

    def test_display_none(self):
        self.driver.get(self.webserver.where_is("element_state/display-none.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertFalse(el.is_displayed())

    def test_display_none_hides_child_node(self):
        self.driver.get(self.webserver.where_is("element_state/display-none-child.html"))
        parent = self.driver.find_element_by_id("parent")
        child = self.driver.find_element_by_id("child")

        self.assertFalse(parent.is_displayed())
        self.asserrFalse(child.is_displayed())

    def test_display_none_hides_child_node_link(self):
        pass

    def test_display_none_hides_child_node_paragraph(self):
        pass

    def test_display_none_on_parent_takes_presedence(self):
        pass

    def test_display_none_on_parent_takes_presedence_over_visibility_visible(self):
        pass
    
class VisibilityTest(base_test.WebDriverBaseTest):
    def test_element_state_hidden(self):
        self.driver.get(self.webserver.where_is("element_state/visibility-hidden.html"))
        el = self.driver_find_element_by_tag_name("p")
        self.assertFalse(el.is_displayed())

    def test_element_state_visible(self):
        self.driver.get(self.webserver.where_is("element_state/visibility-visible.html"))
        el = self.driver.find_element_by_tag_name("p")
        self.assertTrue(el.is_displayed())
    
    def test_visibility_hidden_hides_child_node(self):
        self.driver.get(self.webserver.where_is("element_state/visibility-child.html"))
        parent = self.driver_find_element_by_id("parent")
        child = self.driver.find_element_by_id("child")

        self.assertFalse(parent.is_displayed())
        self.assertFalse(child.is_displayed())

    def test_visibility_hidden_hides_child_node_link(self):
        self.driver.get(self.webserver.where_is("element_state/visibility-child-link.html"))
        parent = self.driver_find_element_by_id("parent")
        child = self.driver.find_element_by_id("child")

        self.assertFalse(parent.is_displayed())
        self.assertFalse(child.is_displayed())

    def test_visibility_hidden_hides_child_node_paragraph(self):
        self.driver.get(self.webserver.where_is("element_state/visibility-child-paragraph.html"))
        parent = self.driver_find_element_by_id("parent")
        child = self.driver.find_element_by_id("child")

        self.assertFalse(parent.is_displayed())
        self.assertFalse(child.is_displayed())

    def test_visibility_hidden_on_parent_takes_presedence(self):
        pass

    def test_visibility_hidden_on_parent_takes_presedence_over_display_block(self):
        pass

if __name__ == "__main__":
    unittest.main()
