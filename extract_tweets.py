from run_prompt import execute_gemini
from x_api import twitterClient
import json
from datetime import datetime

# Get user info
user = twitterClient.get_user(username='Microsoft')
user_id = user.data.id

tweets = twitterClient.get_users_tweets(
    id=user_id,
    max_results=50,
    tweet_fields=['created_at', 'public_metrics', 'text']
).data

tweet_dicts = [{
    "id": tweet.id,
    "text": tweet.text,
    "created_at": tweet.created_at.isoformat() if isinstance(tweet.created_at, datetime) else str(tweet.created_at),
    "public_metrics": tweet.public_metrics
} for tweet in tweets]

with open("extracted_tweets.json", 'w') as json_file:
    json.dump(tweet_dicts, json_file, indent=4)

#     prompt = f"""
# Tweet:
# \"\"\"{tweet.text}\"\"\"
# """

#     llm_out = execute_gemini(prompt=prompt)
#     print(llm_out)