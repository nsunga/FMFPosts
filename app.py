import tweepy
import praw
from tweepy_keys_and_tokens import *
from praw_keys_and_tokens import *

# twit_auth = tweepy.OAuthHandler(twit_consumer_key, twit_consumer_secret)
# twit_auth.set_access_token(twit_access_token, twit_token_secret)
#
# twit_api = tweepy.API(twit_auth)

# reddit = praw.Reddit(client_id=redd_client_id,
#                      client_secret=redd_client_secret,
#                      password=redd_password,
#                      user_agent=redd_user_agent,
#                      username=redd_username)

# print(reddit.user.me())

def connect_to_reddit():
    return praw.Reddit(client_id=redd_client_id,
                         client_secret=redd_client_secret,
                         password=redd_password,
                         user_agent=redd_user_agent,
                         username=redd_username)

# TODO: Instead use a dictionary -> INDEX : (TITLE, URL)
def title_url_dictionary(reddit, subreddit):
    title_and_url = {}
    for every_submission in reddit.subreddit('frugalmalefashion').new(limit=5):
        title_and_url[every_submission.title] = every_submission.url

    return title_and_url

def connect_to_twitter():
    twit_auth = tweepy.OAuthHandler(twit_consumer_key, twit_consumer_secret)
    twit_auth.set_access_token(twit_access_token, twit_token_secret)
    twit_api = tweepy.API(twit_auth)
    return twit_api

def main():
    reddit = connect_to_reddit()

    print(reddit.user.me())
    print('reddit credentials good')

    tweet_list = title_url_dictionary(reddit, reddit.subreddit('frugalmalefashion'))
    twit_api = connect_to_twitter()

    for every_key, every_value in tweet_list.items():
        print(every_key, every_value)
        twit_api.update_status(every_key + every_value)
        break
    # twit_api.update_status(tweet_list[0] +)
    # for every_title in tweet_list:
    #     print(every_title + '\n')


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text + '\n')

# api.update_status('first tweet')
# print('done')
if __name__ == '__main__':
    main()
