import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
from transformers import pipeline

# Fetch news articles
def fetch_news(company):
    url = f"https://news.google.com/search?q={company}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("article")[:10]:
        title = item.find("h3").text if item.find("h3") else "No title"
        link = "https://news.google.com" + item.find("a")["href"][1:]
        articles.append({"title": title, "link": link})
    return articles

# Perform sentiment analysis
def analyze_sentiment(articles):
    sentiment_analyzer = pipeline("sentiment-analysis")
    for article in articles:
        sentiment = sentiment_analyzer(article["title"])[0]
        article["sentiment"] = sentiment["label"]
    return articles

# Generate Hindi TTS output
def generate_hindi_tts(data):
    summary = "\n".join(f"{item['title']} - {item['sentiment']}" for item in data)
    tts = gTTS(text=summary, lang="hi")
    audio_path = "output.mp3"
    tts.save(audio_path)
    return audio_path
