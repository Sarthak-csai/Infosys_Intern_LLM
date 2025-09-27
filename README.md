# Market Content Optimizer

Market Content Optimizer is an open-source tool that leverages the **X (Twitter) API** and **Gemini API** to help brands like Microsoft generate and compare highly engaging, brand-authentic tweets—using real engagement data and state-of-the-art AI.

---

## 🚀 Features

- **Extract tweets** and metrics from any X (Twitter) handle with the X API.
- **Analyze sentiment & engagement** of tweets using Gemini API.
- **Few-shot generation**: Contextualizes new tweets with your brand’s real, top-performing examples.
- **Compare tweets** from different AI models and get predicted engagement.
- **Modern, responsive UX** (Flask + JS/CSS).
- Fully modular for easy extension.

---

## 🌱 Getting Started

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/market-content-optimizer.git
cd market-content-optimizer
```

---

### 2. **Set up Environment**

- Create a `.env` file with your API keys:

```env
GEMINI_API_KEY=your-gemini-api-key
X_BEARER_TOKEN=your-twitter-bearer-token
```

- Or export variables before running.

---

### 3. **Install Python Dependencies**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You’ll need:

- `flask`
- `requests`
- `python-dotenv`
- Gemini client library

---

### 4. **Extract and Analyze Tweets**

Example: Save as `extract_and_analyze.py`
```python
import os, json, requests
from run_prompt import execute_gemini

BEARER_TOKEN = os.environ["X_BEARER_TOKEN"]

def get_tweets(username, n=50):
    url = f"https://api.twitter.com/2/tweets/search/recent?query=from:{username}&tweet.fields=public_metrics&max_results={n}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    resp = requests.get(url, headers=headers)
    return resp.json().get("data", [])

tweets = get_tweets("Microsoft")

with open("extracted_tweets.json", "w") as f:
    json.dump(tweets, f, indent=2)

analyzed = []
for tweet in tweets:
    prompt = f"""Tweet: {tweet["text"]}
like_count: {tweet["public_metrics"]["like_count"]}
retweet_count: {tweet["public_metrics"]["retweet_count"]}
reply_count: {tweet["public_metrics"]["reply_count"]}
Read the tweet with regard to its public reception and provide keywords and sentiment analysis score"""
    result = execute_gemini(prompt)   # Implement this to call Gemini API
    out = json.loads(result)
    out["tweet"] = tweet["text"]
    analyzed.append(out)
with open("analyzed_tweets.json", "w") as f:
    json.dump(analyzed, f, indent=2)
```

---

### 5. **Run the Web App**

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) and try it!

---

### 6. **Usage**

- Use the **Generate Tweet** tab to create a new, engaging tweet.
- Use the **Compare Tweets** tab to see two model outputs with clear, AI explanations and a predicted winner.

---

## 🧠 How It Works

1. Extract tweets with full engagement data via the **X API**.
2. Analyze sentiment, keywords, and engagement scores with the **Gemini API**.
3. Collect top-performing tweets as few-shot examples.
4. Use few-shot prompting to generate and compare new tweets for any product or campaign.
5. Get detailed, AI-powered analysis and winner prediction for head-to-head comparisons.

---

## 🛠️ Code Example: Gemini Prompt

```python
def execute_gemini(prompt: str):
    import google.ai.generativelanguage as genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.generate_content(prompt=prompt)
    return response.text  # Or adapt to your Gemini setup
```

---

## ⚙️ Configuration

- Set `GEMINI_API_KEY` (for Gemini API) and `X_BEARER_TOKEN` (for Twitter API v2) in `.env` or export them in your shell.
- Example `.env` file:

```env
GEMINI_API_KEY=your-gemini-api-key
X_BEARER_TOKEN=your-twitter-bearer-token
```

---

## 👨‍💻 Contributing

1. Fork the repository
2. Make a branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push & open a Pull Request!

---

## 📄 License

MIT

---

## 🙋 FAQ

**Q: Can I use this for brands besides Microsoft?**  
A: Yes! Change the Twitter handle when extracting tweets.

**Q: Can I add more social media platforms?**  
A: Definitely—PRs welcome!

---

## 📫 Questions?

Open an [issue](https://github.com/yourusername/market-content-optimizer/issues) or submit a [pull request](https://github.com/yourusername/market-content-optimizer/pulls).

---

**Market Content Optimizer**  
*Create and compare tweets that engage—built on real data, guided by AI!*

```

---

✔️ This README is ready to drop into your repo using VS Code.  
Let me know if you want starter files, logo, or Open Graph badges!
