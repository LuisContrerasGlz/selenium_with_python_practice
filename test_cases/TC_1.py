# Import necessary libraries and modules
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

# Importing locators from a separate file
from locators.locators import My_Locators

class TC_1():

    def __init__(self, driver):
        # Initialize the class with the Selenium WebDriver instance and locators
        self.driver = driver
        self.root_excel = pd.read_excel(My_Locators.root_excel, engine="openpyxl")
        self.name_user_name = My_Locators.name_user_name
        self.name_user_password = My_Locators.name_user_password
        self.name_login_button = My_Locators.name_login_button
        self.xpath_login_message = My_Locators.xpath_login_message
        self.xpath_signoff_button = My_Locators.xpath_signoff_button
        self.list_columns = My_Locators.list_columns

    def start(self):
        # Iterate through rows in the Excel sheet and execute test methods based on conditions
        # iloc[R][C] - Leer
        # loc[R, C] -Escribir
        global i
        for i in range(len(self.root_excel)):
            if self.root_excel.iloc[i]["Y/N"] == "Y":
                method_name = self.root_excel.iloc[i]["Nombre"]
                try:
                    # Get the reference to the test method dynamically
                    test_method = getattr(TC_1, method_name)
                except AttributeError:
                    print("ERROR!")
                
                # Execute the identified test method
                test_method(self)
            else:
                pass

    
    def Test_001(self):
        # Test method for a specific test case
        print("TC: ", self.root_excel.iloc[i]["ID Test"])

        # DataFrane
        # Initialize a DataFrame to store test results
        df = pd.DataFrame(columns=self.list_columns)
        int_current_row = 2

        # Open the website and perform login actions
        self.driver.get(My_Locators.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # Fill in login credentials
        self.driver.find_element(By.NAME, My_Locators.name_user_name).send_keys(self.root_excel.iloc[i]["Username"])
        self.driver.find_element(By.NAME, My_Locators.name_user_password).send_keys(str(self.root_excel.iloc[i]["Password"]))
        self.driver.find_element(By.NAME, My_Locators.name_login_button).click()

        # Wait for the login message to appear
        try:
            message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, self.xpath_login_message))
            )

            print("Message 2: ", str(message.text))

            # Store the login message in the DataFrame
            df.loc[int_current_row, "Message"] = message.text
        except TimeoutException as toe:
            print("Error: ", toe)

        # Perform actions after login
        print(self.xpath_login_message)
        self.driver.find_element(By.XPATH, self.xpath_signoff_button).click()
        self.driver.implicitly_wait(5)

        int_current_row += 1

        print("login!")

        # Print and save the DataFrame to an Excel file
        print(df)

        df.to_excel("/Users/luisfranciscocontrerasgonzalez/Documents/selenium_with_python_practice/evidence/catalog.xlsx")





