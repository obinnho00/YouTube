import pytest
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestVideoPlayerButtons:

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
        self.waitTime = WebDriverWait(self.driver, 130)
    



   
    #@pytest.mark.skip("pass")
    def test_play_pause(self, setup_testing_content):
        
        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("Page could not be loaded")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")

        # Wait for the video player to load
        video_player = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//video"))
        )
        assert video_player.is_displayed(), "Video player is not displayed"

        # Locate the play/pause button
        play_pause_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-play-button ytp-button']"))
        )
        assert play_pause_button.is_displayed(), "Play/Pause button is not displayed"
        assert play_pause_button.is_enabled(), "Play/Pause button is not enabled"

        # Get the video element
        video_element = self.driver.find_element(By.XPATH, "//video")

        # Check initial playback state
        is_paused = self.driver.execute_script("return arguments[0].paused;", video_element)
       

        # Click the button to toggle playback
        play_pause_button.click()
        time.sleep(2)  # Allow the state to update

        # Verify that the playback state has changed
        new_state = self.driver.execute_script("return arguments[0].paused;", video_element)
        assert new_state != is_paused, "Playback state did not toggle"
       

        # Click the button again to return to the original state
        play_pause_button.click()
        time.sleep(2)  

        # Verify that the playback state has returned to the original state
        final_state = self.driver.execute_script("return arguments[0].paused;", video_element)
        assert final_state == is_paused, "Playback state did not return to the original state"
        



    @pytest.mark.skip("pass")
    def test_progress_bar(self, setup_testing_content):
        
        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("Page could not be loaded")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")
        

        # Wait for the video player to load
        video_element = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//video"))
        )
        assert video_element.is_displayed(), "Video player is not displayed"

        # Get the initial video duration
        video_duration = self.driver.execute_script("return arguments[0].duration;", video_element)
        assert video_duration > 0, "Video duration is invalid"
       
        # Get the current playback position
        initial_position = self.driver.execute_script("return arguments[0].currentTime;", video_element)
        

        # Locate the progress bar
        progress_bar = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ytp-progress-bar-container')]"))
        )
        assert progress_bar.is_displayed(), "Progress bar is not displayed"

        # Move the playback position to the midpoint of the video
        midpoint_position = video_duration / 2
        self.driver.execute_script(f"arguments[0].currentTime = {midpoint_position};", video_element)
        time.sleep(2) 

        # Verify that the playback position has been updated
        updated_position = self.driver.execute_script("return arguments[0].currentTime;", video_element)
        assert round(updated_position) == round(midpoint_position), "Playback position did not update correctly"
       

        # Move the playback position to near the end of the video
        end_position = video_duration - 5 
        self.driver.execute_script(f"arguments[0].currentTime = {end_position};", video_element)
        time.sleep(2) 

        # Verify that the playback position has been updated
        final_position = self.driver.execute_script("return arguments[0].currentTime;", video_element)
        assert round(final_position) == round(end_position), "Playback position did not update correctly"
      




    @pytest.mark.skip("pass")
    def test_volume_control(self, setup_testing_content):
        
        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("Page could not be loaded")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")
        

        # Wait for the video player to load
        video_element = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//video"))
        )
        assert video_element.is_displayed(), "Video player is not displayed"

        # Locate the volume control button
        volume_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-mute-button')]"))
        )
        assert volume_button.is_displayed(), "Volume button is not displayed"
        assert volume_button.is_enabled(), "Volume button is not enabled"

        # Check initial volume state
        initial_volume = self.driver.execute_script("return arguments[0].volume;", video_element)
        is_muted = self.driver.execute_script("return arguments[0].muted;", video_element)
        
        # Mute the video
        volume_button.click()
        time.sleep(1)  # Allow the state to update

        # Verify that the video is muted
        muted_state = self.driver.execute_script("return arguments[0].muted;", video_element)
        assert muted_state, "The video is not muted after clicking the mute button"
       

        # Unmute the video
        volume_button.click()
        time.sleep(1)  

        # Verify that the video is unmuted
        unmuted_state = self.driver.execute_script("return arguments[0].muted;", video_element)
        assert not unmuted_state, "The video is still muted after clicking the unmute button"
        

        # Adjust the volume to 50%
        self.driver.execute_script("arguments[0].volume = 0.5;", video_element)
        time.sleep(1)  # Allow the state to update

        # Verify the volume is set to 50%
        updated_volume = self.driver.execute_script("return arguments[0].volume;", video_element)
        assert updated_volume == 0.5, f"Volume is not set to 50%, current volume: {updated_volume}"
        
  



    @pytest.mark.skip("passed")
    def test_theater_mode(self, setup_testing_content):
        
        # Load the video page using the initialized URL and video ID
        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("URL not working")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")
            

        video_player = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='movie_player']"))
        )
        assert video_player.is_displayed(), "Video player is not loaded"
        assert video_player.is_enabled(), "Video player is not enabled"

        theater_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Theater mode (t)']"))
        )
        assert theater_button.is_displayed(), "Theater mode button is not displayed"
        assert theater_button.is_enabled(), "Theater mode button is not enabled"

        theater_button.click()
        assert "ytp-large-width-mode" in video_player.get_attribute("class"), "Theater mode not activated"

        theater_button.click()
        assert "ytp-large-with-mode" not in video_player.get_attribute("class"), "Theater mode not deactivated"





    @pytest.mark.skip("passed")
    def test_fullscreen(self, setup_testing_content):
        
        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("URL not working")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")

        video_player = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='movie_player']"))
        )
        assert video_player.is_displayed(), "Video player is not loaded"
        assert video_player.is_enabled(), "Video player is not enabled"

        fullscreen_button = self.waitTime.until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'ytp-fullscreen-button')]"))
        )
        assert fullscreen_button.is_displayed(), "Fullscreen button is not displayed" 
        assert fullscreen_button.is_enabled(), "Fullscreen button is not enabled"

        # Enable fullscreen mode
        fullscreen_button.click()
        assert "ytp-fullscreen" in video_player.get_attribute("class"), "Fullscreen mode not activated"

        # Exit fullscreen mode
        fullscreen_button.click()
        assert "ytp-fullscreen" not in video_player.get_attribute("class"), "Fullscreen mode not deactivated"





    @pytest.mark.skip("pass")
    def test_mini_player(self, setup_testing_content):
        
        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("URL not working")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")

        video_player = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='movie_player']"))
        )
        assert video_player.is_displayed(), "Video player is not loaded"
        assert video_player.is_enabled(), "Video player is not enabled"

        mini_player_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Miniplayer (i)']"))
        )
        assert mini_player_button.is_displayed(), "Mini-player button is not displayed"
        assert mini_player_button.is_enabled(), "Mini-player button is not enabled"
        mini_player_button.click()





    @pytest.mark.skip("pass")
    def test_volume_mute_unmute(self, setup_testing_content):
       

        response = requests.get(f"{self.url}/watch?v={self.video_id}")
        if response.status_code != 200:
            raise ValueError("Page could not be loaded")

        self.driver.get(f"{self.url}/watch?v={self.video_id}")
        

        # Wait for the video player to load
        video_element = self.waitTime.until(
            EC.presence_of_element_located((By.XPATH, "//video"))
        )
        assert video_element.is_displayed(), "Video player is not displayed"

        # Locate the mute/unmute button
        volume_button = self.waitTime.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-mute-button')]"))
        )
        assert volume_button.is_displayed(), "Mute/Unmute button is not displayed"
        assert volume_button.is_enabled(), "Mute/Unmute button is not enabled"

        # Check initial mute state
        is_muted = self.driver.execute_script("return arguments[0].muted;", video_element)
        
        # Mute the video
        volume_button.click()
        time.sleep(1)  # Allow the state to update

        # Verify that the video is muted
        muted_state = self.driver.execute_script("return arguments[0].muted;", video_element)
        assert muted_state, "The video is not muted after clicking the mute button"
        
        # Unmute the video
        volume_button.click()
        time.sleep(1)  # Allow the state to update

        # Verify that the video is unmuted
        unmuted_state = self.driver.execute_script("return arguments[0].muted;", video_element)
        assert not unmuted_state, "The video is still muted after clicking the unmute button"
    


def main():
    pytest.main(['test_video_player.py', '-vv'])


if __name__ == '__main__':
    main()
