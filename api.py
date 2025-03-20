from fastapi import FastAPI
from pydantic import BaseModel
import requests
from transformers import pipeline
from gtts import gTTS

app = FastAPI()

# Sentiment analysis pipeline with explicit model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

class CompanyRequest(BaseModel):
    company_name: str

def fetch_news(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey=80e082ff3a5e485db2edb05645d5c61a"
    response = requests.get(url).json()
    return response.get("articles", [])[:5]

def analyze_sentiment(news):
    return [{"title": article["title"], "sentiment": sentiment_analyzer(article["title"])[0]["label"]}
            for article in news]

@app.post("/analyze/")
async def analyze(request: CompanyRequest):
    news_articles = fetch_news(request.company_name)
    sentiment_results = analyze_sentiment(news_articles)

    # Generate Hindi speech summary
    summary = f"{request.company_name} के लिए समाचार विश्लेषण पूरा हुआ। "
    for item in sentiment_results:
        summary += f"शीर्षक: {item['title']}. भावना: {item['sentiment']}. "

    tts = gTTS(summary, lang="hi")
    tts.save("output.mp3")

    return {"news": sentiment_results}
