import tweepy
import praw
from tweepy_keys_and_tokens import *
from praw_keys_and_tokens import *

twit_auth = tweepy.OAuthHandler(twit_consumer_key, twit_consumer_secret)
twit_auth.set_access_token(twit_access_token, twit_token_secret)

twit_api = tweepy.API(twit_auth)

reddit = praw.Reddit(client_id=redd_client_id,
                     client_secret=redd_client_secret,
                     password=redd_password,
                     user_agent=redd_user_agent,
                     username=redd_username)
print(redd_client_id)
print(redd_client_secret)
print(redd_password)
print(redd_user_agent)
print(redd_username)

print(reddit.user.me())
print('done')

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text + '\n')

# api.update_status('first tweet')
# print('done')
