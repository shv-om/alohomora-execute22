## libraries
# Import Libraries
print("Market Analyzer Importing...")

import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
# Import Libraries
from textblob import TextBlob
import sys
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import numpy as np
import os
import pycountry
import re
import string
import json

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

#####   KEYS   #####
## read keys from keys.enc\
keyspath = os.path.join(os.path.join(os.getcwd(), 'analysis'), 'keys.enc')
with open(keyspath, 'r') as keys:
  fourKeys = keys.readlines()

## load keys
GLOBAL_consumer_key = fourKeys[0][:-1]
GLOBAL_consumer_secret = fourKeys[1][:-1]
GLOBAL_access_token = fourKeys[2][:-1]
GLOBAL_access_token_secret = fourKeys[3][:-1]


###   CLASSES   ###
class dataCleaner:
  def __init__(self):
    self.stopword = None
    self.ps = None
    return

  def remove_punct(self, text):
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub("[0–9]+", "", text)
    return text

  def remove_symbols(self, text):
    text = re.sub("RT @\w+: ","",text)
    text = re.sub("[!@,~-]+"," ",text)
    return text

  def tokenization(self, text):
    text = re.split('\W+', text)
    return text

  def remove_stopwords(self, text, stopword):
    text = [word for word in text if word not in stopword]
    return text

  def stemming(self, text, ps):
    text = [ps.stem(word) for word in text]
    return text

  def basicCleaning(self, tw_list):
    #Removing Punctuation
    tw_list["punct"] = tw_list["text"].apply(lambda x: self.remove_punct(x))
    #Removing Symbols
    tw_list["symb"] = tw_list["text"].apply(lambda x: self.remove_symbols(x))
    #Appliyng tokenization
    tw_list['tokenized'] = tw_list['punct'].apply(lambda x: self.tokenization(x.lower()))
    #Removing stopwords
    self.stopword = stopword = nltk.corpus.stopwords.words('english')
    tw_list['nonstop'] = tw_list['tokenized'].apply(lambda x: self.remove_stopwords(x, stopword))
    #Appliyng Stemmer
    self.ps = nltk.PorterStemmer()
    tw_list['stemmed'] = tw_list['nonstop'].apply(lambda x: self.stemming(x, self.ps))
    #tw_list.head()
    return tw_list

  ##########
  #Cleaning Text
  def clean_text(self, text):
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation]) # remove puntuation
    text_rc = re.sub('[0-9]+', '', text_lc)
    tokens = re.split('\W+', text_rc)    # tokenization
    text = [self.ps.stem(word) for word in tokens if word not in self.stopword]  # remove stopwords and stemming
    return text

  #Appliyng Countvectorizer
  def cVectorizer(self, tw_list):
    countVectorizer = CountVectorizer(analyzer=self.clean_text)
    countVector = countVectorizer.fit_transform(tw_list["text"])

    count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names())
    return count_vect_df

  # Most Used Words
  def bestTerms(self, df):
    count = pd.DataFrame(df.sum())
    countdf = count.sort_values(0,ascending=False).head(20)
    return countdf

  ################################################

  def main(self, df):
    tw_list = self.basicCleaning(df)
    cvDF = self.cVectorizer(tw_list)
    termCountDF = self.bestTerms(cvDF)
    return tw_list, termCountDF

####################

