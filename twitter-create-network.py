#a script for creating a graph file out of a csv file output from TAGS
#graph files are used in Gephi
import pandas as pd
from ttp import ttp as prep
import networkx as nx

#enter filepath for your data
filename = "../twitterdata/samsung.csv"

df = pd.read_csv(filename, sep=',', encoding="utf-8")
print(df.head())
parser = prep.Parser()

network = nx.DiGraph()

print(df.columns)

for row in df.itertuples():
  tweet = parser.parse(row.text.encode('utf-8').decode('utf-8'))
  user_from = row.from_user.lower()
  #print(tweet.users)
  new_list = []

  #this for loop checks for a bug that is found in the imported parsing function
  for i in tweet.users:
    if i[-1] == "c" and i[-2] == "i" and i[-3] == "p":
      print(i)
      i = i[0:len(i)-3]
      new_list.append(i)
      print(i)
    else:
      new_list.append(i)
  if len(new_list) != 0:
    for mention in new_list:
      user_to = mention.lower()
      if not network.has_edge(user_from, user_to):
        network.add_edge(user_from, user_to, weight=0)
      network[user_from][user_to]['weight'] += 1

#writes the graph file
nx.readwrite.gexf.write_gexf(network,
  '../twitterdata/network.gexf',
  encoding='utf-8', version='1.2draft')

