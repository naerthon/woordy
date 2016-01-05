from tokens import Tokens as tk
from random import randint
import tweepy

class Retrievy(object):

    twitter_user_names = ['lemondefr', 'Le_Figaro']

    @staticmethod
    def __get_user_name(index):
        return Retrievy.twitter_user_names[index]


    @staticmethod
    def auth_handler():
        auth_name = tweepy.OAuthHandler(tk.CONSUMER_KEY, tk.CONSUMER_SECRET)
        auth_name.set_access_token(tk.ACCESS_TOKEN, tk.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth_name)
        return api


    def get_tweets(username, count):
        api = Retrievy.auth_handler()
        tweets=api.user_timeline(id=username, count=count)
        for tweet in tweets:
            print(tweet.text)


    def random_tweet_pre():
        random_index = randint(0, len(Retrievy.twitter_user_names) - 1)
        username = Retrievy.__get_user_name(random_index)
        api = Retrievy.auth_handler()
        counter_limit = 200
        tweets = api.user_timeline(id=username, count=counter_limit)
        random_number = randint(0, counter_limit)
        tweet = tweets[random_number]
        return tweet.text


    def random_tweet(username):
        api = Retrievy.auth_handler()
        counter_limit = 200
        tweets = api.user_timeline(id=username, count=counter_limit)
        random_number = randint(0, counter_limit)
        print(random_number)
        tweet = tweets[random_number]
        return tweet.text