class marketAnalyzer:
  def __init__(self):
    # keys and tokens from the Twitter Dev Console
    consumer_key = GLOBAL_consumer_key
    consumer_secret = GLOBAL_consumer_secret
    access_token = GLOBAL_access_token
    access_token_secret = GLOBAL_access_token_secret
    self.api=None

    # attempt authentication
    try:
      # create OAuthHandler object
      auth = OAuthHandler(consumer_key, consumer_secret)
      # set access token and secret
      auth.set_access_token(access_token, access_token_secret)
      # create tweepy API object to fetch tweets
      self.api = tweepy.API(auth)
    except:
      print("Error: Authentication Failed")

  def sentimentAnalysis(self, rawData):
    tw_list = rawData.copy()
    #Calculating Negative, Positive, Neutral and Compound values
    tw_list[['polarity', 'subjectivity']] = tw_list['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in tw_list['text'].iteritems():
      score = SentimentIntensityAnalyzer().polarity_scores(row)
      neg = score['neg']
      neu = score['neu']
      pos = score['pos']
      comp = score['compound']
      if neg > pos:
        tw_list.loc[index, 'sentiment'] = "negative"
      elif pos > neg:
        tw_list.loc[index, 'sentiment'] = "positive"
      else:
        tw_list.loc[index, 'sentiment'] = "neutral"
        tw_list.loc[index, 'neg'] = neg
        tw_list.loc[index, 'neu'] = neu
        tw_list.loc[index, 'pos'] = pos
        tw_list.loc[index, 'compound'] = comp
      # return
      return tw_list

  def count_values_in_column(self, data,feature):
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

  #Sentiment Analysis
  def percentage(self, part,whole):
    return 100 * float(part)/float(whole)

  def initCleaning(self, tweet_list):
    #Creating new dataframe and new features
    tw_list = pd.DataFrame(tweet_list)
    tw_list.drop_duplicates(inplace = True)
    #Cleaning Text (RT, Punctuation etc)
    tw_list["text"] = tw_list[0]
    #Removing RT, Punctuation etc
    remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
    tw_list['text'] = tw_list.text.map(remove_rt)
    tw_list["text"] = tw_list.text.str.lower()
    return tw_list

  def extractAllTweets(self, keyword, noOfTweet: int=200):
    #tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)
    #tweets =  get_tweets(api, query = keyword, count = noOfTweet)
    print("Got query... from module: ",keyword)
    tweets =  self.api.search_tweets(q = keyword, count = noOfTweet, lang='en')
    positive, negative, neutral, polarity = 0, 0, 0, 0
    tweet_list, neutral_list, negative_list, positive_list = [], [], [], []
    for tweet in tweets:
      #print(tweet.text)
      tweet_list.append(tweet.text)
      analysis = TextBlob(tweet.text)
      score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
      neg, neu, pos, comp = score['neg'], score['neu'], score['pos'], score['compound']
      polarity += analysis.sentiment.polarity

      if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
      elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1

      elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1

    positive = self.percentage(positive, noOfTweet)
    negative = self.percentage(negative, noOfTweet)
    neutral = self.percentage(neutral, noOfTweet)
    polarity = self.percentage(polarity, noOfTweet)
    positive = format(positive, '.1f')
    negative = format(negative, '.1f')
    neutral = format(neutral, '.1f')

    #Creating PieCart
    sentimentCounter = pd.DataFrame({'positive':[positive], 'negative':[negative], 'neutral':[neutral]})
    #print(lol.shape)

    ######
    tweet_list = self.initCleaning(tweet_list)
    tweet_list.drop(columns=[0], inplace=True)

    return tweet_list, sentimentCounter
  
  def saveJson(self, jsonDict, fname):
    with open(fname, "w") as outfile:
      json.dump(jsonDict, outfile)
    return
  
  def postProcess(self, df, indexColName, forNa=0):
    df.reset_index(inplace=True)
    df.rename(columns={'index':indexColName}, inplace=True)
    df[indexColName] = df[indexColName].fillna(forNa)
    ## dict to json
    dictKeys = list(df[df.columns[0]])
    dictVals = list(df[df.columns[-1]])
    dictionary = dict(zip(dictKeys,dictVals))
    return dictionary

  ###################################################
  ###################################################

  def getSentiments(self, query, count=2000):
    # get tweets
    twDF, sentimentCounter = self.extractAllTweets(query, count)
    ##
    dc = dataCleaner()
    cleanedDF, termCountDF = dc.main(twDF)
    ##
    sentiDF = self.sentimentAnalysis(cleanedDF)
    counter = self.count_values_in_column(sentiDF,"sentiment")
    ####### SAVING #####
    termCountDFDict = self.postProcess(termCountDF,'words',forNa=query)
    self.saveJson(termCountDFDict, 'json/termCountDF.json')
    counterFDict = self.postProcess(counter,'sentiment','negative and neutral')
    self.saveJson(counterFDict, 'json/counter.json')
    ## jsons
    sentimentCounter.to_json('json/sentimentCounter.json')
    cleanedDF.to_json('json/cleanedDF.json')
    sentiDF.to_json('json/sentiDF.json')
    return
