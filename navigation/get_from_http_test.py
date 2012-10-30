import unittest
import sys
import os
 
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import base_test

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
        
        
    def testGetWillFollowMetaRefreshThatRefreshesInstantly(self):
        page = self.webserver.where_is('navigation/instant-meta-redirect.html')
        self.driver.get(page)
        
        expected = self.webserver.where_is('navigation/empty.html')
        url = self.driver.current_url
        self.assertEquals(expected, url)
		
		
    def testGetWillFollowMetaRefreshThatRefreshesAfterOneSecond(self):
        page = self.webserver.where_is('navigation/1s-meta-redirect.html')
        self.driver.get(page)

        expected = self.webserver.where_is('navigation/empty.html')
        url = self.driver.current_url
        self.assertEquals(expected, url)		


    def testGetWillNotFollowMetaRefreshThatRefreshesAfterMoreThanOneSecond(self):
        page = self.webserver.where_is('navigation/60s-meta-redirect.html')
        self.driver.get(page)

        url = self.driver.current_url
        self.assertEquals(page, url)		

				
if __name__ == '__main__':
    unittest.main()
