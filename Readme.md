# Market Content Optimizer

Market Content Optimizer is an open-source tool that leverages the **X (Twitter) API** and **Gemini API** to help brands like Microsoft generate and compare highly engaging, brand-authentic tweets—using real engagement data and state-of-the-art AI.

---

## 🚀 Features

- **Generate tweets** using few-shot learning, with your brand’s top-performing tweet examples.
- **Compare tweets** from different AI models, with predicted performance and detailed explanations.
- **Sentiment & engagement analysis** using Gemini API.
- **Modern, responsive UX** (Flask + JS/CSS).
- **Modular code** for easy extension.

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

### 4. **Run the Web App**

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) and try it!

---

### 5. **Usage**

- Use the **Generate Tweet** tab to create a new, engaging tweet.
- Use the **Compare Tweets** tab to see two model outputs with clear, AI explanations and a predicted winner.

---

## 🧠 How It Works

1. Uses the **X API** to get real tweets and engagement data for your brand (Twitter handle).
2. Analyzes tweets using the **Gemini API** for sentiment, keywords, and engagement scores.
3. Collects top-performing tweets as few-shot examples for new generations.
4. When you submit a new prompt, Market Content Optimizer uses these examples to guide the Gemini model to generate and/or compare tweets, producing outputs and AI-driven explanations that are brand-authentic and optimized for engagement.

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

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 FAQ

**Q: Can I use this for brands besides Microsoft?**  
A: Yes! Change the Twitter handle when extracting tweets.

**Q: Can I add more social media platforms?**  
A: Definitely—PRs welcome!

---

## 📫 Questions?

Open an [issue](https://github.com/Sarthak-csai/Infosys_Intern_LLM/issues) or submit a [pull request](https://github.com/Sarthak-csai/Infosys_Intern_LLM/pulls).

---