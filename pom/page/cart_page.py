#to test cart page
from selenium.webdriver.common.by import By
import time
class cartpage:
    def __init__(self, driver):
        self.driver=driver
        self.cart=(By.XPATH,"//a[@class='shopping_cart_link']")
        self.add_cart=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        self.add_cart1=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
        self.remove_cart=(By.XPATH,"//button[@id='remove-sauce-labs-backpack']")
        self.checkout=(By.XPATH,"//button[@id='checkout']")
        self.fname_textbox=(By.XPATH,"//input[@id='first-name']")
        self.lname_textbox=(By.XPATH,"//input[@id='last-name']")
        self.zip_textbox=(By.XPATH,"//input[@id='postal-code']")
        self.continue_cart=(By.XPATH,"//input[@id='continue']")
        self.finish=(By.XPATH,"//button[@id='finish']")
        self.back_home=(By.XPATH,"//button[@id='back-to-products']")

    #to add cart click
    def click_add_cart(self):
        self.driver.find_element(*self.add_cart).click()
        time.sleep(1)
        self.driver.find_element(*self.add_cart1).click()
    #remove from cart
    def click_remove_cart(self):
        self.driver.find_element(*self.remove_cart).click()
    
    def click_cart(self):
        self.driver.find_element(*self.cart).click()
        #checkout
    def click_checkout(self):
        self.driver.find_element(*self.checkout).click()
    #enter checkout detail
    def enter_detail(self, fname, lname, zip):
        self.driver.find_element(*self.fname_textbox).send_keys(fname)
        time.sleep(1)
        self.driver.find_element(*self.lname_textbox).send_keys(lname)
        time.sleep(1)
        self.driver.find_element(*self.zip_textbox).send_keys(zip)
    
    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0,50);")
        
    def click_continue(self):
        self.driver.find_element(*self.continue_cart).click()

    def click_finish(self):
        self.driver.find_element(*self.finish).click()

    def click_home(self):
        self.driver.find_element(*self.back_home).click()
    

    

    

    





