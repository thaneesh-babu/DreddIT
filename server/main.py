from nltk.util import clean_url
import praw
import pandas as pd
from praw.models import MoreComments
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from wordcloud import WordCloud

import seaborn as sns
import matplotlib.pyplot as plt
import emoji
import re
import en_core_web_sm
import spacy
import os

from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(client_id=os.environ.get("CLIENT_ID"),
                     client_secret=os.environ.get("CLIENT_SECRET"),
                     user_agent="ua")

subreddit = reddit.subreddit('gatech')

nlp = en_core_web_sm.load()
allStopWords = nlp.Defaults.stop_words

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|http\S+')
lemmatizer = WordNetLemmatizer()

sia = SIA()

for submission in subreddit.hot(limit=5):

    allComments = []
    post = reddit.submission(id=submission.id)
    for comment in post.comments.list():
        allComments.append(comment.body)
    print(len(allComments))
    stringifiedList = [str(com) for com in allComments]
    uncleanString = ' , '.join(stringifiedList)

    emojilessString = emoji.get_emoji_regexp().sub(u'', uncleanString)
    tokenizedString = tokenizer.tokenize(emojilessString)
    # lowering the case of all words
    cleanedString = [word.lower() for word in tokenizedString]

    # removing stop words
    cleanedString = [
        word for word in cleanedString if word not in allStopWords]

    # normalizing words using lemmatizing
    cleanedString = ([lemmatizer.lemmatize(word) for word in cleanedString])

    results = []
    for word in cleanedString:
        polarityScore = sia.polarity_scores(word)
        polarityScore['words'] = word
        results.append(polarityScore)

    pd.set_option('display.max_columns', None, 'max_colwidth', None)
    df = pd.DataFrame.from_records(results)

    df['label'] = 0
    df.loc[df['compound'] > 0.10, 'label'] = 1
    df.loc[df['compound'] < -0.10, 'label'] = -1

    fig, ax = plt.subplots(figsize=(8, 8))
    counts = df.label.value_counts(normalize=True) * 100

    sns.barplot(x=counts.index, y=counts, ax=ax)

    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_ylabel("Percentage")

    plt.show()

    positiveWords = list(df.loc[df['label'] == 1].words)
    negativeWords = list(df.loc[df['label'] == -1].words)
    positiveFreq = FreqDist(positiveWords).most_common(10)
    negativeFreq = FreqDist(negativeWords).most_common(10)

    topPositiveWords = [str(w) for w in positiveFreq]
    topPositiveString = ' , '.join(topPositiveWords)
    topNegativeWords = [str(w) for w in negativeFreq]
    topNegativeString = ' , '.join(topNegativeWords)

    wordcloud_positive = WordCloud(
        background_color='white').generate(topPositiveString)
    wordcloud_negative = WordCloud().generate(topNegativeString)

    plt.imshow(wordcloud_positive, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    plt.imshow(wordcloud_negative, interpolation='bilinear')
    plt.axis("off")
    plt.show()
