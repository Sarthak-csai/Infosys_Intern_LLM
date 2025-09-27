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
twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,                 # Used for app-only authentication
    consumer_key=API_KEY,                      # Required for user authentication
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True                    # Automatically waits if rate limit is hit
)

# Create and post a tweet with the specified text
response = twitterClient.create_tweet(text="Hello world from Tweepy!")

# Check if the tweet was successfully posted
if response.data:
    # If successful, print the Tweet ID
    print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
else:
    # If failed, print the error details
    print("Tweet failed:", response.errors)