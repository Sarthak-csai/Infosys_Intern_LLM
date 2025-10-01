# Social Media Content Optimizer

Social Media Content Optimizer is an open-source tool that leverages the **X (Twitter) API** and **Gemini API** to help brands like Microsoft generate and compare highly engaging, brand-authentic tweets—using real engagement data and state-of-the-art AI.

---

## 🚀 Features

- **Generate tweets** using few-shot learning, guided by your brand’s top-performing tweet examples.
- **Compare tweets** from different AI models, with AI-predicted engagement and detailed explanations.
- **Sentiment & engagement analysis** tailoring results to your audience.
- **Modern, responsive UX:** Built with Flask, JS, and dynamic CSS.
- **Modular, extensible code** for research or production use.

---

## 🌱 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sarthak-csai/Infosys_Intern_LLM
cd Infosys_Intern_LLM
```

### 2. Environment Configuration

Social Media Content Optimizer requires credentials for the X (Twitter) API and the Gemini API.

**Create a file named `.env` in the project root directory with the following:**

```env
# ==== X (Twitter) API credentials ====
API_KEY=your_twitter_api_key
API_SECRET_KEY=your_twitter_api_secret_key
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
BEARER_TOKEN=your_twitter_bearer_token

# ==== Gemini API ====
GEMINI_API_KEY=your_gemini_api_key
```
- Never commit your real `.env` file or secrets to GitHub.
- See `.env.example` for a template.

### 3. Install Dependencies

All Python dependencies are included in `requirements.txt`:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the Web App

```bash
python app.py
```

Go to [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💻 Usage

- Use the **Generate Tweet** tab to create highly engaging, on-brand tweets.
- Use the **Compare Tweets** tab to see two model outputs side-by-side, with AI-powered analysis and prediction of the winner.

---

## 🧠 How It Works

1. Collects tweets and engagement data for your brand using the **X API**.
2. Analyzes tweets with the **Gemini API** for sentiment, keywords, and engagement insights.
3. Selects your brand’s top-performing tweets as few-shot examples.
4. Uses these examples to guide the Gemini model to generate and compare tweets specifically tuned for your brand voice and audience.

---

## 👨‍💻 Contributing

1. Fork the repository
2. Make a branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push and open a Pull Request!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Questions?

Open an [issue](https://github.com/Sarthak-csai/Infosys_Intern_LLM/issues) or submit a [pull request](https://github.com/Sarthak-csai/Infosys_Intern_LLM/pulls).