# Market Content Optimizer

Market Content Optimizer is an open-source toolkit for **extracting, analyzing, and generating high-engagement tweets** by leveraging the X (Twitter) API and Gemini API, with a modern and intuitive web UI.

## 🚀 Features

- **Extract tweets** and public metrics from any X (Twitter) handle using X API.
- **Analyze sentiment and keywords** using Gemini API.
- **Generate new tweets** using few-shot learning—top-performing examples as context.
- **Compare tweet outputs** from multiple AI models and get engagement predictions.
- **Beautiful, responsive UX** using Flask, JS, and CSS.
- **Modular code** for easy extension, automation, or integration.

## 📦 Quick Start

### **Clone the Repository**


`git clone https://github.com/yourusername/market-content-optimizer.git`
`cd market-content-optimizer`

### **1. Set up environment variables**

Create a `.env` file or export secrets in your shell for:

```env
# .env
GEMINI_API_KEY=your-gemini-api-key
X_BEARER_TOKEN=your-twitter-bearer-token
```

Or set/export those before running.

---

### **2. Install dependencies**

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Dependencies:**
- `flask`
- `requests`
- Any Gemini client library (or openai, if you adapt to GPT-style models)
- `python-dotenv` _(for loading .env variables)_
- [Optional for local dev] `flask-cors`

---

### **3. Extract and Analyze Tweets**

Example: `extract_and_analyze.py`
```python
import json
import requests
from run_prompt import execute_gemini

BEARER_TOKEN = os.environ["X_BEARER_TOKEN"]
USERNAME = "Microsoft"

def get_tweets(username, n=50):
    url = f"https://api.twitter.com/2/tweets/search/recent?query=from:{username}&tweet.fields=public_metrics&max_results={n}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    resp = requests.get(url, headers=headers)
    return resp.json()["data"]

tweets = get_tweets(USERNAME)
with open("extracted_tweets.json", "w") as f:
    json.dump(tweets, f, indent=2)

# Analyze with Gemini (example using your provided logic)
analyzed = []
for tweet in tweets:
    prompt = f"""Tweet: {tweet["text"]}
like_count: {tweet["public_metrics"]["like_count"]}
retweet_count: {tweet["public_metrics"]["retweet_count"]}
reply_count: {tweet["public_metrics"]["reply_count"]}
Read the tweet with regard to its public reception and provide keywords and sentiment analysis score"""
    result = execute_gemini(prompt)   # You implement this using Gemini API
    out = json.loads(result)
    out["tweet"] = tweet["text"]
    analyzed.append(out)
with open("analyzed_tweets.json", "w") as f:
    json.dump(analyzed, f, indent=2)
```

---

### **4. Run the Web App**

```sh
export FLASK_APP=app.py
flask run
# Or simply:
python app.py
```

Then open [http://localhost:5000](http://localhost:5000)

---

### **5. Use the Web UI**
- Use "Generate Tweet" tab to create an optimized, brand-authentic tweet.
- Use "Compare Tweets" tab for head-to-head LLM comparison and AI-based engagement prediction.

---

## 🛠 Code Sample — Gemini Prompting

```python
def execute_gemini(prompt: str) -> str:
    # Example using Gemini API (pseudo code—adapt as needed)
    import google.ai.generativelanguage as genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.generate_content(prompt=prompt)
    return response.text  # Or .json() / proper parsing
```

---

## ⚙️ Configuration

- Set up your `GEMINI_API_KEY` (Google Gemini/PaLM API) and `X_BEARER_TOKEN` (Twitter API v2).
- See `.env.example` for sample.

**Gemini API:**  
> https://ai.google.dev/api/rest/reference/rest/v1beta/models/generateContent

**X (Twitter) API:**  
> https://developer.twitter.com/en/docs/twitter-api

---

## 🧩 Extending

- Swap in another LLM by replacing the Gemini functions.
- Add more advanced analytics or custom ranking.
- Integrate other social media APIs (LinkedIn, Facebook).
- Fork the repository and submit pull requests!

---

## 📄 License

[MIT](LICENSE)

---

## 🙋 FAQ

**Q: Can I use this for brands other than Microsoft?**  
A: Yes! Change the Twitter handle in extraction and you can optimize for any account.

**Q: Is this production-ready?**  
A: This is a research/developer toolkit and may require adjustments for scale, quotas, or robust error-handling.

---

## 👏 Contributing

1. Fork the repo
2. Open an issue/discussion for your idea or bug
3. Make a branch, submit a pull request

---

**Market Content Optimizer — Supercharge your social presence with real engagement data and state-of-the-art AI.**

---

_Questions? [File an issue](https://github.com/yourusername/market-content-optimizer/issues). PRs welcome!_

---

Let me know if you want actual files (`requirements.txt`, `.env.example`, etc.) or further customization!
