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
        self.root_excel = pd.read_excel(My_Locators.root_excel, engine="openpyxl")
        self.name_user_name = My_Locators.name_user_name
        self.name_user_password = My_Locators.name_user_password
        self.name_login_button = My_Locators.name_login_button

    def start(self):
        # iloc[R][C] - Leer
        # loc[R, C] -Escribir
        global i
        for i in range(len(self.root_excel)):
            if self.root_excel.iloc[i]["Y/N"] == "Y":
                method_name = self.root_excel.iloc[i]["Nombre"]
                try:
                    test_method = getattr(TC_1, method_name)
                except AttributeError:
                    print("ERROR!")
                
                test_method(self)
            else:
                pass

    
    def Test_001(self):
        self.driver.get(My_Locators.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.NAME, My_Locators.name_user_name).send_keys(self.root_excel.iloc[i]["Username"])
        self.driver.find_element(By.NAME, My_Locators.name_user_password).send_keys(self.root_excel.iloc[i]["Password"])
        self.driver.find_element(By.NAME, My_Locators.name_login_button).click()
        print("login!")





