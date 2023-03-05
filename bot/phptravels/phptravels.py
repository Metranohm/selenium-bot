from selenium import webdriver
import os 
import phptravels.constants as const  
from selenium.webdriver.common.by import By


class Phptravels(webdriver.Chrome):
    def __init__(self, driver_path=r"usr/bin/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Phptravels, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
      if self.teardown:
        self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(15)
    
    def check_nav_links(self):
        nav_links = self.find_elements(By.XPATH, const.NAV_LINKS)
        return nav_links
    



            