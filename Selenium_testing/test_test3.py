import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestTest3():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_test3(self):
        self.driver.get("http://127.0.0.1:5500/")
        self.driver.set_window_size(1552, 880)
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".cta-button").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-distance_mode").click()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, ".extension-floorplanner-tape-measure-icon")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxbind > path")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxbind > path")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxbind > path")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release()
        time.sleep(1) 

# Instantiate the test class and run the test
test = TestTest3()
test.setup()
test.test_test3()
