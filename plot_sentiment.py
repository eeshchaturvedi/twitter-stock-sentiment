import pandas as pd
import matplotlib.pyplot as plt

# Load the sentiment CSV
df = pd.read_csv('reliance_tweets_with_sentiment.csv')

# Count sentiment types
sentiment_counts = df['sentiment'].value_counts()

# Plot bar chart
plt.figure(figsize=(6, 4))
bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'gray', 'red'])
plt.title('Sentiment Distribution of Reliance Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')

# Annotate each bar with the count
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('sentiment_distribution.png')  # saves the chart image
plt.show()
