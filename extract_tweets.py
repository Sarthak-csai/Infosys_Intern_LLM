from x_api import twitterClient  # Import the Twitter API client
import json                     # Import JSON module for saving data
from datetime import datetime   # Import datetime for timestamp formatting

# Step 1: Get user info for the Twitter handle 'Microsoft'
user = twitterClient.get_user(username='Microsoft')
user_id = user.data.id  # Extract the user ID from the response

# Step 2: Fetch up to 50 recent tweets from the user
tweets = twitterClient.get_users_tweets(
    id=user_id,
    max_results=50,
    tweet_fields=['created_at', 'public_metrics', 'text']  # Include timestamp, metrics, and text
).data

# Step 3: Format each tweet into a dictionary with selected fields
tweet_dicts = [{
    "id": tweet.id,
    "text": tweet.text,
    "created_at": tweet.created_at.isoformat() if isinstance(tweet.created_at, datetime) else str(tweet.created_at),
    "public_metrics": tweet.public_metrics
} for tweet in tweets]

# Step 4: Save the formatted tweet data to a JSON file
with open("extracted_tweets.json", 'w') as json_file:
    json.dump(tweet_dicts, json_file, indent=4)