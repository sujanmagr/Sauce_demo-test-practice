from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pom.page.login_page import loginpage
from pom.page.home_page import homepage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
def login(driver):
    login_page=loginpage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)
    #send username
    login_page.enter_username("standard_user")
    time.sleep(1)
    # send password
    login_page.enter_password("secret_sauce")
    time.sleep(1)

    login_page.click_login()
    time.sleep(4)

#parameter values for username and password
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visua_user", "secret_sauce"),#wrong user
])
#for login test
def test_login(driver, username, password):
    login_page=loginpage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)
    #send username
    login_page.enter_username(username)
    time.sleep(1)
    # send password
    login_page.enter_password(password)
    time.sleep(1)

    login_page.click_login()
    time.sleep(4)
    #to check login successful or not
    try:
        if "product" in driver.page_source:
            print("Login successful!")
            assert True 
        else:
            raise AssertionError("Login failed - 'product' not found in page source.")
    
    except Exception as e:
        print(f"Error! {str(e)}")
        assert False  

#test home page
def test_home(driver):
    #to login to the home page
    login(driver)
    home_page=homepage(driver)
    #menu click
    home_page.click_menu()
    time.sleep(1)
    #open cart
    home_page.click_cart()
    time.sleep(1)
    #click sort order
    home_page.click_sort()
    time.sleep(2)


