from selenium import webdriver
import os 
import booking.constants as const  
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"usr/bin/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
      if self.teardown:
        self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(15)
    
    def close_popup(self):
        popup = self.find_element(By.CSS_SELECTOR, 'button[class="b6dc9a9e69 e25355d3ee"]')
        popup.click()
    
    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()



            