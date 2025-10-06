# Import the Tweepy library for accessing the Twitter API
import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access credentials from environment
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


# Initialize the Tweepy client using OAuth 1.0a credentials and bearer token
# twitterClient = tweepy.Client(
#     bearer_token=BEARER_TOKEN,                 # Used for app-only authentication
#     consumer_key=API_KEY,                      # Required for user authentication
#     consumer_secret=API_SECRET_KEY,
#     access_token=ACCESS_TOKEN,
#     access_token_secret=ACCESS_TOKEN_SECRET,
#     wait_on_rate_limit=True                    # Automatically waits if rate limit is hit
# )

# Authenticate using OAuth 1.0a
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define your tweet
tweet_text = "Hello world! This is a tweet from Tweepy using OAuth 1.0a 🎯"

try:
    # Post the tweet
    response = api.update_status(status=tweet_text)
    print("✅ Tweet posted successfully!")
    print("🆔 Tweet ID:", response.id)
    print("📝 Tweet Text:", response.text)
except tweepy.TweepyException as e:
    print("❌ Failed to post tweet:", e)
