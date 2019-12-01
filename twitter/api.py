import tweepy
import configparser

class Twitter():

    def __init__(self, config_file):
        config = configparser.RawConfigParser()
        config.read(config_file)

        consumer_key=config.get('credentials', 'consumer_key')
        consumer_secret=config.get('credentials', 'consumer_secret')
        access_token=config.get('credentials', 'access_token')
        access_token_secret=config.get('credentials', 'access_token_secret')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def get_api(self):
        return self.api
