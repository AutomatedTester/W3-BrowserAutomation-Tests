import unittest

import base_test
import unittest

class GetFromHttpTest(base_test.WebDriverBaseTest):

    # Boot strapping test. There is no assertion in this case, but this test
    # must pass before anything else will.
    def testGetUrlWithNoRedirectionOverHttp(self):
        page = self.webserver.where_is('navigation/empty.html')
        self.driver.get(page)

        url = self.driver.current_url
        self.assertEquals(page, url)
        

    def testGetWillFollowTheLocationHeader(self):
        page = self.webserver.where_is('navigation/redirect')
        self.driver.get(page)
        
        expected = self.webserver.where_is('navigation/empty.html')
        url = self.driver.current_url
        self.assertEquals(expected, url)
		
		
if __name__ == '__main__':
    unittest.main()
