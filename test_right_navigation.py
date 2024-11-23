import pytest
import unittest
import time
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import google.oauth2.credentials


# functional testing for  youtube right side bar navigation 

class   TestLeftSideNavigation:

    # pytest setup 
    def setup_method(self):
        self.video_id = None
        self.url = None
        self.driver = webdriver.Chrome()
        #yield
    
    # clean up the web after test
    def teardown(self):
        self.driver.quit()


    # web driver is set up 
    @pytest.fixture
    def setup_testing_content(self):
       self.url = "https://www.youtube.com"
       self.video_id = 'tjwzPIHPEdA'
       self.driver.get(self.url)
       self.waitTime = WebDriverWait(self.driver, 50)

    
    
    # testing the home icon
    @pytest.mark.skip(reason="TEST ALREADY PASSED") 
    def test_home_icon_button(self,setup_testing_content):
        # REQUST THE HOME PAGE 
        response = requests.get(self.url)
        # CHECK IF THE STSTUE IS TRUE 
        if response.status_code != 200:
            raise ValueError("url not working")
        
        home_icon_button = self.waitTime.until(EC.element_to_be_clickable((By.ID,'logo-icon')))
        home_icon_button.click()
        reloded = requests.get(self.driver.current_url)
        assert  reloded.status_code == 200,"page reloaded sucessfully"
        pass

    pytest.mark.skip(reason="TEST ALREADY PASSED")
    # test the interaction button on youtube the 3 lines 
    def test_hamburger_manue_icon(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("url not Valid")
        hamburger_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        hamburger_button.click()
        # make sure we are still on that page and the munue is avalable 
        samePage = requests.get(self.driver.current_url)
        assert samePage.status_code == 200 # made sure we are still on smae page 
        assert response.status_code == 200 # made sure that we the button is working 
        pass

    pytest.mark.skip(reason="TEST ALREADY PASSED")
    # testinf youtube short videos 
    def test_hamburgerHome(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("url not working")
        
        hamburger_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        hamburger_button.click()


        shorts_button = self.waitTime.until(EC.element_to_be_clickable((By.ID, "endpoint")))
        shorts_button.click()

        assert "youtube.com" in self.driver.current_url
        pass 
    

    def test_shorts(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("URL not working")

        hamburger_button = self.waitTime.until(
            EC.element_to_be_clickable((By.ID, "guide-button"))
        )
        hamburger_button.click()
      
        # shors  button 
        shorts_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Shorts']"))
        )
        assert shorts_button.is_displayed()
        assert shorts_button.is_enabled()

        shorts_button.click()
        self.waitTime.until(EC.url_contains("shorts"))
        assert "shorts" in self.driver.current_url
    
    
    def test_hamburger_subscription_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("URL not working")

        hamburger_subscription_button = self.waitTime.until(
            EC.element_to_be_clickable((By.ID, "guide-button"))
        )
        hamburger_subscription_button.click()
      
        # shors  button 
        subscription_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Subscriptions']"))
        )
        assert subscription_button.is_displayed()
        assert subscription_button.is_enabled()

        subscription_button.click()
        self.waitTime.until(EC.url_contains("feed/subscriptions"))
        assert "feed/subscriptions" in self.driver.current_url
    

    #  test the explor content inside the hamgurger button 

    def test_tranding_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("invalide url")

        hamburger_button = self.waitTime.until(
            EC.element_to_be_clickable((By.ID, "guide-button"))
        )
        hamburger_button.is_displayed()
        hamburger_button.is_enabled()
        hamburger_button.click()

        #  now find the trending button 
        trending_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH,  "//yt-formatted-string[text()='Trending']")))
        assert trending_button.is_displayed()
        assert trending_button.is_enabled()
        trending_button.click()

        self.waitTime.until(EC.url_contains('feed/trending'))
        assert "feed/trending" in self.driver.current_url

    def test_shopping_button(self, setup_testing_content):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ValueError("invalid url")
        # make sure that the 3 line are showing 
        side_menue = self.waitTime.until(EC.element_to_be_clickable((By.ID, "guide-button")))
        side_menue.is_displayed()
        side_menue.is_enabled()
        side_menue.click()

        shopping_button = self.waitTime.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Shopping']")))
        assert shopping_button.is_displayed()
        assert shopping_button.is_enabled()
        shopping_button.click()
        self.waitTime.until(EC.url_contains("channel"))
        assert "channel" in self.driver.current_url


            
        


        


def main():
    pytest.main()
if __name__ == "__main__":
    main()
        


       

    





