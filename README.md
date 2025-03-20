# News Sentiment Analysis with Text-to-Speech

This project is a **News Sentiment Analysis and Text-to-Speech (TTS) System** built using **FastAPI**, **Streamlit**, and **Hugging Face Models**. It fetches news, analyzes sentiment (Positive, Negative, Neutral), and converts the sentiment summary into speech.

## 🧰 Features

- **News Scraping**: Extracts live news articles.
- **Sentiment Analysis**: Classifies the sentiment of news (Positive/Neutral/Negative).
- **Text-to-Speech**: Converts analyzed sentiments into audio.
- **REST API**: Built with FastAPI to handle news input and return sentiment analysis.
- **Interactive UI**: Streamlit for user-friendly news input and sentiment visualization.
- **Model Integration**: Uses Hugging Face for sentiment analysis and TTS.

---

## 📁 Project Structure

```
news-sentiment-tts/
├── app.py                # FastAPI backend
├── streamlit_app.py      # Streamlit frontend
├── models/               # Pre-trained models (sentiment, TTS)
├── requirements.txt      # Required packages
└── README.md             # Project documentation
```

---

## 🛠️ Prerequisites

Ensure the following are installed:

- **Python 3.10+**
- **Git**

---

## 🚀 Installation Guide

1. **Clone the Repository:**

```bash
git clone https://github.com/SupriyaBC/news-to-speech.git
cd news-to-speech
```

2. **Create a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set Hugging Face Token (If Required):**

If using private models:
```bash
huggingface-cli login
```

5. **Download Pre-trained Models (Optional):**

```bash
python download_models.py
```

---

## 📊 Usage

### 1. Run FastAPI Backend

```bash
uvicorn app:app --reload
```
- API will be available at: `http://localhost:8000`

### 2. Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```
- Access the UI at: `http://localhost:8501`

### 3. API Endpoints

- `POST /analyze`: Analyze news sentiment

Example:
```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"news": "Stock market rises sharply."}'
```
Response:
```json
{
  "sentiment": "Positive",
  "confidence": 0.97
}
```

---

## 📦 Core Technologies

- **FastAPI**: REST API for news and sentiment analysis.
- **Streamlit**: Frontend for user input and audio output.
- **Hugging Face**: Sentiment models (`distilbert-base-uncased`) and TTS.
- **Python**: Core programming language.

---

## 📜 Key Commands

### 1. Common Git Operations

- **Clone Repository:**

```bash
git clone https://github.com/SupriyaBC/news-to-speech.git
```

- **Push Changes:**

```bash
git add .
git commit -m "Updated feature"
git push origin main
```

### 2. Virtual Environment Management

- **Activate (Linux/macOS):**

```bash
source venv/bin/activate
```

- **Activate (Windows):**

```bash
venv\Scripts\activate
```

- **Deactivate:**

```bash
deactivate
```

### 3. Model Download (Optional)

```bash
python download_models.py
```

### 4. Dependency Management

- **Freeze Dependencies:**

```bash
pip freeze > requirements.txt
```

- **Install Dependencies:**

```bash
pip install -r requirements.txt
```

### 5. Debugging & Logs

- **FastAPI Logs:**

```bash
tail -f uvicorn.log
```

- **Streamlit Logs:**

```bash
tail -f streamlit.log
```

---

## 🧪 Troubleshooting

1. **Virtual Environment Not Activating:**

Ensure you are using the correct command for your OS.

2. **Dependency Errors:**

Run:
```bash
pip install -r requirements.txt
```

3. **Slow API Response:**

Check model size and RAM availability.

---

## 📊 Future Enhancements

- Dockerize the project.
- Implement multilingual support.
- Optimize TTS output latency.

---

## 🤝 Contribution

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/new-feature
```

3. Submit a Pull Request.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 📧 Contact

For any queries, reach out to:
- **Supriya Chougale**  
- **Email:** supriyachougale2626@gmail.com

---

⭐ **If you found this project useful, don't forget to star the repository!**
