
import os
import sys
import requests
import json 
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from google.oauth2.credentials import Credentials
from config import TOKEN, API_KEY


class TestAPIEndpoints(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.BASE_URL = "https://www.googleapis.com/youtube/v3"
        self.API_KEY = API_KEY
        self.video_id = "gxQKjup3m4k"
        self.comment_id = "COMMENT_ID"
        self.ACCESS_TOKEN = TOKEN
        self.SCOPES = 'https://www.googleapis.com/auth/youtube.force-ssl'

    def tearDown(self):
        self.driver.quit()

    
    def test_get_video_metadata(self):

       
        response = requests.get(f"{self.BASE_URL}/videos?part=snippet&id={self.video_id}&key={self.API_KEY}")
        status_code = 200
        self.assertEqual(response.status_code, status_code)

        
        json_data = response.json()

        
        self.assertIn("items", json_data)
        self.assertGreater(len(json_data["items"]), 0)

        video_info = json_data["items"][0].get("snippet", {})
        self.assertIn("title", video_info)
        self.assertIn("description", video_info)
        

       
        self.assertIsInstance(video_info["title"], str)
        self.assertIsInstance(video_info["description"], str)

        if "tags" in video_info:
            self.assertIn("tags", video_info)
            self.assertIsInstance(video_info["tags"], list)
            self.assertGreater(len(video_info["tags"]), 0)
        else:
            pass 

        self.assertTrue(video_info["title"])
        self.assertTrue(video_info["description"])  

        

     
    def test_post_comment(self):
    
        Comment = "This is a test comment"
        
        post_comment = requests.post(
            f"{self.BASE_URL}/commentThreads?part=snippet",
            headers={
                "Authorization": f"Bearer {self.ACCESS_TOKEN}",
                "Accept": "application/json"
            },
            json={
                "snippet": {
                    "videoId": self.video_id,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": Comment
                        }
                    }
                }
            }
        )
       
        self.assertEqual(post_comment.status_code, 201)
        response_data = post_comment.json()

        comment_id = response_data["snippet"]["topLevelComment"]["id"]
        top_level_comment_snippet = response_data["snippet"]["topLevelComment"]["snippet"]
        author = response_data["snippet"]["topLevelComment"]["snippet"].get("authorDisplayName")
        timestamp = response_data["snippet"]["topLevelComment"]["snippet"].get("publishedAt")
        
        self.assertEqual(top_level_comment_snippet["textOriginal"], Comment)
        self.assertEqual(top_level_comment_snippet['id'], comment_id)
        self.assertIsNotNone(author)
        self.assertIsNotNone(timestamp)
        



    def test_get_comments(self):
       
        comment_respond = requests.get(
            f"{self.BASE_URL}/commentThreads",
            params={
                "part": "snippet",
                "videoId": self.video_id,
                "key": self.API_KEY,
                "maxResults":1,  
                "order": "relevance"
            }
        )
        
        self.Status_code = 200
        self.assertEqual(comment_respond.status_code, self.Status_code)
  
        comment_data = comment_respond.json()
        
        self.assertIn("items", comment_data)
        self.assertGreater(len(comment_data["items"]), 0)
        
        
        for comment in comment_data["items"]:
            
            self.assertIn("snippet", comment, "Expected 'snippet' in each comment item")
            self.assertIn("topLevelComment", comment["snippet"], "Expected 'topLevelComment' in the snippet")

            
            top_comment = comment["snippet"]["topLevelComment"]["snippet"]
            self.assertIn("authorDisplayName", top_comment, "Expected 'authorDisplayName' field for comment author")
            self.assertIn("textDisplay", top_comment, "Expected 'textDisplay' field for comment text")
            self.assertIn("publishedAt", top_comment, "Expected 'publishedAt' field for timestamp")

           
            self.assertIsInstance(top_comment["authorDisplayName"], str, "Expected author name to be a string")
            self.assertIsInstance(top_comment["textDisplay"], str, "Expected 'textDisplay' to be a string representing the comment text")
            self.assertIsInstance(top_comment["publishedAt"], str, "Expected 'publishedAt' to be a string representing timestamp")
            
            print("Comment:", top_comment["textDisplay"])
        
        if "nextPageToken" in comment_data:
            print("Pagination available with nextPageToken.")
        else:
            print("No additional pages of comments available.")

  

def main():
    """
    Main function to run the test suite.
    """
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()
