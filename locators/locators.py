from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time # Pausa en segundos
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class My_Locators():
    driver_path  = "/Users/luisfranciscocontrerasgonzalez/Documents/QAMinds/drivers/chromedriver"
    url = "https://demo.guru99.com/test/newtours/index.php"

    # Main Page

    name_user_name = "userName"
    name_user_password = "password"
    name_login_button = "submit"
    

