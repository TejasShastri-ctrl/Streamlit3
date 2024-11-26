import streamlit as st
from textblob import TextBlob

# Title and description
st.title("Sentiment Analysis App")
st.write("Analyze the sentiment of your text input: positive, negative, or neutral.")

# Input text
user_input = st.text_area("Enter text to analyze:")

# Perform sentiment analysis
if st.button("Analyze Sentiment"):
    if user_input.strip():  # Ensure the input is not empty
        # Analyze the sentiment
        blob = TextBlob(user_input)
        sentiment_polarity = blob.sentiment.polarity
        
        # Determine sentiment category
        if sentiment_polarity > 0:
            sentiment = "Positive 😊"
        elif sentiment_polarity < 0:
            sentiment = "Negative 😟"
        else:
            sentiment = "Neutral 😐"
        
        # Display results
        st.write(f"**Sentiment Polarity:** {sentiment_polarity:.2f}")
        st.write(f"**Overall Sentiment:** {sentiment}")
    else:
        st.write("Please enter some text for analysis.")

# Footer
st.write("---")
st.write("Powered by [TextBlob](https://textblob.readthedocs.io/)")
