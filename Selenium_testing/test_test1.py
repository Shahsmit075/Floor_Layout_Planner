import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_test1(self):
        self.driver.get("http://127.0.0.1:5500/")
        self.driver.set_window_size(1552, 880)
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".cta-button").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "li > #extension-floorplanner-new-file-button").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-modal-new-floorplan-name-input").click()
        self.driver.find_element(By.ID, "extension-floorplanner-modal-new-floorplan-name-input").send_keys("hello1")
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".extension-floorplanner-boxMouseOver:nth-child(2) > .extension-floorplanner-img-fluid").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-line_mode > img").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-partition_mode > .extension-floorplanner-unicode-icon-medium").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-node_mode > .extension-floorplanner-unicode-icon-medium").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-room_mode > .extension-floorplanner-unicode-icon-large").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-object_mode > .extension-floorplanner-unicode-icon-large").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-delete-button").click()
        time.sleep(1)  # Introduce a delay
        
        assert self.driver.switch_to.alert.text == "Are you sure you want to delete this floorplan?"
        self.driver.switch_to.alert.accept()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-select_mode > img").click()
# Instantiate the test class and run the test
test = TestTest1()
test.setup_method(None)
test.test_test1()
