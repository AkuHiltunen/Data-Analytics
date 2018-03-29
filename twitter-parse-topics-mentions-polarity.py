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

#mentions = []
#hashtags = []

mention_columns = [[], [], [], [], [], [], [], [], [], []]
hashtag_columns = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                   [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
print(mention_columns)
polarities = []

for row in df.itertuples():
  tweet = parser.parse(row.text.encode('utf-8').decode('utf-8'))
  user_from = row.from_user.lower()

  count = 0

  for mention in tweet.users:
      mention_columns[count].append(mention)
      count += 1

  while count < 10:
      mention_columns[count].append('')
      count += 1

  count = 0

  for tag in tweet.tags:
      hashtag_columns[count].append(tag)
      count += 1

  while count < 10:
      hashtag_columns[count].append('')
      count += 1

  #part of old implementation that lumps all tags and mentions in a single column
  '''mention_list = []
  for mention in tweet.users:
      user_to = mention.lower()
      mention_list.append(user_to)

  mentions.append(mention_list)

  tag_list = []
  for tag in tweet.tags:
      tag_list.append(tag)
  #print(tweet.users)
  #print(tweet.tags)
  hashtags.append(tag_list)'''

  sentiment = get_tweet_sentiment(row.text)
  polarities.append(sentiment)

#df['mentions'] = mentions
#df['hashtags'] = hashtags
#print(hashtags)

df['mention 1'] = mention_columns[0]
df['mention 2'] = mention_columns[1]
df['mention 3'] = mention_columns[2]
df['mention 4'] = mention_columns[3]
df['mention 5'] = mention_columns[4]
df['mention 6'] = mention_columns[5]
df['mention 7'] = mention_columns[6]
df['mention 8'] = mention_columns[7]
df['mention 9'] = mention_columns[8]
df['mention 10'] = mention_columns[9]

df['hashtag 1'] = hashtag_columns[0]
df['hashtag 2'] = hashtag_columns[1]
df['hashtag 3'] = hashtag_columns[2]
df['hashtag 4'] = hashtag_columns[3]
df['hashtag 5'] = hashtag_columns[4]
df['hashtag 6'] = hashtag_columns[5]
df['hashtag 7'] = hashtag_columns[6]
df['hashtag 8'] = hashtag_columns[7]
df['hashtag 9'] = hashtag_columns[8]
df['hashtag 10'] = hashtag_columns[9]

df['polarity'] = polarities

df2 = df['polarity']

print(df.head())

output = "../twitterdata/output.csv"

df.to_csv(output, sep=',', encoding='utf-8')

#can write columns to separate files
#output2 = "../twitterdata/output2.csv"
#df2.to_csv(output2, sep=',', encoding='utf-8')



