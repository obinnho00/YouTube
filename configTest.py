import pytest
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# pytest setup
def setup_method(self):
    self.video_id = None
    self.url = None
        
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-cache")  # Disable browser cache
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--incognito")      # Run in incognito mode to avoid residuals
        
    self.driver = webdriver.Chrome(options=chrome_options)

# Clean up the web after the test
def teardown(self):
    self.driver.quit()

# pytest fixture for setup content
@pytest.fixture(scope="function")
def setup_testing_content(self):
    self.url = "https://www.youtube.com"
    self.video_id = 'tjwzPIHPEdA'
    self.driver.get(self.url)
    self.waitTime = WebDriverWait(self.driver, 50)
    yield  # Allow the test to execute here