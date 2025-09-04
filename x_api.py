import tweepy

API_KEY = "4nKJOThSyR5n1hGk1Wqrim3y5"
API_SECRET_KEY = "9YfwYWdW77DW2VzxVdhOGzT74uFbtqQ2WGZPMSl1Erhp6GzlVa"
ACCESS_TOKEN = "1957421162859986944-0BV79n8MHKwAfNWby3n4uUZbjDuzXD"
ACCESS_TOKEN_SECRET = "03uYMTVD60PsHYQ2Udbh5rqxJ7zQEJf9zB87gs2SqSFSr"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALSM3gEAAAAAQ1E2M%2BAXntqcweg4OcjBgGWgXDs%3DHwz5Nz9pST8jlGs85ffOs4uZmWu85YyzrWtxUUkjmtqCLQabBi"

# Initialize the client
twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)

'''
# Get user ID from username
user_response = twitterClient.get_user(username='sundarpichai')
user_id = user_response.data.id
print(f"User ID: {user_id}")

# Get recent tweets
tweets_response = twitterClient.get_users_tweets(id=user_id, max_results=5)

# Print tweet texts
if tweets_response.data:
    for tweet in tweets_response.data:
        print(tweet.text)
else:
    print("No tweets found.")
'''