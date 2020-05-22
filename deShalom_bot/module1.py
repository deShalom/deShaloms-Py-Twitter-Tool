import tweepy
import time
import schedule
import pickle
from module2 import collectTweet

#---- Loading users security keys
keys = pickle.load(open("keysfile", "rb"))

#---- Users security keys
CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY = keys[2]
ACCESS_SECRET = keys[3]

#---- Users Tweepy authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#---- Tweet function
def tweet(txt):
    api.update_status(txt)
    return print(txt)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
