import tweepy
import configparser
#
config = configparser.ConfigParser()
config.read('twitter.ini')


API_KEY = config['twitter']['api_key']
API_SECRET = config['twitter']['api_secret']
ACCESS_TOKEN = config['twitter']['access_token']
ACCESS_TOKEN_SECRET = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def tweet(text):
    try:
        api.update_status(status=text)
    except tweepy.TweepError as e:
        api.send_direct_message(recipient_id=config['dm']['username'], text=e.reason + e.with_traceback())






