import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import dataLogindanLogout


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Positive(self):
        driver = self.driver
        dataLogindanLogout.Positive(driver)
        driver.find_element(By.NAME,'login').click()

        response_message = driver.find_element(By.CSS_SELECTOR,'h3')
        print( response_message.get_attribute('innerHTML'))

    def test_Login_Negative(self):
        driver = self.driver
        dataLogindanLogout.Negative(driver)
        driver.find_element(By.NAME,'login').click()

        response_message = driver.find_element(By.CLASS_NAME,'alert-danger').text
        self.assertEqual(response_message, 'Wrong username or password')

    def test_Logout(self):
        driver = self.driver
        dataLogindanLogout.Logout(driver)
        driver.find_element(By.LINK_TEXT,"Log out").click()

        response_message = driver.find_element(By.XPATH,'//table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
        print(response_message)
        

       


unittest.main()

