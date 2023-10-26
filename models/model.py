from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle


import re
from bs4 import BeautifulSoup

from utils.constant import *

def preprocessed_text(text_data):
    text_data = BeautifulSoup(text_data, 'html.parser').get_text()
    text_data = re.sub(r'[^a-zA-Z]', ' ', text_data)
    text_data = re.sub('https://.*','',text_data)
    text_data = text_data.lower()
    words = text_data.split()
    preprocessed_text = ' '.join(words)

    return preprocessed_text

def predict_price(news):

    if isinstance(news, str):
        news = pd.DataFrame([news], columns=["News"])

    news["cleaned_news"] = news["News"].apply(preprocessed_text)

    with open(VECTORIZER_MODEL_PATH, "rb") as file:
        vectorizer = pickle.load(file)
    with open(RANDOM_FOREST_MODEL_PATH, "rb") as file:
        classifier = pickle.load(file)

    test_mactrix = vectorizer.transform(news["cleaned_news"])

    predictions = classifier.predict(test_mactrix)
    average = predictions.mean()

    news["Model Predictions"] = predictions
    news["Model Predictions"] = news["Model Predictions"].apply(lambda x: "Bullish" if int(x) == 1 else "Bearish")

    average = "Bullish" if average > 0.5 else "Bearish"

    news = news.drop(columns=["cleaned_news"])

    return news, average

if __name__ == "__main__":
    print("This is a module, not a script.")
    print("Run streamlit_app.py instead.")

    predict_price("This is a test news")
