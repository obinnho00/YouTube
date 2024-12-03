
import pytest
import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTopNavigationBar:

    # pytest setup
    def setup_method(self):
        self.video_id = None
        self.url = None
        self.driver = webdriver.Chrome()

    # Clean up the web after test
    def teardown(self):
        self.driver.quit()

    # pytest fixture for setup content
    @pytest.fixture
    def setup_testing_content(self):
        self.url = "https://www.youtube.com"
        self.video_id = 'tjwzPIHPEdA'
        self.driver.get(self.url)
        self.waitTime = WebDriverWait(self.driver, 160)





    #@pytest.mark.skip('passed')
    def test_search_bar(self, setup_testing_content):
        """
        Search Bar - Enter keywords to search for videos, playlists, or channels using XPath.
        """

        # Navigate to the page
        Home = requests.get(self.url)
        if Home.status_code != 200:
            raise ValueError("Error URL: Home page did not return status 200")
        
        expected_video_id = "aufs0Z57r58"
        search_video = "ecu campus tour welcome video"

        # Locate the search input field using XPath
        search_input = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='search']"))
        )
        assert search_input.is_displayed(), "Search input is not displayed"
        assert search_input.is_enabled(), "Search input is not enabled"

        # Click and send input
        search_input.click()
        search_input.send_keys(search_video)

        # Locate and click the search button
        search_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search-icon-legacy']"))
        )
        assert search_button.is_displayed(), "Search button is not displayed"
        assert search_button.is_enabled(), "Search button is not enabled"
        search_button.click()

        # Wait for search results to load
        video_element = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/watch?v={expected_video_id}')]"))
        )

        # Verify the video is displayed in the search results
        assert video_element.is_displayed(), f"Video with ID '{expected_video_id}' not found in search results"





    @pytest.mark.skip('url compersion fails')
    def test_submit_empty_search(self, setup_testing_content):
        """
        Test attempting to submit an empty search query.
        """

        Home = requests.get(self.url)
        if Home.status_code != 200:
            raise ValueError("Error URL: Home page did not return status 200")

        # Locate the search input field
        search_input = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='search']"))
        )
        assert search_input.is_displayed(), "Search input is not displayed"
        assert search_input.is_enabled(), "Search input is not enabled"

        # Ensure the input field is empty
        search_input.click()
        assert search_input.get_attribute("value") == "", "Search input is not empty"

        # Locate and click the search button
        search_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search-icon-legacy']"))
        )
        assert search_button.is_displayed(), "Search button is not displayed"
        assert search_button.is_enabled(), "Search button is not enabled"
        search_button.click()

        # Verify that the page does not navigate away (URL remains the same)
        current_url = self.driver.current_url
        assert current_url.rstrip('/') == self.url, "Page navigated away on empty search query"

        # Verify that no search results are loaded (default homepage content is visible)
        homepage_content = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='contents']"))
        )
        assert homepage_content.is_displayed(), "Default homepage content is not displayed"

    

    
    @pytest.mark.skip("tbt")
    def test_clear_empty_search(self, setup_testing_content):
        """
        Test attempting to clear an already empty search bar.
        """

        Home = requests.get(self.url)
        if Home.status_code != 200:
            raise ValueError("Error URL: Home page did not return status 200")
        

        # Locate the search input field
        search_input = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='search']"))
        )
        assert search_input.is_displayed(), "Search input is not displayed"
        assert search_input.is_enabled(), "Search input is not enabled"

        # Ensure the input field is empty
        assert search_input.get_attribute("value") == "", "Search input is not empty"

        # Locate the clear button
        clear_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Clear search query']"))
        )
        assert clear_button.is_displayed(), "Clear button is not displayed"
        assert clear_button.is_enabled(), "Clear button is not enabled"

        # Click the clear button
        clear_button.click()

        # Verify the input field remains empty
        assert search_input.get_attribute("value") == "", "Search input is not cleared"

    
    
    
    
    #@pytest.mark.skip('passed')
    def test_search_by_voice(self, setup_testing_content):
        """
        Test to verify the functionality of the 'Search by Voice' button.
        """

        # Navigate to the page
        Home = requests.get(self.url)
        if Home.status_code != 200:
            raise ValueError("Error URL: Home page did not return status 200")

        # Locate the 'Search by Voice' button
        voice_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='voice-search-button']"))
        )
        assert voice_button.is_displayed(), "Voice search button is not displayed"
        assert voice_button.is_enabled(), "Voice search button is not enabled"

        # Click the voice search button
        voice_button.click()

        """# Verify the response to clicking the button
        # (check if the 'Listening' UI or microphone icon appears)
        listening_ui = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listening-ui')]"))
        )
        assert listening_ui.is_displayed(), "Voice search 'Listening' UI did not appear"
        """




def main():
    pytest.main(['test_top_navigation_bar.py', '-vv'])


if __name__ == '__main__':
    main()
