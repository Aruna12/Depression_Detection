# The main package to help us with our text analysis
from textblob import TextBlob

# For reading input files in CSV format
import csv

# For doing cool regular expressions
import re

# For sorting dictionaries
import operator


# For plotting results
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# Intialize an empty list to hold all of our tweets
tweets = []
final = []

# A helper function that removes all the non ASCII characters
# from the given string. Retuns a string with only ASCII characters.
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# LOAD AND CLEAN DATA

# Load in the input file and process each row at a time.
# We assume that the file has three columns:
# 0. The tweet text.
# 1. The tweet ID.
# 2. The tweet publish date
#
# We create a data structure for each tweet:
#
# id:       The ID of the tweet
# pubdate:  The publication date of the tweet
# orig:     The original, unpreprocessed string of characters
# clean:    The preprocessed string of characters
# TextBlob: The TextBlob object, created from the 'clean' string

with open('frustration.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #reader.next()
    for row in reader:

        tweet= dict()
        tweet['orig'] = row[0]
       # tweet['id'] = int(row[0])
       # tweet['username'] = row[1]

        # Ignore retweets
        if re.match(r'^RT.*', tweet['orig']):
            continue
        print("Original Tweet : " + tweet['orig'])
        tweet['clean'] = tweet['orig']

        # Remove all non-ascii characters
        tweet['clean'] = strip_non_ascii(tweet['clean'])

        # Normalize case
        tweet['clean'] = tweet['clean'].lower()

        # Remove URLS. (I stole this regex from the internet.)
        tweet['clean'] = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet['clean'])
        # Fix classic tweet lingo
        tweet['clean'] = re.sub(r'\bthats\b', 'that is', tweet['clean'])
        tweet['clean'] = re.sub(r'\bthat\'s\b', 'that is', tweet['clean'])
        tweet['clean'] = re.sub(r'\bive\b', 'i have', tweet['clean'])
        tweet['clean'] = re.sub(r'\biv\'e\b', 'i have', tweet['clean'])
        tweet['clean'] = re.sub(r'\bim\b', 'i am', tweet['clean'])
        tweet['clean'] = re.sub(r'\bi\'m\b', 'i am', tweet['clean'])
        tweet['clean'] = re.sub(r'\bya\b', 'yeah', tweet['clean'])
        tweet['clean'] = re.sub(r'\byea\b', 'yeah', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcant\b', 'cannot', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcan\'t\b', 'cannot', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwont\b', 'will not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwon\'t\b', 'will not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bid\b', 'i would', tweet['clean'])
        tweet['clean'] = re.sub(r'wtf', 'what the fuck', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwth\b', 'what the hell', tweet['clean'])
        tweet['clean'] = re.sub(r'\br\b', 'are', tweet['clean'])
        tweet['clean'] = re.sub(r'\bu\b', 'you', tweet['clean'])
        tweet['clean'] = re.sub(r'\bk\b', 'OK', tweet['clean'])
        tweet['clean'] = re.sub(r'\bsux\b', 'sucks', tweet['clean'])
        tweet['clean'] = re.sub(r'\bno+\b', 'no', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcoo+\b', 'cool', tweet['clean'])
        tweet['clean'] = re.sub(r'\bn\b', 'in', tweet['clean'])
        tweet['clean'] = re.sub(r'/\s[\w\/]', '',tweet['clean'])
        # Emoticons?
        # NOTE: Turns out that TextBlob already handles emoticons well, so the
        # following is not actually needed.
        # See http://www.datagenetics.com/blog/october52012/index.html
        # tweet['clean'] = re.sub(r'\b:\)\b', 'good', tweet['clean'])
        # tweet['clean'] = re.sub(r'\b:D\b', 'good', tweet['clean'])
        # tweet['clean'] = re.sub(r'\b:\(\b', 'sad', tweet['clean'])
        # tweet['clean'] = re.sub(r'\b:-\)\b', 'good', tweet['clean'])
        # tweet['clean'] = re.sub(r'\b=\)\b', 'good', tweet['clean'])
        # tweet['clean'] = re.sub(r'\b\(:\b', 'good', tweet['clean'])
        # tweet['clean'] = re.sub(r'\b:\\\b', 'annoyed', tweet['clean'])
        
        # Create textblob object
        tweet['TextBlob'] = TextBlob(tweet['clean'])
        tweet['clean2'] = clean_tweet(tweet['clean'])
        tweet['clean2'] = re.sub(r'\bb \b', '', tweet['clean2'])
        tweet['TextBlob2'] = TextBlob(tweet['clean2'])

        # Correct spelling (WARNING: SLOW)
        #tweet['TextBlob'] = tweet['TextBlob'].correct()

        print("Cleaned Tweet : " + tweet['clean'])
        print("TextBlobbed Tweet : ")
        print(tweet['TextBlob'])
        print("Cleaned Tweet 2: " + tweet['clean2'])
        print("TextBlobbed Tweet 2 : ")
        print(tweet['TextBlob2'])
        a = str(tweet['TextBlob2'])
        print("a: "+a)
        final.append(a)
        tweets.append(tweet)
print(final)
with open("frustration_out.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in final:
        writer.writerow([val])