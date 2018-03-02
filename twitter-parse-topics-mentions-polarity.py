import re
from textblob import TextBlob

import pandas as pd
from ttp import ttp as prep


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

filename = "../twitterdata/samsung.csv"

df = pd.read_csv(filename, sep=',', encoding="utf-8")
print(df.head())
parser = prep.Parser()

print(df.columns)

mentions = []
hashtags = []
polarities = []

for row in df.itertuples():
  tweet = parser.parse(row.text.encode('utf-8').decode('utf-8'))
  user_from = row.from_user.lower()

  mention_list = []
  for mention in tweet.users:
      user_to = mention.lower()
      mention_list.append(user_to)

  mentions.append(mention_list)

  tag_list = []
  for tag in tweet.tags:
      tag_list.append(tag)
  #print(tweet.users)
  #print(tweet.tags)
  hashtags.append(tag_list)

  sentiment = get_tweet_sentiment(row.text)
  polarities.append(sentiment)

df['mentions'] = mentions
df['hashtags'] = hashtags
df['polarity'] = polarities

print(df.head())

output = "../twitterdata/output.csv"

df.to_csv(output, sep=',', encoding='utf-8')


