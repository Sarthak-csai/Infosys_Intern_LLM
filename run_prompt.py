import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def execute_gemini(prompt):
    """
    Executes a Gemini model call with a structured prompt and returns
    a schema-compliant JSON string.
    Parameters:
        prompt (str): The input prompt.
    Returns:
        dict: The parsed JSON response from the Gemini model.
    """
    # Configure Gemini API
    genai.configure(api_key=GEMINI_API_KEY)

    # Name of the available model (check with genai.list_models() if unsure)
    model = genai.GenerativeModel("gemini-2.5-flash-lite")  # Or "gemini-1.5-flash" if available

    # -- Prompt Engineering: Instruct the model to return the desired JSON format --
    schema = (
        "Respond in valid JSON only, with the following fields:\n"
        "  sentiment_type (one of: angry, sad, fearful, sarcastic, motivational, positive, negative, excited, neutral),\n"
        "  engagement_type (like, reply, impression, retweet),\n"
        "  sentiment_score (number),\n"
        "  topic (string),\n"
        "  reason_for_engagement (string),\n"
        "  engagement_score (number),\n"
        "  keywords (list of strings),\n"
        "  target_audience (string).\n"
        "For example:\n"
        "{\n"
        '  "sentiment_type": "positive",\n'
        '  "engagement_type": "like",\n'
        '  "sentiment_score": 0.87,\n'
        '  "topic": "AI advancements",\n'
        '  "reason_for_engagement": "Positive impact on society",\n'
        '  "engagement_score": 0.8,\n'
        '  "keywords": ["AI", "technology", "future"],\n'
        '  "target_audience": "developers"\n'
        "}\n"
    )
    final_prompt = f"{prompt}\n\n{schema}"

    # Generate model response
    response = model.generate_content(final_prompt)

    # Safely parse JSON from response
    try:
        data = json.loads(response.text)
    except Exception:
        # If model returned extra text, extract embedded JSON
        import re
        matches = re.findall(r'\{.*?\}', response.text, re.DOTALL)
        data = json.loads(matches[0]) if matches else {"error": "Failed to parse JSON."}
    return data

# Example usage:
# result = execute_gemini("Analyze this tweet: 'I'm learning AI with Python every day!'")
# print(result)

def execute_gemini_for_tweet_creation(prompt, model_name="gemini-2.5-flash-lite"):
    """
    Generates a single tweet using the specified Gemini model and returns structured output.

    Parameters:
        prompt (str): The input prompt describing the tweet to be generated.
        model_name (str): The Gemini model to use (default: see `genai.list_models()`).

    Returns:
        dict: Dictionary containing the generated tweet, prediction, and explanation.
    """
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name)

    full_prompt = (
        f"{prompt}\n\n"
        "Respond only in JSON with these fields:\n"
        "tweet (the generated tweet),\n"
        "prediction (engagement prediction),\n"
        "explanation (rationale for prediction).\n"
        "For example:\n"
        '{\n'
        '  "tweet": "Exciting news in AI today!",\n'
        '  "prediction": "High engagement",\n'
        '  "explanation": "AI is trending and the tweet is concise."\n'
        '}'
    )

    response = model.generate_content(full_prompt)
    try:
        return json.loads(response.text)
    except Exception:
        import re
        matches = re.findall(r'\{.*?\}', response.text, re.DOTALL)
        return json.loads(matches[0]) if matches else {"error": "Failed to parse JSON."}

def execute_gemini_for_tweets_comparison(prompt, model_name="gemini-2.5-flash"):
    """
    Generates two tweets and compares them using the specified Gemini model.

    Parameters:
        prompt (str): The input prompt describing the tweet generation and comparison task.
        model_name (str): The Gemini model to use (default: see `genai.list_models()`).

    Returns:
        dict: Dictionary containing both tweets, comparison, prediction, and explanation.
    """
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name)

    full_prompt = (
        f"{prompt}\n\n"
        "Respond only in JSON with these fields:\n"
        "tweet_a (first generated tweet),\n"
        "tweet_b (second generated tweet),\n"
        "tweet_a_vs_tweet_b (comparative analysis),\n"
        "prediction (which tweet will perform better),\n"
        "explanation (rationale for prediction).\n"
        "For example:\n"
        '{\n'
        '  "tweet_a": "...",\n'
        '  "tweet_b": "...",\n'
        '  "tweet_a_vs_tweet_b": "...",\n'
        '  "prediction": "...",\n'
        '  "explanation": "..."\n'
        '}'
    )

    response = model.generate_content(full_prompt)
    try:
        return json.loads(response.text)
    except Exception:
        import re
        matches = re.findall(r'\{.*?\}', response.text, re.DOTALL)
        return json.loads(matches[0]) if matches else {"error": "Failed to parse JSON."}
