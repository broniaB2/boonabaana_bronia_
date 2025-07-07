import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def test_credentials():
    try:
        # Test OAuth2
        client = tweepy.Client(
            consumer_key=os.getenv('X_CONSUMER_KEY'),
            consumer_secret=os.getenv('X_CONSUMER_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_TOKEN_SECRET')
        )
        me = client.get_me()
        print(f"OAuth2 Success! User: @{me.data.username}")
        
        # Test OAuth1
        auth = tweepy.OAuth1UserHandler(
            os.getenv('X_CONSUMER_KEY'),
            os.getenv('X_CONSUMER_SECRET'),
            os.getenv('X_ACCESS_TOKEN'),
            os.getenv('X_ACCESS_TOKEN_SECRET')
        )
        api = tweepy.API(auth)
        print("OAuth1 Success! API:", api.verify_credentials().screen_name)
        return True
    except Exception as e:
        print(f"Auth Failed: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    if test_credentials():
        print("\n✅ Credentials work! Now try posting:")
        client = tweepy.Client(
            consumer_key=os.getenv('X_CONSUMER_KEY'),
            consumer_secret=os.getenv('X_CONSUMER_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_TOKEN_SECRET')
        )
        try:
            tweet = client.create_tweet(text="Test tweet - please ignore")
            print(f"Posted: https://twitter.com/user/status/{tweet.data['id']}")
        except Exception as e:
            print(f"Post failed: {e}")
    else:
        print("\n❌ Fix these issues:")
        print("1. Are all credentials in .env? (See above)")
        print("2. Are permissions 'Read + Write' in developer portal?")
        print("3. Did you REGENERATE tokens after changing permissions?")
        print("4. Wait 10 minutes after permission changes")