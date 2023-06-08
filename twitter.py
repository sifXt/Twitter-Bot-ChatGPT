import tweepy
from gpt import *

from constants import *

# tokens and keys saved in contants.py file

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def tweet(text):

    text = chatgpt('tell me a science fact')
    client.create_tweet(text = text)