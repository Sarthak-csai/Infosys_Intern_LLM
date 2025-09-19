import json
import pandas as pd
from run_prompt import execute_gemini_for_tweet_creation,execute_gemini_for_tweets_comparison
from run_gpt import execute_gpt_for_tweet_creation

def get_top5(analysed_tweets, eng_type):
    df = pd.DataFrame(analysed_tweets)

    # Filter by engagement type
    filtered_df = df[df['engagement_type'] == eng_type]

    # Get top 5 by engagement_score
    top5_df = filtered_df.nlargest(n=5, columns=['engagement_score'])

    # Return as list of dicts
    return top5_df.to_dict(orient='records')

def create_tweet(prompt):

    with open('analyzed_tweets.json') as file:
        analysed_tweets = json.load(file)

    engagement_type = "like"  # Example: could be 'like', 'retweet', 'reply', etc.
    top5_tweets = get_top5(analysed_tweets, engagement_type)

    if not top5_tweets or prompt=='':
        print(f"No tweets found for engagement type '{engagement_type}'.")
        return None
    
    if prompt=='':
        prompt = """
            Write a tweet announcing the launch of Microsoft 365 Copilot, highlighting its AI-powered productivity features. Focus on how it transforms everyday workflows in Word, Excel, PowerPoint, and Teams by automating tasks, summarizing meetings, generating content, and analyzing data.

            Make the tweet appeal to tech-savvy professionals, developers, and productivity enthusiasts who crave smarter tools and seamless integration. Emphasize Copilot’s ability to save time, reduce cognitive load, and unlock creative potential.

            The tone should be futuristic, empowering, and crisp — something that makes users feel like they’re stepping into the next era of intelligent work.
            """
    system_prompt = """
        Create an engaging twitter tweet for Microsoft company.
        PROMPT: {prompt}

        Here are some example tweets and their sentiment analysis with very high user engagement of other similar companies.
        Example Tweets:
        {top5_tweets}

        Create the tweet compare it with the example tweets and predict and explain why and how this tweet will perform well comparing to given examples.

        """
    
    out = execute_gemini_for_tweet_creation(prompt=system_prompt)

    # out = compare_tweets_from_two_models(prompt=system_prompt)

    tweet = out['tweet']
    prediction = out['prediction']
    explanation = out['explanation']

    print("Generated Tweet:", tweet)
    print("Prediction:", prediction)
    print("Explanation:", explanation)



    with open("generated_tweet.json", 'a') as file:
        json.dump(out,file,indent=4)

    return out

def compare_tweets(analysed_tweets):
    engagement_type = "like"  # Can be changed to 'retweet', 'reply', etc.
    top5_tweets = get_top5(analysed_tweets, engagement_type)

    if not top5_tweets:
        print(f"No tweets found for engagement type '{engagement_type}'.")
        return

    prompt = """
        Write two distinct tweets announcing the launch of Microsoft 365 Copilot, highlighting its AI-powered productivity features.
        Focus on how it transforms workflows in Word, Excel, PowerPoint, and Teams by automating tasks, summarizing meetings, generating content, and analyzing data.

        Make both tweets appeal to tech-savvy professionals, developers, and productivity enthusiasts.
        Emphasize Copilot’s ability to save time, reduce cognitive load, and unlock creative potential.

        The tone should be futuristic, empowering, and crisp — something that makes users feel like they’re stepping into the next era of intelligent work.
    """

    system_prompt = f"""
        Create two engaging tweets for Microsoft company.
        PROMPT: {prompt}

        Here are some example tweets and their sentiment analysis with very high user engagement from similar companies:
        Example Tweets:
        {top5_tweets}

        Compare the two generated tweets with each other and with the examples.
    """

    out = execute_gemini_for_tweets_comparison(prompt=system_prompt)

    tweet_a = out['tweet_a']
    tweet_b = out['tweet_b']
    tweet_comparison = out['tweet_a_vs_tweet_b']
    prediction = out['prediction']
    explanation = out['explanation']

    print("Tweet A:", tweet_a)
    print("Tweet B:", tweet_b)
    print("Tweet A vs Tweet B:", tweet_comparison)
    print("Prediction:", prediction)
    print("Explanation:", explanation)

    with open("tweet_comparison.json", 'a') as file:
        json.dump(out, file, indent=4)

def gemini_gpt_tweets_creation(analysed_tweets):
    engagement_type = "like"  # Could be 'retweet', 'reply', etc.
    top5_tweets = get_top5(analysed_tweets, engagement_type)

    if not top5_tweets:
        print(f"No tweets found for engagement type '{engagement_type}'.")
        return

    prompt = """
        Write a tweet announcing the launch of Microsoft 365 Copilot, highlighting its AI-powered productivity features. Focus on how it transforms everyday workflows in Word, Excel, PowerPoint, and Teams by automating tasks, summarizing meetings, generating content, and analyzing data.

        Make the tweet appeal to tech-savvy professionals, developers, and productivity enthusiasts who crave smarter tools and seamless integration. Emphasize Copilot’s ability to save time, reduce cognitive load, and unlock creative potential.

        The tone should be futuristic, empowering, and crisp — something that makes users feel like they’re stepping into the next era of intelligent work.
    """

    system_prompt = f"""
        Create an engaging twitter tweet for Microsoft company.
        PROMPT: {prompt}

        Here are some example tweets and their sentiment analysis with very high user engagement of other similar companies.
        Example Tweets:
        {top5_tweets}

        Create the tweet, compare it with the example tweets, and predict and explain why and how this tweet will perform well compared to the given examples.
    """

    # Generate from Gemini and OpenAI
    gemini_output = execute_gemini_for_tweet_creation(prompt=system_prompt)
    openai_output = execute_gpt_for_tweet_creation(prompt=system_prompt)

    try:
        openai_dict = json.loads(openai_output)
    except json.JSONDecodeError:
        openai_dict = {
            "tweet": None,
            "prediction": "unknown",
            "explanation": "Failed to parse OpenAI response."
        }

    # Print comparison
    print("\n🔵 Gemini Tweet:")
    print("Tweet:", gemini_output["tweet"])
    print("Prediction:", gemini_output["prediction"])
    print("Explanation:", gemini_output["explanation"])

    print("\n🟣 OpenAI Tweet:")
    print("Tweet:", openai_dict["tweet"])
    print("Prediction:", openai_dict["prediction"])
    print("Explanation:", openai_dict["explanation"])

    # Save to file
    with open("generated_tweet.json", 'a') as file:
        json.dump({
            "gemini": gemini_output,
            "openai": openai_dict
        }, file, indent=4)

