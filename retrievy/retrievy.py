from tokens import Tokens as tk
import tweepy

class Retrievy(object):


    @staticmethod
    def __get_user_name(username):
        twitter_user_names = ['lemondefr', 'Le_Figaro']

        if username in twitter_user_names:
            return username
        else:
            return False


    @staticmethod
    def auth_handler():
        auth_name = tweepy.OAuthHandler(tk.CONSUMER_KEY, tk.CONSUMER_SECRET)
        auth_name.set_access_token(tk.ACCESS_TOKEN, tk.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth_name)
        return api


    def get_tweets(count):
        username = Retrievy.__get_user_name('lemondefr')
        api = Retrievy.auth_handler()
        tweets=api.user_timeline(id=username, count=count)

        for tweet in tweets:
            print(tweet.text)

        #tweet=tweets[1] #Get the very first tweepy.model.status object
        #tweet_json=tweet._json 
        #print(tweet_json['entities']['hashtags']) # this returns dict type

