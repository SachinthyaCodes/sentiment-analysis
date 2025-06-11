#  Twitter Sentiment Analyzer with Streamlit

This project analyzes the sentiment of tweets using Python and provides an interactive Streamlit web application for single tweet predictions and batch analysis through CSV uploads. It supports sentiment detection using both TextBlob and VADER models, making it versatile and user-friendly.

This project is organized as follows:
- `.ipynb_checkpoints/`: Jupyter auto-save files.
- `data/`: Contains sample data files like `tweets.csv`.
- `.gitignore`: Used to ignore unnecessary files such as `__pycache__` or virtual environments.
- `Clean_the_Tweets.ipynb`: Jupyter notebook for cleaning tweets.
- `Load_and_explore_dataset.ipynb`: Jupyter notebook for exploring the tweet dataset.
- `Visualize_Sentiment_Counts.ipynb`: Notebook for visualizing sentiment distribution.
- `requirements.txt`: Python dependencies required to run the project.
- `sentiment_app.py`: A Streamlit-based mini web application for real-time sentiment analysis.

This sentiment analysis project is useful in the real world for multiple reasons. Businesses can track brand reputation, monitor customer feedback, and respond quickly to negative sentiment. Marketing teams use it to assess the impact of their campaigns. Journalists and researchers can analyze public opinion in response to events or policies. Data scientists can use it as a base for building more advanced NLP tools.

Features of this application include:
- Upload CSV files of tweets and perform sentiment analysis in bulk.
- Automatically clean tweets by removing mentions, hashtags, URLs, numbers, and special characters.
- Choose between TextBlob or VADER as the sentiment analysis model via a sidebar toggle.
- Classify tweets as Positive, Negative, or Neutral.
- Display sentiment distribution using bar charts built with seaborn or matplotlib.
- A Streamlit web interface to make it interactive and easy to use.

### Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/twitter-sentiment-analyzer.git
   cd twitter-sentiment-analyzer
