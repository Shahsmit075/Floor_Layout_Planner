import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest5():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_test5(self):
        self.driver.get("http://127.0.0.1:5500/")
        self.driver.set_window_size(1552, 880)
        self.driver.find_element(By.CSS_SELECTOR, ".cta-button").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-new-file-button > span").click()
        self.driver.find_element(By.ID, "extension-floorplanner-modal-new-floorplan-name-input").click()
        self.driver.find_element(By.ID, "extension-floorplanner-modal-new-floorplan-name-input").send_keys("floor")
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.CSS_SELECTOR, ".extension-floorplanner-boxMouseOver:nth-child(2) > .extension-floorplanner-img-fluid").click()
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-text_mode > .extension-floorplanner-unicode-icon-large").click()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-text_mode > .extension-floorplanner-unicode-icon-large")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)  # Introduce a delay
        
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#extension-floorplanner-boxSurface > .extension-floorplanner-room").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-text-size-slider").send_keys("60")
        self.driver.find_element(By.ID, "extension-floorplanner-text-size-slider").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-labelBox").click()
        self.driver.find_element(By.ID, "extension-floorplanner-labelBox").send_keys("area")
        self.driver.find_element(By.CSS_SELECTOR, ".extension-floorplanner-textEditorColor:nth-child(9)").click()
        time.sleep(1)  # Introduce a delay
        
        self.driver.find_element(By.ID, "extension-floorplanner-save-text").click()
        self.driver.find_element(By.ID, "extension-floorplanner-delete-button").click()
        assert self.driver.switch_to.alert.text == "Are you sure you want to delete this floorplan?"
        self.driver.switch_to.alert.accept()
        self.driver.close()

# Instantiate the test class and run the test
test = TestTest5()
test.setup()
test.test_test5()
