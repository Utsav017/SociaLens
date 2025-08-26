---

# 🛡️ SociaLens – AI Harm Index Dashboard

SociaLens is an **AI-powered dashboard** that monitors harmful content (toxicity, misinformation, self-harm) from **CSV uploads, Reddit, and Twitter (X)**.
It helps researchers, educators, and policymakers analyze online discourse and track harmful content trends.

---

## 🚀 Features

* 📂 **Upload CSVs** of text data for analysis
* 🔗 **Fetch live posts** from:

  * Reddit (via PRAW)
  * Twitter/X (via Tweepy)
* 🤖 **AI Classification** of posts into:

  * Toxic
  * Misinformation
  * Self-harm
* 📊 **Harm Index Score** for each dataset
* 📈 **Trendline charts** over time
* ☁️ **Word Cloud** of harmful terms
* 📋 **Flagged Posts Viewer** (see exact harmful posts)
* 🌐 Deployed on **Streamlit Cloud**

---

## 🏗️ Tech Stack

* **Frontend & Deployment**: [Streamlit](https://streamlit.io/)
* **ML/NLP**: Hugging Face Transformers (`unitary/toxic-bert`, `distilbert-base-uncased`)
* **Reddit API**: PRAW
* **Twitter/X API**: Tweepy
* **Data Analysis**: Pandas, Matplotlib, WordCloud
* **Hosting**: Streamlit Cloud

---

## ⚙️ Setup (Local Development)

1. **Clone the repository**

   ```bash
   git clone https://github.com/Utsav017/SociaLens.git
   cd SociaLens
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set API credentials**
   Create a `.streamlit/secrets.toml` file (ignored by Git) with:

   ```toml
   REDDIT_CLIENT_ID = "your_reddit_client_id"
   REDDIT_CLIENT_SECRET = "your_reddit_client_secret"
   REDDIT_USER_AGENT = "sociaLens_app"

   TWITTER_API_KEY = "your_twitter_api_key"
   TWITTER_API_SECRET = "your_twitter_api_secret"
   TWITTER_ACCESS_TOKEN = "your_twitter_access_token"
   TWITTER_ACCESS_SECRET = "your_twitter_access_secret"
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment on Streamlit Cloud

1. Push your code to GitHub (`main` branch).
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo → Select `app.py` as entrypoint.
4. Add the secrets under `App Settings → Secrets`.
5. Deploy 🚀

Live App: **[SociaLens Streamlit App](https://socialens-app.streamlit.app/)**

---

## 📊 Example Workflow

1. Choose **data source** → CSV, Reddit, or Twitter.
2. Enter **subreddit / hashtag / upload file**.
3. Click **Fetch & Analyze**.
4. Dashboard shows:

   * Harm index score
   * Trendline of harmful content
   * Word cloud
   * Table of flagged posts

---

## 📂 Project Structure

```
SociaLens/
│── app.py                  # Streamlit main app
│── requirements.txt        # Dependencies
│
├── models/
│   └── load_model.py       # Loads HuggingFace classifier
│
├── utils/
│   ├── classifier.py       # Text classification helper
│   ├── fetch_reddit.py     # Reddit scraper
│   ├── fetch_twitter.py    # Twitter scraper
│   └── harm_index.py       # Harm Index calculator
```

---

## 🛡️ Future Enhancements

* ✅ Add **multi-language support (Hindi + English)**
* ✅ Support for **more social platforms**
* ✅ Export analysis results as CSV/PDF
* ✅ Add advanced ML models (fine-tuned IndicBERT, multilingual transformers)

---

## 👨‍💻 Authors

* **Utsav017** – [GitHub](https://github.com/Utsav017)
* Built with ❤️ using **Streamlit + Hugging Face**

---