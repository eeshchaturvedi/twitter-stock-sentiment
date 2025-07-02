# 📈 Twitter Stock Sentiment Analysis

Can Twitter sentiment predict stock market movement?  
This project explores that question using basic Natural Language Processing (NLP) on tweets related to **Reliance stock**.

---

## 🧠 What It Does

- Loads a sample dataset of Reliance-related tweets from a JSON file
- Applies sentiment analysis using the VADER NLP model
- Adds custom financial keywords to better capture market tone (e.g., "bullish", "dip", "spike")
- Outputs results to a CSV file
- (Optional) Visualizes sentiment distribution in a bar chart

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas
- VADER SentimentIntensityAnalyzer
- Matplotlib (for plotting)

---

## 💻 How to Run This Project

### 1. Clone this repo:
```bash
git clone https://github.com/eeshchaturvedi/twitter-stock-sentiment.git
cd twitter-stock-sentiment
