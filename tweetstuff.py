import tweepy
from sopel import *
import random

@module.commands('tweetstuff')
def tweetstuff(bot, trigger):
	# Replace the below variables with your keys & tokens
	CONSUMER_KEY = 'your_key'
	CONSUMER_SECRET = 'your_key'
	ACCESS_TOKEN = 'your_key'
	ACCESS_TOKEN_SECRET = 'your_key'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	tweet = trigger.group(2)
	if len(tweet) >= 160:
		bot.say('Your tweet is too long, please shorten')
	else:
		if not trigger.owner:
			bot.say('Don\'t tell me what to do...')
		else:
			api.update_status(status=tweet)
			bot.say('Tweeted')

# Version 1.0