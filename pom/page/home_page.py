#test home page functionality and ui
from selenium.webdriver.common.by import By
import time

class homepage:
    def __init__(self, driver):
        self.driver=driver
        self.menu=(By.XPATH,"//button[@id='react-burger-menu-btn']")
        self.sort=(By.XPATH,"//select[@class='product_sort_container']")
        self.cart=(By.XPATH,"//a[@class='shopping_cart_link']")
        self.sort_option=(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[2]")
        self.back_home=(By.XPATH,"//button[@id='continue-shopping']")

    def click_menu(self):
        self.driver.find_element(*self.menu).click()
    
    def click_cart(self):
        self.driver.find_element(*self.cart).click()
        time.sleep(2)
        self.driver.find_element(*self.back_home).click()
    
    def click_sort(self):
    # Step 1: Click the sort button
        self.driver.find_element(*self.sort).click()
        time.sleep(2)
        self.driver.find_element(*self.sort_option).click()


        