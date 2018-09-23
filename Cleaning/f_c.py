# The main package to help us with our text analysis
from textblob import TextBlob

# For reading input files in CSV format
import csv

# For doing cool regular expressions
import re

#importing tweet preprocessor
import preprocessor as p

# Intialize an empty list to hold all of our tweets
tweets = []
final = []

# LOAD AND CLEAN DATA

with open('frustration_1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:

        tweet= dict()
        for i in row:
          if i == "":
            continue
          print()
          tweet['orig'] = i.encode('ascii')
          tweet['orig'] = tweet['orig'].decode('ascii')
          print("Original Tweet : " + tweet['orig'])
          tweet['orig'] = re.sub(r'^(b)', '', tweet['orig'])
          print("Original Tweet after removing b: " + tweet['orig'])

          tweet['orig'] = re.sub(r'rt\b', '', tweet['orig'])
          print("Original Tweet after removing rt: " + tweet['orig'])

          tweet['orig'] = re.sub(r'RT\b', '', tweet['orig'])
          print("Original Tweet after removing RT: " + tweet['orig'])



          #cleaning with preprocessor
          p.set_options(p.OPT.MENTION)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing mentions: " + tweet['orig'])

          p.set_options(p.OPT.URL)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing url: " + tweet['orig'])

          p.set_options(p.OPT.HASHTAG)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing hashtags: " + tweet['orig'])

          p.set_options(p.OPT.RESERVED)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing reserved: " + tweet['orig'])

          p.set_options(p.OPT.EMOJI)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing emoji: " + tweet['orig'])

          p.set_options(p.OPT.SMILEY)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing smiley: " + tweet['orig'])

          p.set_options(p.OPT.NUMBER)
          tweet['orig'] = p.clean(tweet['orig'])
          print("Original Tweet after removing numberss: " + tweet['orig'])

          tweet['orig'] = re.sub(':','',tweet['orig'])
          print("Original Tweet after removing ':'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(\n\n)+','',tweet['orig'])
          print("Original Tweet after removing 'slash n'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(\\n)+','',tweet['orig'])
          print("Original Tweet after removing 'slash ns'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(\\)','',tweet['orig'])
          print("Original Tweet after removing 'slash'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(\.)+','',tweet['orig'])
          print("Original Tweet after removing 'multiple dots'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(\()+','',tweet['orig'])
          print("Original Tweet after removing 'open brace'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(\))+','',tweet['orig'])
          print("Original Tweet after removing 'close brace'" + tweet['orig'])

          tweet['orig'] = re.sub(r'(https//)','',tweet['orig'])
          print("Original Tweet after removing 'https//'" + tweet['orig'])

          tweet['orig'] = re.sub(r'\\','',tweet['orig'])
          print("Original Tweet after removing 'https//'" + tweet['orig'])

          tweet['orig'] = re.sub(r"[\']",'',tweet['orig'])
          print("Original Tweet after removing 'https//'" + tweet['orig'])

          tweet['orig'] = re.sub(r'["]','',tweet['orig'])
          print("Original Tweet after removing 'https//'" + tweet['orig'])
 
          '''# Ignore retweets
          if re.match(r'^RT.*', tweet['orig']):
              continue'''

          print("Original Tweet : " + tweet['orig'])
          tweet['clean'] = tweet['orig']

          # Normalize case
          tweet['clean'] = tweet['clean'].lower()

          # Create textblob object
          tweet['TextBlob'] = TextBlob(tweet['clean'])

          # Correct spelling (WARNING: SLOW)
          #tweet['TextBlob'] = tweet['TextBlob'].correct()

          print("Cleaned Tweet : " + tweet['clean'])
          print("TextBlobbed Tweet : ")
          print(tweet['TextBlob'])
          a = str(tweet['TextBlob'])
          print("a: "+a)
          final.append(a)
          tweets.append(tweet)
print(final)
with open("frustration_out.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in final:
        writer.writerow([val])
