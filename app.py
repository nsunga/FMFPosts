import tweepy
import praw
from tweepy_keys_and_tokens import *
from praw_keys_and_tokens import *

def connect_to_reddit():
    return praw.Reddit(client_id=redd_client_id,
                         client_secret=redd_client_secret,
                         password=redd_password,
                         user_agent=redd_user_agent,
                         username=redd_username)

# TODO: FILTERING
def title_url_dictionary(reddit, subreddit):
    title_and_url = {}
    for every_submission in reddit.subreddit('frugalmalefashion').new(limit=5):
        if every_submission.score > 15:
            title_and_url[every_submission.title] = every_submission.url
            print(every_submission.score)

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

    # for every_key, every_value in tweet_list.items():
    #     print(every_key, every_value)
    #     twit_api.update_status(every_key + ' ' + every_value)
    #     break

if __name__ == '__main__':
    main()
