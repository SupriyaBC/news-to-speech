import streamlit as st
import requests

st.title("📰 News Sentiment Analysis with Hindi Audio")

# Input for company name
company = st.text_input("Enter a Company Name", "")

if st.button("Analyze News"):
    if company:
        st.info(f"Fetching news and analyzing sentiment for: {company}")

        # Call the FastAPI service (ensure api.py is running)
        response = requests.post("http://localhost:8000/analyze/", json={"company_name": company})

        if response.status_code == 200:
            result = response.json()
            st.success("Analysis Complete!")

            # Display results
            st.write("### Sentiment Analysis")
            for news in result["news"]:
                st.write(f"**Headline:** {news['title']}")
                st.write(f"**Sentiment:** {news['sentiment']}")
                st.write("---")

            # Play the Hindi audio
            st.audio("output.mp3", format="audio/mp3")

        else:
            st.error("Failed to fetch news. Ensure the FastAPI backend is running.")
    else:
        st.warning("Please enter a company name to analyze.")
