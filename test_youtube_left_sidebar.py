import pytest
import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLeftSideNavigation:

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





    # Test the home icon button
    def test_home_icon(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("URL not working")
        
        home_icon_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, 'logo-icon')))
        assert home_icon_button.is_displayed(), "Home icon button not displayed"
        assert home_icon_button.is_enabled(), "Home icon button not enabled"
        home_icon_button.click()

        reloaded = requests.get(self.driver.current_url)
        assert reloaded.status_code == 200, "Page did not reload successfully"

    # Test the hamburger menu icon



    
    
    def test_menu_icon(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("URL not valid")
        
        hamburger_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert hamburger_button.is_displayed(), "Hamburger menu button not displayed"
        assert hamburger_button.is_enabled(), "Hamburger menu button not enabled"
        hamburger_button.click()

        same_page = requests.get(self.driver.current_url)
        assert same_page.status_code == 200, "Failed to stay on the same page"

    # Test YouTube Shorts button
    #@pytest.mark.skip()
    def test_shorts_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("URL not working")

        hamburger_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert hamburger_button.is_displayed(), "Hamburger button not displayed"
        assert hamburger_button.is_enabled(), "Hamburger button not enabled"
        hamburger_button.click()

        shorts_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Shorts']")))
        assert shorts_button.is_displayed(), "Shorts button not displayed"
        assert shorts_button.is_enabled(), "Shorts button not enabled"
        shorts_button.click()
        self.waitTime.until(EC.url_contains("shorts"))
        assert "shorts" in self.driver.current_url, "Shorts redirect failed"

    # Test subscription button
    #@pytest.mark.skip()
    def test_subscriptions_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("URL not working")

        hamburger_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert hamburger_button.is_displayed(), "Hamburger button not displayed"
        assert hamburger_button.is_enabled(), "Hamburger button not enabled"
        hamburger_button.click()

        subscription_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Subscriptions']")))
        assert subscription_button.is_displayed(), "Subscription button not displayed"
        assert subscription_button.is_enabled(), "Subscription button not enabled"
        subscription_button.click()

        self.waitTime.until(EC.url_contains('feed/subscriptions'))
        assert "feed/subscriptions" in self.driver.current_url, "Subscription redirection URL failed"

    # Test the Trending button
    #@pytest.mark.skip()
    def test_trending_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        hamburger_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert hamburger_button.is_displayed(), "Hamburger button not displayed"
        assert hamburger_button.is_enabled(), "Hamburger button not enabled"
        hamburger_button.click()

        trending_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Trending']")))
        assert trending_button.is_displayed(), "Trending button not displayed"
        assert trending_button.is_enabled(), "Trending button not enabled"
        trending_button.click()
        self.waitTime.until(EC.url_contains('feed/trending'))
        assert "feed/trending" in self.driver.current_url, "Trending redirect failed"

    # Test the Shopping button
    #@pytest.mark.skip()
    def test_shopping_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        side_menu = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert side_menu.is_displayed(), "Side menu not displayed"
        assert side_menu.is_enabled(), "Side menu not enabled"
        side_menu.click()

        shopping_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Shopping']")))
        assert shopping_button.is_displayed(), "Shopping button not displayed"
        assert shopping_button.is_enabled(), "Shopping button not enabled"
        shopping_button.click()
        self.waitTime.until(EC.url_contains("channel"))
        assert "channel" in self.driver.current_url, "Shopping redirect failed"

    # Test the Music button
    #@pytest.mark.skip()
    def test_music_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        music_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Music']")))
        assert music_button.is_displayed(), "Music button not displayed"
        assert music_button.is_enabled(), "Music button not enabled"
        music_button.click()
        self.waitTime.until(EC.url_contains('channel'))
        assert "channel" in self.driver.current_url, "Music redirect failed"

    # Test the Movies & TV button
    #@pytest.mark.skip()
    def test_movies_tv_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        movies_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Movies & TV']")))
        assert movies_button.is_displayed(), "Movies & TV button not displayed"
        assert movies_button.is_enabled(), "Movies & TV button not enabled"
        movies_button.click()
        self.waitTime.until(EC.url_contains('feed'))
        assert "feed" in self.driver.current_url, "Movies & TV redirect failed"

    # Test the Live button
    #@pytest.mark.skip()
    def test_live_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        live_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Live']")))
        assert live_button.is_displayed(), "Live button not displayed"
        assert live_button.is_enabled(), "Live button not enabled"
        live_button.click()
        self.waitTime.until(EC.url_contains('channel'))
        assert "channel" in self.driver.current_url, "Live redirect failed"

    # Test the Gaming button
    #@pytest.mark.skip()
    def test_gaming_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        gaming_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Gaming']")))
        assert gaming_button.is_displayed(), "Gaming button not displayed"
        assert gaming_button.is_enabled(), "Gaming button not enabled"
        gaming_button.click()
        self.waitTime.until(EC.url_contains('gaming'))
        assert "gaming" in self.driver.current_url, "Gaming redirect failed"

    # Test the News button
    #@pytest.mark.skip()
    def test_news_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        news_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='News']")))
        assert news_button.is_displayed(), "News button not displayed"
        assert news_button.is_enabled(), "News button not enabled"
        news_button.click()
        self.waitTime.until(EC.url_contains('channel'))
        assert "channel" in self.driver.current_url, "News redirect failed"

    # Test the Sports button
    #@pytest.mark.skip()
    def test_sports_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        sports_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Sports']")))
        assert sports_button.is_displayed(), "Sports button not displayed"
        assert sports_button.is_enabled(), "Sports button not enabled"
        sports_button.click()
        self.waitTime.until(EC.url_contains('channel'))
        assert "channel" in self.driver.current_url, "Sports redirect failed"

    # Test the Learning button
    #@pytest.mark.skip()
    def test_learning_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        learning_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Courses']")))
        assert learning_button.is_displayed(), "Learning button not displayed"
        assert learning_button.is_enabled(), "Learning button not enabled"
        learning_button.click()
        self.waitTime.until(EC.url_contains('feed/courses_destination'))
        assert "feed/courses_destination" in self.driver.current_url, "Learning redirect failed"

    # Test the Fashion & Beauty button
    #@pytest.mark.skip()
    def test_fashion_beauty_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        fashion_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Fashion & Beauty']")))
        assert fashion_button.is_displayed(), "Fashion & Beauty button not displayed"
        assert fashion_button.is_enabled(), "Fashion & Beauty button not enabled"
        fashion_button.click()
        self.waitTime.until(EC.url_contains('channel'))
        assert "channel" in self.driver.current_url, "Fashion & Beauty redirect failed"

    #@pytest.mark.skip()
    # Test the Podcasts button
    def test_podcast_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        podcast_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Podcasts']")))
        assert podcast_button.is_displayed(), "Podcasts button not displayed"
        assert podcast_button.is_enabled(), "Podcasts button not enabled"
        podcast_button.click()
        self.waitTime.until(EC.url_contains('podcasts'))
        assert "podcasts" in self.driver.current_url, "Podcasts redirect failed"

    #@pytest.mark.skip()
    # Test the Playables button
    def test_playables_button(self, setup_testing_content):
        
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("Invalid URL")

        menu_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        assert menu_button.is_displayed(), "Menu button not displayed"
        assert menu_button.is_enabled(), "Menu button not enabled"
        menu_button.click()

        playables_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Playables']")))
        assert playables_button.is_displayed(), "Playables button not displayed"
        assert playables_button.is_enabled(), "Playables button not enabled"
        playables_button.click()
        self.waitTime.until(EC.url_contains('playables'))
        assert "playables" in self.driver.current_url, "Playables redirect failed"

