import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators import
from locators.locators import My_Locators

# Test Cases import
from test_cases.TC_1 import TC_1


"""

It gets divided into 3 main phases:

1) setUpClass
2) test_name
3) tearDownClass
Bonus: MAIN

"""

class QAMinda(unittest.TestCase):
    
    @classmethod
    def  setUpClass(cls):
        print("Starting Test")
        mi_servicio = Service(My_Locators.driver_path)
        cls.driver = webdriver.Chrome(service=mi_servicio)
        cls.driver.implicitly_wait(5)


    def test_QAMinds(self):
        driver = self.driver
        tc_1 = TC_1(driver)
        tc_1.start()
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Finished test")

if __name__ == "__main__":
    unittest.main()