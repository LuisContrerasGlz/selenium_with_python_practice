from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time # Pausa en segundos
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class My_Locators():
    driver_path  = "/Users/luisfranciscocontrerasgonzalez/Documents/selenium_with_python_practice/drivers/chromedriver"
    url = "https://demo.guru99.com/test/newtours/index.php"
    root_excel = "/Users/luisfranciscocontrerasgonzalez/Documents/selenium_with_python_practice/data/Test_Matrix.xlsx"

    # Main Page

    name_user_name = "userName"
    name_user_password = "password"
    name_login_button = "submit"
    xpath_login_message = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3"
    xpath_signoff_button = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a"


