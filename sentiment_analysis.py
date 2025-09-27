import json
import time
from run_prompt import execute_gemini  # Import Gemini execution function

# Step 1: Load extracted tweets from JSON file
with open("extracted_tweets.json") as extracted_tweets_file:
    extracted_tweets = json.load(extracted_tweets_file)

    analyzed_tweets = []  # Initialize list to store analyzed tweet results

    # Step 2: Iterate through each tweet and perform sentiment analysis
    for tweet in extracted_tweets:
        # Construct a prompt for Gemini model using tweet text and engagement metrics
        sentiment_analysis_prompt = f"""
            Tweet: {tweet["text"]}
            like_count: {tweet["public_metrics"]["like_count"]}
            retweet_count: {tweet["public_metrics"]["retweet_count"]}
            reply_count: {tweet["public_metrics"]["reply_count"]}
            impression_count: {tweet["public_metrics"]["impression_count"]}
            Read the tweet with regard to its public reception and provide keywords and sentiment analysis score
        """

        # Execute Gemini model with the prompt
        out = execute_gemini(sentiment_analysis_prompt)

        # Parse the model output into a dictionary
        out_dict = json.loads(out)

        # Add original tweet text to the analysis result
        out_dict["tweet"] = tweet["text"]

        # Append the enriched result to the analyzed_tweets list
        analyzed_tweets.append(out_dict)

        print("done")  # Log progress
        time.sleep(2)  # Pause to avoid overwhelming the model or API

    # Step 3: Save all analyzed tweets to a new JSON file
    with open("analyzed_tweets.json", "w") as analyzed_tweets_file:
        json.dump(analyzed_tweets, analyzed_tweets_file, indent=4)