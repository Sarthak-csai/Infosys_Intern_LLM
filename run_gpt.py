from openai import OpenAI

# OPENAI_API_KEY = "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"

def execute_gpt_for_tweet_creation(prompt: str) -> dict:
    """
    INFO: This function generates a tweet using GPT-4o with structured output.
    Expected keys in response: tweet, prediction, explanation
    """

    client = OpenAI(api_key=OPENAI_API_KEY)

    instructions = (
        "You are a concise, witty assistant that generates high-performing tweets. "
        "Respond in JSON format with keys: tweet, prediction, explanation."
    )

    input_text = (
        f"Prompt: {prompt}\n\n"
        "Respond with a JSON object containing:\n"
        "- tweet: the tweet text\n"
        "- prediction: expected engagement level (e.g., high, medium, low)\n"
        "- explanation: why this tweet is likely to perform that way"
    )

    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=input_text,
    )

    # Parse the JSON string from response.text
    import json
    try:
        parsed = json.loads(response.text)
    except json.JSONDecodeError:
        parsed = {
            "tweet": None,
            "prediction": "unknown",
            "explanation": "Failed to parse GPT response as JSON."
        }

    return parsed