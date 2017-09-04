from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NerVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
       self.browser.close()

    def test_can_start_a_list_and_retrieve_later(self):
        #someone go to the website
        self.browser.get('http://localhost:8000')
        #she find a 'To-Do' in title and web
        self.assertIn('To-Do',self.browser.title)
        header=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header)
        #she find a input with something and enter something when read it
        inputbox=self.browser.find_element_by_id('enter_list')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys("Buy french fries")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        #she find the web reopen and the thing she enter in website
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text=='1: Buy french fries' for row in rows),"msg not in table")

        self.fail("finish test")
#she find the input is empty and write something else.

#she find the two things after enter

#she find the web make her own url

#she go to the url and find everything is still.

#she exit the website

if __name__ == '__main__':
    unittest.main(warnings='ignore')