import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import string

# ------------------------
# Helper Functions
# ------------------------

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def analyze_textblob(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# ------------------------
# Streamlit UI
# ------------------------

st.title(" Tweet Sentiment Analyzer")

# Sidebar
model_choice = st.sidebar.selectbox("Choose Sentiment Model", ["TextBlob", "VADER"])

st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader("Upload CSV file with tweets", type=["csv"])

# Show single tweet sentiment analysis
st.header(" Single Tweet Analysis")
user_input = st.text_area("Enter a tweet")

if st.button("Analyze Sentiment"):
    cleaned = clean_text(user_input)
    sentiment = analyze_textblob(cleaned) if model_choice == "TextBlob" else analyze_vader(cleaned)
    st.write(f"**Sentiment:** `{sentiment}`")

# Show CSV sentiment analysis
if uploaded_file:
    st.header(" Batch Tweet Analysis")
    df = pd.read_csv(uploaded_file)

    if 'text' not in df.columns:
        st.error("Uploaded CSV must have a 'text' column.")
    else:
        df['cleaned_text'] = df['text'].apply(clean_text)
        if model_choice == "TextBlob":
            df['sentiment'] = df['cleaned_text'].apply(analyze_textblob)
        else:
            df['sentiment'] = df['cleaned_text'].apply(analyze_vader)

        st.dataframe(df[['text', 'sentiment']].head(10))

        # Visualization
        st.subheader(" Sentiment Distribution")
        sentiment_counts = df['sentiment'].value_counts()

        fig, ax = plt.subplots()
        sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'], ax=ax)
        ax.set_title("Sentiment Counts")
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Number of Tweets")
        st.pyplot(fig)
