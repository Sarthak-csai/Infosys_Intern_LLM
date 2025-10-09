import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def execute_gemini(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    # Expand the prompt to instruct JSON output with desired fields
    formatted_prompt = (
        f"{prompt}\n\n"
        "Respond only in JSON with these fields: "
        "sentiment_type, engagement_type, sentiment_score, topic, reason_for_engagement, "
        "engagement_score, keywords (as a list), target_audience. "
        "Example:\n"
        "{\n"
        '  "sentiment_type": "positive",\n'
        '  "engagement_type": "like",\n'
        '  "sentiment_score": 0.9,\n'
        '  "topic": "AI advancements",\n'
        '  "reason_for_engagement": "Exciting new tech",\n'
        '  "engagement_score": 0.8,\n'
        '  "keywords": ["AI", "technology", "future"],\n'
        '  "target_audience": "developers"\n'
        "}"
    )

    model = genai.GenerativeModel("gemini-1.5-pro")  # Or appropriate model name
    response = model.generate_content(formatted_prompt)

    return json.loads(response.text)
    
# Usage:
# result = execute_gemini("Analyze this tweet: ...")

print(execute_gemini("Wrtie a tweet on Copilot"))

'''
def execute_gemini_for_tweet_creation(prompt, model_name="gemini-2.5-flash-lite"):
    """ Generates a single tweet using the specified Gemini model and returns structured output.
    Parameters:
        prompt (str): The input prompt describing the tweet to be generated.
        model_name (str): The Gemini model to use (default is 'gemini-2.5-flash-lite').
    Returns:
        dict: A dictionary containing the generated tweet, prediction, and explanation. 
    """
    # Initialize Gemini client with API key
    client = genai.Client(api_key=GEMINI_API_KEY)
    # Format the user prompt into Gemini-compatible content structure
    contents = [
        types.Content(
            role="user",  # Indicates this is a user message
            parts=[
                types.Part.from_text(text=prompt),  # Convert prompt to Gemini-compatible format
            ],
        ),
    ]
    # Define the expected structure of the response using a schema
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),  # No extra compute budget
        response_mime_type="application/json",  # Expect structured JSON output
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["tweet", "prediction", "explanation"],  # Required fields in the response
            properties={
                "tweet": genai.types.Schema(type=genai.types.Type.STRING),         # The generated tweet
                "prediction": genai.types.Schema(type=genai.types.Type.STRING),     # Engagement prediction
                "explanation": genai.types.Schema(type=genai.types.Type.STRING),    # Rationale for prediction
            },
        ),
    )
    # Call the Gemini model with the prompt and configuration
    result = client.models.generate_content(
        model=model_name,
        contents=contents,
        config=generate_content_config,
    )
    # Parse and return the structured JSON response
    return json.loads(result.text)

def execute_gemini_for_tweets_comparison(prompt: str, model_name="gemini-2.5-flash") -> str:

    """
    Generates two tweets and compares them using the specified Gemini model.

    Assumes the prompt includes instructions for tweet generation and performance analysis.

    Parameters:
        prompt (str): The input prompt describing the tweet generation and comparison task.
        model_name (str): The Gemini model to use (default is 'gemini-2.5-flash').

    Returns:
        dict: A dictionary containing both tweets, their comparison, prediction, and explanation.
    """

    # Initialize Gemini client with API key
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Format the user prompt into Gemini-compatible content structure
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    # Define the expected structure of the response using a schema
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=[
                "tweet_a", "tweet_b", "tweet_a_vs_tweet_b", "prediction", "explanation"
            ],
            properties={
                "tweet_a": genai.types.Schema(type=genai.types.Type.STRING),             # First generated tweet
                "tweet_b": genai.types.Schema(type=genai.types.Type.STRING),             # Second generated tweet
                "tweet_a_vs_tweet_b": genai.types.Schema(type=genai.types.Type.STRING),  # Comparative analysis
                "prediction": genai.types.Schema(type=genai.types.Type.STRING),          # Which tweet will perform better
                "explanation": genai.types.Schema(type=genai.types.Type.STRING),         # Rationale for prediction
            },
        ),
    )

    # Call the Gemini model with the prompt and configuration
    result = client.models.generate_content(
        model=model_name,
        contents=contents,
        config=generate_content_config,
    )

    # Parse and return the structured JSON response
    return json.loads(result.text)
'''