import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def Positive(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    driver.find_element(By.NAME,'Username').send_keys('ma')
    driver.find_element(By.NAME,'Password').send_keys('1')

def Negative(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    driver.find_element(By.NAME,'Username').send_keys('x')
    driver.find_element(By.NAME,'Password').send_keys('z')

def Logout(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    driver.find_element(By.NAME,'Username').send_keys('ma')
    driver.find_element(By.NAME,'Password').send_keys('1')
    time.sleep(3)
    driver.find_element(By.NAME,"login").click()

