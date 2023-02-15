import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Screenshot import Screenshot
from PIL import Image
import dataCRUD

class TestCreate(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_create_user(self):
        driver = self.driver
        dataCRUD.Create(driver)
        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
        driver.get_screenshot_as_file('create user.png')
    
    def test_update_user(self):
        driver = self.driver
        dataCRUD.Update(driver)
        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

    def test_delete_user(self):
        driver = self.driver
        dataCRUD.Delete(driver)
        
        
        

unittest.main()

    