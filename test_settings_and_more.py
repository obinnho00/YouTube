import pytest
import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSettingsAndMore:

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
        self.waitTime = WebDriverWait(self.driver, 200)



        

    #@pytest.mark.skip()
    def test_youtube_premium(self, setup_testing_content):
        
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("invalid url")
        # locate the button 
        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        Youtube_premium_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='YouTube Premium']")))
        Youtube_premium_button.is_displayed()
        Youtube_premium_button.is_enabled()
        Youtube_premium_button.click()

        # verify the url 
        self.waitTime.until(EC.url_contains('premium'))
        assert 'premium' in self.driver.current_url

        
    #@pytest.mark.skip('passed')
    def test_youtube_premium(self, setup_testing_content):
        """
        YouTube Premium - Redirects to the YouTube Premium subscription page.
        """
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("invalid url")
        # locate the button 
        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        Youtube_premium_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='YouTube Premium']")))
        Youtube_premium_button.is_displayed()
        Youtube_premium_button.is_enabled()
        Youtube_premium_button.click()

        # verify the url 
        self.waitTime.until(EC.url_contains('premium'))
        assert 'premium' in self.driver.current_url

    
    
    #@pytest.mark.skip('passed')
    def test_youtube_tv(self, setup_testing_content):
        """
        YouTube TV - Redirects to YouTube's TV service.
        """
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("invalid url")
        
        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        youtube_tv_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='YouTube TV']")))
        youtube_tv_button.is_displayed()
        youtube_tv_button.is_enabled()
        youtube_tv_button.click()
        #print("current url", self.driver.current_url)

        #self.waitTime.until(EC.presence_of_element_located((By.XPATH, "//div[@id='tv-content']")))
        #assert 'tv.youtube' in self.driver.current_url

    
    
    #@pytest.mark.skip('passed')
    def test_youtube_music(self, setup_testing_content):
        """
        YouTube Music - Opens the music streaming section.
        """
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("Invalid URL")

        # Navigate to the side menu
        menu_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menu_page.click()

        # Locate and click the YouTube Music button
        youtube_music_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='YouTube Music']"))
        )
        assert youtube_music_button.is_displayed(), "YouTube Music button is not displayed"
        assert youtube_music_button.is_enabled(), "YouTube Music button is not enabled"
        youtube_music_button.click()

        # Check if the current URL contains "music"
        self.waitTime.until(EC.url_contains('music'))
        assert "music" in self.driver.current_url, "Navigation failed: 'music' not found in the current URL."
 

    
    
    #@pytest.mark.skip("passed")
    def test_youtube_kids(self, setup_testing_content):
        """
        YouTube Kids - Opens the child-friendly version of YouTube.
        """
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("invalid url")

        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        youtube_kids_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='YouTube Kids']")))
        youtube_kids_button.is_displayed()
        youtube_kids_button.is_enabled()
        youtube_kids_button.click()

        #self.waitTime.until(EC.url_contains('kids.com'))
        #assert 'kids' in self.driver.current_url

   
    
    #@pytest.mark.skip(reason='passed')
    def test_settings(self, setup_testing_content):
        """
        Settings - Access account and general platform settings.
        """
        # Verify the main page is accessible
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("Invalid URL")

        # Open the menu
        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        # Click the Settings button
        settings_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Settings']")))
        assert settings_button.is_displayed()
        assert settings_button.is_enabled()
        settings_button.click()

        # Wait for redirection to the Google account sign-in page
        self.waitTime.until(EC.url_contains('https://accounts.google.com/'))

        # Assert the URL contains key components
        assert 'https://accounts.google.com/' in self.driver.current_url, (
            f"Unexpected URL: {self.driver.current_url}"
        )

    

        

    #@pytest.mark.skip("passed but still nedded other verfiction")
    def test_send_feedback(self, setup_testing_content):
        """
        Send Feedback - Validate the feedback form popup and its elements.
        """
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("Invalid URL")

        # Navigate to the side menu
        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        # Locate and click the feedback button
        feedback_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Send feedback']"))
        )
        assert feedback_button.is_displayed(), "Feedback button is not displayed"
        assert feedback_button.is_enabled(), "Feedback button is not enabled"
        feedback_button.click()


        
        # Wait for the feedback popup container to appear
        #popup_container = self.waitTime.until(
        #EC.element_located_to_be_selected((By.XPATH, "//div[contains(@class, 'uvFeedbackFeedbackmanager-parent-container')]//div[contains(@class, 'uvFeedbackFeedbackmanagerview-container')]")))
        #assert popup_container.is_displayed(), "Feedback popup container is not displayed"
        """
        # Validate the title of the feedback form
        form_title = popup_container.find_element(By.CLASS_NAME, "uvFeedbackFormtitle")
        assert form_title.is_displayed(), "Feedback form title is not displayed"
        assert form_title.text == "Send feedback to YouTube", f"Unexpected form title: {form_title.text}"

        # Validate the feedback text area
        feedback_text_area = popup_container.find_element(By.CLASS_NAME, "scSharedMaterialtextfieldnative-control")
        assert feedback_text_area.is_displayed(), "Feedback text area is not displayed"

        # Locate and validate the legal text section
        legal_text = self.waitTime.until(
            EC.presence_of_element_located((By.CLASS_NAME, "uvFeedbackLegaltextroot"))
        )
        assert legal_text.is_displayed(), "Legal text is not displayed"
        assert "Some account and system information" in legal_text.text, "Legal text content is incorrect"

        # Locate the "Send" button and validate its state
        send_button = popup_container.find_element(By.XPATH, "//button[span[text()='Send']]")
        assert send_button.is_displayed(), "'Send' button is not displayed"
        assert not send_button.is_enabled(), "'Send' button should be disabled by default"

        print("Feedback form validations passed successfully.")
        """

    #@pytest.mark.skip("Passes")
    def test_help(self, setup_testing_content):
        """
        Help - Validate the Help Center popup and its title.
        """
        mainpage = requests.get(self.url)
        if mainpage.status_code != 200:
            raise ValueError("invalid url")

        menue_page = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        menue_page.click()

        help_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Help']")))
        assert help_button.is_displayed()
        assert help_button.is_enabled()
        help_button.click()

        # Wait for the help popup container to appear
        popup_container = self.waitTime.until(EC.visibility_of_element_located((By.ID, "help_panel_main_frame")))
        assert popup_container.is_displayed(), "help panel conatainer did not apear "
        assert popup_container.is_enabled()

       
        
        
        




def main():

    pytest.main(['test_settings_and_more.py', '-vv'])

if __name__ == '__main__':
    main()
