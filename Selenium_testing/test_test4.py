import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestTest4():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_test4(self):
        self.driver.get("http://127.0.0.1:5500/")
        self.driver.set_window_size(1552, 880)
        self.driver.find_element(By.CSS_SELECTOR, ".cta-button").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "li > #extension-floorplanner-new-file-button").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-modal-new-floorplan-name-input").click()
        self.driver.find_element(By.ID, "extension-floorplanner-modal-new-floorplan-name-input").send_keys("hello2")
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".extension-floorplanner-boxMouseOver:nth-child(2) > .extension-floorplanner-img-fluid").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-partition_mode > .extension-floorplanner-unicode-icon-medium").click()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.ID, "extension-floorplanner-partition_mode")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxSurface > .extension-floorplanner-room")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxSurface > .extension-floorplanner-room")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxSurface > .extension-floorplanner-room")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-select_mode > img").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-object_mode > .extension-floorplanner-unicode-icon-large").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-text_mode > .extension-floorplanner-unicode-icon-large").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.close()

# Instantiate the test class and run the test
test = TestTest4()
test.setup()
test.test_test4()
