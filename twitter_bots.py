# library tweepy is used to deal with twitter API
import tweepy  

# API keys
consumer_key = "Consumer_key"
consumer_secret = "Consumer_secret_key"
access_token = "access_token"
access_token_secret = "access_token_secret"

# Authenticate
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Create API object 
api = tweepy.API(auth)

# Post 
api.update_status("Hello from my Twitter")