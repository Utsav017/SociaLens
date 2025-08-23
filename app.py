import streamlit as st
import pandas as pd
from models.load_model import load_classifier
from utils.classifier import classify_text
from utils.harm_index import calculate_harm_index
from utils.fetch_reddit import fetch_reddit
from utils.fetch_twitter import fetch_twitter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("🛡️ SociaLens – AI Harm Index Dashboard")

source = st.selectbox("Select Data Source", ["Upload CSV", "Reddit", "Twitter"])
keyword = st.text_input("Enter Keyword / Subreddit / Hashtag")
limit = st.slider("Number of posts", 10, 200, 50)

classifier = load_classifier()

if st.button("Fetch & Analyze"):
    if source == "Upload CSV":
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
        else:
            st.warning("Please upload a CSV file")
            st.stop()
    elif source == "Reddit":
        df = fetch_reddit(keyword, limit)
    elif source == "Twitter":
        df = fetch_twitter(keyword, limit)

    # Classify
    results = []
    for text in df['text'].astype(str):
        cats = classify_text(text, classifier)
        results.append(cats)

    results_df = pd.DataFrame(results)
    df = pd.concat([df, results_df], axis=1)

    # Harm Index
    index = calculate_harm_index(df)
    st.write("### Harm Index Results")
    st.json(index)

    # Trendline
    if 'date' in df.columns:
        trend = df.groupby('date')[['toxic','misinfo','selfharm']].mean()
        st.line_chart(trend)

    # Word Cloud
    harmful_terms = " ".join(df[df[['toxic','misinfo','selfharm']].any(axis=1)]['text'])
    if harmful_terms:
        wc = WordCloud(width=800, height=400, background_color="black").generate(harmful_terms)
        fig, ax = plt.subplots()
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

    # Flagged Posts
    st.write("### Flagged Posts")
    st.dataframe(df[df[['toxic','misinfo','selfharm']].any(axis=1)][['date','text','toxic','misinfo','selfharm']])
