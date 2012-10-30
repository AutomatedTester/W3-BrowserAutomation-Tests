import unittest

import base_test
import unittest

class GetFromHttpTest(base_test.WebDriverBaseTest):

    # Boot strapping test. There is no assertion in this case, but this test
    # must pass before anything else will.
    def testGetUrlWithNoRedirectionOverHttp(self):
        page = self.webserver.where_is('navigation/empty.html')
        self.driver.get(page)

        url = self.driver.current_url;
        self.assertEquals(page, url)
		
if __name__ == '__main__':
    unittest.main()
