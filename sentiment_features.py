from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_score(text):
    return (SentimentIntensityAnalyzer().polarity_scores(text).get('compound')+1)/2


def get_sentiment_score_list(reviews):
    sentiments = []
    for review in reviews:
        sentiments.append(sentiment_score(review['review']))
    return sentiments


def get_rating_contrast(reviews, sentiments):
    average = 0.0
    contrasts = []
    for i in range(len(reviews)):
        review = reviews[i]
        rating = float(review['rating']-1)/4
        sentiment = sentiments[i]
        contrast = (rating-sentiment)**2
        average += contrast
        contrasts.append(contrast)
    average /= len(reviews)
    return contrasts, average
