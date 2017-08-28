from selenium import webdriver
import unittest

class NerVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    #def tearDown(self):
    #   self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        #someone go to the website
        self.browser.get('http://localhost:8000')
        #she find a 'To-Do' in title
        self.assertIn('To-Do',self.browser.title)
        #she enter something when read it
        self.fail('Finish to test!')
#she find the web reopen and the thing she enter in website

#she find the input is empty and write something else.

#she find the two things after enter

#she find the web make her own url

#she go to the url and find everything is still.

#she exit the website

if __name__ == '__main__':
    unittest.main(warnings='ignore')