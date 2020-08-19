import tweepy
import json
# Setting
from Settings import APIKey, APISecret, AccessSecret, AccessToken

# Setting Autentificaion
consumer_key = APIKey
consumer_secret = APISecret
access_token = AccessToken
access_token_secret = AccessSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

# data user Me
#data = api.me()
#print (json.dumps(data._json, indent=2))

# Get data User
#data = api.get_user("@NetlifeEcuador")
#print (json.dumps(data._json, indent=2))

# Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="Netlife", 
tweet_modes="extended").items(100):
    print (json.dumps(tweet._json, indent=2)) # all text