def create_compare_tweets_with_gemini_models(prompt):
    """
    Generate and compare tweets from two different Gemini models using top-performing tweet examples.

    Parameters:
    - analysed_tweets (list): List of tweet dicts with engagement metrics.
    - output_path (str): File path to append comparison results.
    """

    with open('analyzed_tweets.json') as file:
        analysed_tweets = json.load(file)

    engagement_type = "like"
    top5_tweets = get_top5(analysed_tweets, engagement_type)

    if not top5_tweets:
        print(f"No tweets found for engagement type '{engagement_type}'.")
        return

    if prompt=='':
        prompt = """
            Write a tweet announcing the launch of Microsoft 365 Copilot, highlighting its AI-powered productivity features. Focus on how it transforms everyday workflows in Word, Excel, PowerPoint, and Teams by automating tasks, summarizing meetings, generating content, and analyzing data.

            Make the tweet appeal to tech-savvy professionals, developers, and productivity enthusiasts who crave smarter tools and seamless integration. Emphasize Copilot’s ability to save time, reduce cognitive load, and unlock creative potential.

            The tone should be futuristic, empowering, and crisp — something that makes users feel like they’re stepping into the next era of intelligent work.
            """

    system_prompt = f"""
        Create an engaging twitter tweet for Microsoft company.
        PROMPT: {prompt}

        Here are some example tweets and their sentiment analysis with very high user engagement of other similar companies.
        Example Tweets:
        {top5_tweets}

        Create the tweet, compare it with the example tweets, and predict and explain why and how this tweet will perform well compared to the given examples.
    """

    model_a = "gemini-2.0-flash"
    model_b = "gemini-2.5-flash-lite"

    # Generate tweets from two Gemini models
    output_a = execute_gemini_for_tweet_creation(prompt=system_prompt, model_name=model_a)
    output_b = execute_gemini_for_tweet_creation(prompt=system_prompt, model_name=model_b)

    tweet_a = output_a.get("tweet", None)
    prediction_a = output_a.get("prediction", "unknown")
    explanation_a = output_a.get("explanation", "Failed to parse response.")

    tweet_b = output_b.get("tweet", None)
    prediction_b = output_b.get("prediction", "unknown")
    explanation_b = output_b.get("explanation", "Failed to parse response.")

    # Compare tweets using another Gemini model
    comparison_prompt = f"""
    You are an expert in social media engagement analysis.

    Compare the following two tweets announcing Microsoft 365 Copilot. Evaluate them based on clarity, emotional appeal, relevance to target audience (tech-savvy professionals), and likelihood of high engagement.

    Tweet A:
    "{tweet_a}"

    Tweet B:
    "{tweet_b}"

    Provide:
    - tweet_a_vs_tweet_b: Comparative analysis highlighting strengths and weaknesses of each tweet.
    - prediction: Which tweet will perform better and why.
    - explanation: Reasoning referencing tone, structure, and audience alignment.
    """

    model_comp = "gemini-2.5-flash"
    output = execute_gemini_for_tweets_comparison(prompt=comparison_prompt,model_name=model_comp)
    
    tweet_comparison = output.get("tweet_a_vs_tweet_b", "Comparison not available.")
    prediction = output.get("prediction", "unknown")
    explanation = output.get("explanation", "Failed to parse explanation.")

    # Print comparison results
    print("\n🔵 Gemini Model A Tweet:")
    print("Tweet:", tweet_a)
    print("Prediction:", prediction_a)
    print("Explanation:", explanation_a)

    print("\n🟣 Gemini Model B Tweet:")
    print("Tweet:", tweet_b)
    print("Prediction:", prediction_b)
    print("Explanation:", explanation_b)

    print("\n🧠 Comparative Analysis:")
    print("Comparison:", tweet_comparison)
    print("Predicted Winner:", prediction)
    print("Explanation:", explanation)

    # Save comparison results
    with open("compared_tweets.json", 'a') as file:
        json.dump({
            "model_a": {
                "name": model_a,
                "tweet": tweet_a,
                "prediction": prediction_a,
                "explanation": explanation_a
            },
            "model_b": {
                "name": model_b,
                "tweet": tweet_b,
                "prediction": prediction_b,
                "explanation": explanation_b
            },
            "comparison": {
                "name": model_comp,
                "tweet_a_vs_tweet_b": tweet_comparison,
                "prediction": prediction,
                "explanation": explanation
            }
        }, file, indent=4)

    return output
'''
if __name__ == '__main__':
    with open('analyzed_tweets.json') as file:
        data = json.load(file)
        # print("First tweet loaded:", data[0])
        # create_tweet(data)
        # compare_tweets(data)
        # create_and_compare_tweets(data)
        create_compare_tweets_with_gemini_models(data)
'''