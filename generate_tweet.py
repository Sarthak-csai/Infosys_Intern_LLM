import json
import pandas as pd
from run_prompt import execute_gemini_for_tweet_creation

def get_top5(analysed_tweets, eng_type):
    df = pd.DataFrame(analysed_tweets)

    # Filter by engagement type
    filtered_df = df[df['engagement_type'] == eng_type]

    # Get top 5 by engagement_score
    top5_df = filtered_df.nlargest(n=5, columns=['engagement_score'])

    # Return as list of dicts
    return top5_df.to_dict(orient='records')

def create_tweet(analysed_tweets):
    engagement_type = "like"  # Example: could be 'like', 'retweet', 'reply', etc.
    top5_tweets = get_top5(analysed_tweets, engagement_type)

    if not top5_tweets:
        print(f"No tweets found for engagement type '{engagement_type}'.")
        return
    
    # prompt = "Write a tweet announcing the newly released iPhone 17 Pro Max and the upcoming iPhone 18 Pro, highlighting their physically moving camera zoom feature. Make the tweet appealing to a camera-enthusiast audience. mention Iphones too."
    prompt = """
        Write a tweet announcing the launch of Microsoft 365 Copilot, highlighting its AI-powered productivity features. Focus on how it transforms everyday workflows in Word, Excel, PowerPoint, and Teams by automating tasks, summarizing meetings, generating content, and analyzing data.

        Make the tweet appeal to tech-savvy professionals, developers, and productivity enthusiasts who crave smarter tools and seamless integration. Emphasize Copilot’s ability to save time, reduce cognitive load, and unlock creative potential.

        The tone should be futuristic, empowering, and crisp — something that makes users feel like they’re stepping into the next era of intelligent work.
"""
    system_prompt = """
        Create an engaging twitter tweet for Microsoft company
        PROMPT: {prompt}

        Here are some example tweets and their sentiment analysis with very high user engagement of other similar companies.
        Example Tweets:
        {top5_tweets}

        Create the tweet compare it with the example tweets and predict and explain why and how this tweet will perform well comparing to given examples.

        """
    
    out = execute_gemini_for_tweet_creation(
        prompt=system_prompt,
    )

    out_dict = json.loads(out)

    tweet = out_dict['tweet']
    prediction = out_dict['prediction']
    explanation = out_dict['explanation']

    print("Generated Tweet:", tweet)
    print("Prediction:", prediction)
    print("Explanation:", explanation)



    with open("generated_tweet.json", 'a') as file:
        json.dump(out_dict,file,indent=4)

    # Build a prompt or summary from top tweets
    # prompt = "Top 5 tweets by engagement:\n"
    # for i, tweet in enumerate(top5, 1):
    #     prompt += f"{i}. {tweet['text']} (Score: {tweet['engagement_score']})\n"

    # print(prompt)

if __name__ == '__main__':
    with open('analyzed_tweets.json') as file:
        data = json.load(file)
        # print("First tweet loaded:", data[0])
        create_tweet(data)