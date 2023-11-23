import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from locators.locators import My_Locators

class TC_1():

    def __init__(self, driver):
        self.driver = driver
        self.name_user_name = My_Locators.name_user_name
        self.name_user_password = My_Locators.name_user_password
        self.name_login_button = My_Locators.name_login_button

    def start(self):
        self.driver.get(My_Locators.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.NAME, My_Locators.name_user_name).send_keys("Luis")
        self.driver.find_element(By.NAME, My_Locators.name_user_password).send_keys("1234abcd")
        self.driver.find_element(By.NAME, My_Locators.name_login_button).click()
        print("login!")





