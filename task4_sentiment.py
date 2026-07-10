# Demonstrates three approaches: VADER (rule-based), TextBlob, and transformers (best accuracy)
# pip install nltk vaderSentiment textblob transformers torch

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

sample_texts = [
    "I love this product! It's amazing and easy to use.",
    "This is terrible. I hate the service and the product broke after one day.",
    "The item is okay, nothing special but works as expected.",
]

def vader_sentiment(texts):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for t in texts:
        scores = analyzer.polarity_scores(t)
        results.append({"text": t, **scores})
    return results

def textblob_sentiment(texts):
    results = []
    for t in texts:
        tb = TextBlob(t)
        results.append({"text": t, "polarity": tb.sentiment.polarity, "subjectivity": tb.sentiment.subjectivity})
    return results

def transformer_sentiment(texts):
    # uses a small model; for better accuracy use "cardiffnlp/twitter-roberta-base-sentiment"
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    results = [ {"text": t, **r} for t, r in zip(texts, classifier(texts)) ]
    return results

if __name__ == "__main__":
    print("VADER results:")
    for r in vader_sentiment(sample_texts):
        print(r)

    print("\nTextBlob results:")
    for r in textblob_sentiment(sample_texts):
        print(r)

    print("\nTransformer results:")
    for r in transformer_sentiment(sample_texts):
        print(r)