import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import main

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

app = Flask(__name__)

cors = CORS(app)


@app.route("/", methods=['GET'])
def get():
    print("get route reached")
    return {}


@app.route("/input", methods=['POST'])
def getInput():
    input = request.get_json()['data']
    print(input)
    return main.run_nlp(input)


if __name__ == "__main__":
    app.run(debug=True)
