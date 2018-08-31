import tweepy
import csv
import pandas as pd
import unicodedata 
####input your credentials here
consumer_key = 'Om46sx7dvrX8G9JzgBGQWNvXS'
consumer_secret = 'PAs048q82Bh4IDz0XIbpMzdYtNuMQUbNG6pb76hmf1JfdOBHlG'
access_token = '826443242333835264-qfK6Cw4JwFGsnp7ojW8hGCi93OUug52'
access_secret = 'EdgqmlnUu1wbOdZXy5X9jTvY2atLA57IbQzAXuqA6QFNw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('depression_1.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#depression",count=1200,
                           lang="en",
                           since="2018-01-01").items():
    print (tweet.user.id, tweet.text)
    u = api.get_user(tweet.user.id)
    print (u.screen_name)
    csvWriter.writerow([tweet.user.id, u.screen_name, unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')])
