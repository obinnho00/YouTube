# libraries.py

# Standard libraries
import os
import sys
import unittest

# Third-party libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json 

class TestAPIEndpoints(unittest.TestCase):
    
    def setUp(self):
        
        # Initialize Chrome WebDriver for Selenium to interact with YouTube webpage
        self.driver = webdriver.Chrome()
        self.BASE_URL = "https://www.googleapis.com/youtube/v3"
        self.API_KEY = "AIzaSyApCrhYlW-vVuPuUrCgqhH9LNWAXrtgGr4"
        self.video_id = "gxQKjup3m4k"
        self.comment_id = "COMMENT_ID"

    def tearDown(self):
        self.driver.quit()


    def test_get_video_metadata(self):
        
        Respond = requests.get(f"{self.BASE_URL}/videos?part=snippet&id={self.video_id}&key={self.API_KEY}")
        Status_code = 200
        
        if Respond.status_code != Status_code:
            print("Error: Status code is not 200, check API key and request parameters.")
        self.assertEqual(Respond.status_code, Status_code, "API response status code is as expected.")

        json_data = Respond.json()
        self.driver.get(f"https://www.youtube.com/watch?v={self.video_id}")
        
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[property="og:title"]'))
        )

        description = self.driver.execute_script("return document.querySelector('meta[name=\"description\"]').getAttribute('content');")
        og_title = self.driver.execute_script("return document.querySelector('meta[property=\"og:title\"]').getAttribute('content');")
       
        api_description = "".join(json_data["items"][0]["snippet"]["description"].split()).lower()
        web_description = "".join(description.split()).lower()
        
        self.assertEqual(api_description, web_description, "Description matches the API data.")
        self.assertEqual(json_data["items"][0]["snippet"]["title"].strip().lower(), og_title.strip().lower(), "Title matches the API data.")
        
        if description and og_title:
            print("Description and title are present and validated successfully.")
        else:
            raise ValueError("Error: Title or description not found in metadata.")


    def test_get_comments(self):
        comment_respond = requests.get(
            f"{self.BASE_URL}/commentThreads",
            params={
                "part": "snippet",
                "videoId": self.video_id,
                "key": self.API_KEY,
                "maxResults": 1,
                "order": "relevance"
            }
        )

        self.Status_code = 200

        if comment_respond.status_code != self.Status_code:
            print("This webpage is not present or there is an error in the request.")
        
        self.assertEqual(comment_respond.status_code, self.Status_code)

        comment_data = comment_respond.json()
        self.assertIn("items", comment_data, "Expected 'items' key in the response data")
        self.assertGreater(len(comment_data["items"]), 0, "Expected at least one comment in the response")

        first_comment = comment_data["items"][0]
        self.assertIn("snippet", first_comment, "Expected 'snippet' in the first comment item")
        self.assertIn("topLevelComment", first_comment["snippet"], "Expected 'topLevelComment' in the snippet")

        comment_text = first_comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        self.assertIsInstance(comment_text, str, "Expected 'textDisplay' to be a string representing the comment text")
        

    def test_post_comment(self):
        status_code = 201
        # Sample comment text
        comment = "This is a test comment"
        self.ACCESS_TOKEN = "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"
        
        # Make the POST request to YouTube API to add a comment
        post_comment = requests.post(
            f"{self.BASE_URL}/commentThreads",
            headers={
                "Authorization": f"Bearer {self.ACCESS_TOKEN}",  # Replace with your OAuth token
                "Accept": "application/json"
            },
            json={
                "snippet": {
                    "videoId": self.video_id,  # Video ID to post the comment on
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": comment
                        }
                    }
                }
            }
        )
        
        # Check if the response status code is 201
        self.assertEqual(post_comment.status_code, status_code, "Comment was successfully posted.")
        
        # Parse the response JSON to verify the comment ID
        response_data = post_comment.json()
        self.assertIn("id", response_data["snippet"]["topLevelComment"], "Comment ID exists in the response.")
        
        print("Comment posted successfully:", response_data["snippet"]["topLevelComment"]["id"])


        

def main():
    """
    Main function to run the test suite.
    """
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()
