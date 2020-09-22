# Import the Twython class
from twython import Twython
import json
import pandas as pd

def get_twitter_data(ticker):
    creds = {"CONSUMER_KEY": "5kb1EkoAm6E5ZW26y4hDIQ9gA", "CONSUMER_SECRET": "q91kk6fkPZ2gFGAC7O78RqCciea9gnCvjq24uGJRdoVnmKZnWJ", "ACCESS_TOKEN": "813194346216484865-n1ZRaYXVngZ5Z86RB4q2qUUlK2WjJKy", "ACCESS_SECRET": "72QIwsKzTXuT8C2WrTMogfEfdlvYgYc3Dbr0Mm4npCcAm"}

    # Instantiate an object
    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

    # Create our query
    query = {'q': ticker,
            'result_type': 'latest',
            'count': 100,
            'lang': 'en',
            'tweet_mode' : 'extended'
            }
    tweets = python_tweets.search(**query)
    parent_tweets = []
    for tweet in tweets['statuses']:
        user_id = tweet['user']['screen_name']
        tweet_date = tweet['created_at']
        text = tweet['full_text']
        if tweet['retweeted'] == True:
            text = tweet['retweeted_status']['full_text']
        cashtag_counter = text.count("$")
        if cashtag_counter == 1:
            baby_tweet = {'handle': user_id, 'date':tweet_date, 'tweet':text}
            parent_tweets.append(baby_tweet)
    # parent_tweets is a list which contains tweets, each element inside this is a dictionary with the 3 items - user_id, date, tweet text
    return parent_tweets
