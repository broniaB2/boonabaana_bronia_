import tweepy
import random
from datetime import datetime, timedelta
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

print("Credential Check:")
print(f"Consumer Key: {'****'+os.getenv('X_CONSUMER_KEY')[-4:] if os.getenv('X_CONSUMER_KEY') else 'MISSING'}")
print(f"Consumer Secret: {'****'+os.getenv('X_CONSUMER_SECRET')[-4:] if os.getenv('X_CONSUMER_SECRET') else 'MISSING'}")
print(f"Access Token: {'****'+os.getenv('X_ACCESS_TOKEN')[-4:] if os.getenv('X_ACCESS_TOKEN') else 'MISSING'}")
print(f"Access Token Secret: {'****'+os.getenv('X_ACCESS_TOKEN_SECRET')[-4:] if os.getenv('X_ACCESS_TOKEN_SECRET') else 'MISSING'}")

class X_posting_agent:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
        Initialize with both OAuth1 (for media) and OAuth2 (for posting) clients
        """
        # OAuth2 Client (for most operations)
        self.client_v2 = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        # OAuth1 Handler (for media uploads)
        self.auth_v1 = tweepy.OAuth1UserHandler(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
        )
        self.api_v1 = tweepy.API(self.auth_v1)

    def post_text(self, content: str) -> bool: 
        """Post a text tweet using API v2"""
        try:
            response = self.client_v2.create_tweet(text=content)
            print(f"Successfully posted tweet: {response.data['id']}")
            return True
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return False
        
    def post_with_image(self, content: str, image_path: str) -> bool:
        """Post a tweet with an image using both APIs"""
        try:
            # Upload media using v1 API
            media = self.api_v1.media_upload(image_path)
            
            # Post tweet using v2 API
            response = self.client_v2.create_tweet(
                text=content,
                media_ids=[media.media_id]
            )
            print(f"Successfully posted tweet with image: {response.data['id']}")
            return True
        except Exception as e:
            print(f"Error posting tweet with image: {e}")
            return False

    def post_thread(self, messages: list) -> bool:
        """Post a thread of tweets"""
        previous_tweet_id = None
        success = True

        for message in messages:
            try:
                if previous_tweet_id:
                    response = self.client_v2.create_tweet(
                        text=message,
                        in_reply_to_tweet_id=previous_tweet_id
                    )
                else:
                    response = self.client_v2.create_tweet(text=message)

                previous_tweet_id = response.data['id']
                print(f"Posted thread tweet: {previous_tweet_id}")
            except Exception as e:
                print(f"Error posting thread tweet: {e}")
                success = False
                break
        
        return success
    
    def schedule_post(self, content: str, post_time: datetime) -> bool:
        """Placeholder for scheduled posts"""
        print(f"Post scheduled for {post_time}: {content}")
        return True

if __name__ == "__main__":
    # Load credentials from environment variables
    CONSUMER_KEY = os.getenv('X_CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('X_CONSUMER_SECRET')
    ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')
    
    if None in [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]:
        print("Error: Missing Twitter API credentials in environment variables")
        print("Please ensure your .env file contains:")
        print("X_CONSUMER_KEY, X_CONSUMER_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET")
    else:
        # Initialize the agent
        X_agent = X_posting_agent(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        # Example posts
        X_agent.post_text("Testing Twitter bot functionality! #Python #Automation")
        
        # Example thread
        thread = [
            "Thread part 1: Testing thread functionality...",
            "Thread part 2: This should appear as a reply...",
            "Thread part 3: Final part of the test thread!"
        ]
        X_agent.post_thread(thread)
        
        # Example scheduled post
        future_time = datetime.now() + timedelta(hours=1)
        X_agent.schedule_post("This would be a scheduled post", future_time)