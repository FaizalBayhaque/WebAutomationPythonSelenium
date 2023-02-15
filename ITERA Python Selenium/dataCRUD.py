import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def Create(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    driver.find_element(By.NAME,'Username').send_keys('ma')
    driver.find_element(By.NAME,'Password').send_keys('1')
    driver.find_element(By.NAME,'login').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    time.sleep(5)
    driver.find_element(By.ID,'Name').send_keys('ujang')
    time.sleep(5)
    driver.find_element(By.ID,'Company').send_keys('PT.Sukamakmur')
    time.sleep(5)
    driver.find_element(By.ID,'Address').send_keys('Jalan sukadari')
    time.sleep(5)
    driver.find_element(By.ID,'City').send_keys('Cihanjuang')
    time.sleep(5)
    driver.find_element(By.ID,'Phone').send_keys('081212324231')
    time.sleep(5)
    driver.find_element(By.ID,'Email').send_keys('sampleemail@testemail.com')

def Update(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    driver.find_element(By.NAME,'Username').send_keys('ma')
    driver.find_element(By.NAME,'Password').send_keys('1')
    driver.find_element(By.NAME,'login').click()
    time.sleep(2)
    driver.find_element(By.ID, 'searching').send_keys('Ujang')
    driver.find_element(By.XPATH, "//input[@value='Search']").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.btn-outline-primary').click()
    time.sleep(2)
    driver.find_element(By.ID, 'City').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    time.sleep(1)
    driver.find_element(By.ID, 'City').send_keys('Bandung')

def Delete(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    driver.find_element(By.NAME,'Username').send_keys('ma')
    driver.find_element(By.NAME,'Password').send_keys('1')
    driver.find_element(By.NAME,'login').click()
    time.sleep(2)
    driver.find_element(By.ID, 'searching').send_keys('Ujang')
    driver.find_element(By.XPATH, "//input[@value='Search']").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "body > div > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > a.btn.btn-outline-danger").click()
    driver.find_element(By.CSS_SELECTOR, "body > div > div > form > div > input").click()