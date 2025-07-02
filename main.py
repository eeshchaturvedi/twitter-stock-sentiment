import json
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Optional: Add custom finance-related words to boost context understanding
analyzer.lexicon.update({
    "bullish": 2.5,
    "bearish": -2.5,
    "profit": 2.0,
    "loss": -2.0,
    "spike": 1.8,
    "rally": 2.0,
    "drop": -2.0,
    "dip": -1.5,
    "surge": 2.2,
    "crash": -3.0,
    "gain": 1.5,
    "hit": -1.0,
})

# Load tweet data from JSON file
with open("reliance_tweets.json", "r") as file:
    tweets = json.load(file)

# Process each tweet
data = []
for tweet in tweets:
    date = tweet["date"]
    content = tweet["content"]
    sentiment_score = analyzer.polarity_scores(content)["compound"]
    
    if sentiment_score >= 0.05:
        sentiment = "positive"
    elif sentiment_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    data.append({
        "date": date,
        "content": content,
        "sentiment": sentiment
    })

# Save results to CSV
df = pd.DataFrame(data)
df.to_csv("reliance_tweets_with_sentiment.csv", index=False)

print("✅ Sentiment analysis complete. Results saved to reliance_tweets_with_sentiment.csv")

