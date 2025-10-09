import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json

# Load environment variables from .env file
load_dotenv()

# Access Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def execute_gemini(prompt):
    """
    Executes a Gemini model call with a structured prompt and schema-based response.

    Parameters:
        prompt (str): The input prompt describing the task (e.g., sentiment analysis).

    Returns:
        str: JSON-formatted string response from the Gemini model.
    """

    # Step 1: Initialize Gemini client with API key
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Step 2: Specify the model to use
    model = "gemini-2.5-flash-lite"

    # Step 3: Format the user prompt as content
    contents = [
        types.Content(
            role="user",  # Indicates this is a user message
            parts=[
                types.Part.from_text(text=prompt),  # Convert prompt to Gemini-compatible format
            ],
        ),
    ]

    # Step 4: Define optional tools (currently unused)
    tools = [
        # Example: types.Tool(googleSearch=types.GoogleSearch()),
    ]

    # Step 5: Configure generation settings and expected response schema
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,  # No extra compute budget for reasoning
        ),
        response_mime_type="application/json",  # Expect structured JSON output
        response_schema=genai.types.Schema(  # Define expected fields and types
            type=genai.types.Type.OBJECT,
            required=["sentiment_type", "sentiment_score", "topic", "keywords", "target_audience"],
            properties={
                "sentiment_type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=[
                        "angry", "sad", "fearful", "sarcastic", "motivational", "positive",
                        "negative", "excited", "neutral"
                    ],
                ),
                "engagement_type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["like", "reply", "impression", "retweet"],
                ),
                "sentiment_score": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "topic": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "reason_for_engagement": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "engagement_score": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "keywords": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    items=genai.types.Schema(type=genai.types.Type.STRING),
                ),
                "target_audience": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
            },
        ),
    )

    # Step 6: Call the Gemini model with the prompt and configuration
    result = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Step 7: Return the model's response as a JSON string
    return result.text

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