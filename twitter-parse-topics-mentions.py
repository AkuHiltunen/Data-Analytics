import pandas as pd
from ttp import ttp as prep

df = pd.read_csv(filename, sep=',', encoding="utf-8")
print(df.head())
parser = prep.Parser()

print(df.columns)

mentions = []
hashtags = []

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

df['mentions'] = mentions
df['hashtags'] = hashtags
print(df.head())

df.to_csv(filename, sep=',', encoding='utf-8')


