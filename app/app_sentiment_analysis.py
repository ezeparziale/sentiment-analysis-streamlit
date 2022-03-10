import nltk
nltk.download("all") 
import streamlit as st
from textblob import TextBlob

# Config
st.set_page_config(
     page_title="Sentiment Analysis",
     page_icon="😀",
    #  layout="wide",
     initial_sidebar_state="expanded"
 )

def get_sentiment(value):
    if value > 0:
        return("😃 Positive")
    elif value < 0:
        return("😏 Negative")
    else:
        return("😐 Neutral")

st.title("😀Sentiment Analysis😒")

st.caption("""
Sentiment analysis is a natural language processing (NLP) technique 
used to determine whether text is positive, negative or neutral.  
Sentiment analysis is also known as “opinion mining” or “emotion artificial intelligence”.  
You can use it in e-commerce, politics, marketing, advertising, market research for example.
""")

text = st.text_input("Input text", "I went to Paris last year. I bought a new perfume.")

blob = TextBlob(text)

st.subheader("Sentiment:")

st.write(get_sentiment(blob.sentiment.polarity))

if blob.sentiment.subjectivity > 0.5:
    st.write("Personal opinion: ✅")
else:
    st.write("Personal opinion: ❌")

st.write(blob.sentiment)

st.subheader(f"Sentences: {len(blob.sentences)}")
st.write(blob.sentences)

st.subheader(f"Noun Phrase: {len(blob.noun_phrases)}")
st.write(blob.noun_phrases)

st.subheader(f"Words: {len(blob.words)}")
st.write(blob.words)

st.subheader(f"Lemmatize: {len(blob.words)}")
for item in blob.tags:
    if item[1] == "NN":
        st.write(item[0], "-->", item[1], "-->", item[0].pluralize())
    elif item[1] == "NNS":
        st.write(item[0], "-->", item[1], "-->", item[0].singularize())
    else:
        st.write(item[0], "-->", item[1], "-->1", item[0].lemmatize("v"))

st.subheader(f"Tags:")
st.write(blob.tags)

st.subheader("Sentiment by sentences:")
for sentence in blob.sentences:
    st.write(get_sentiment(sentence.sentiment.polarity), sentence)

st.subheader("Traslate to Spanish")
st.write(blob.translate(to="es"))

st.subheader("Traslate to France")
st.write(blob.translate(to="fr"))

st.subheader(f"Spelling Correction:")
st.write(blob.correct())
