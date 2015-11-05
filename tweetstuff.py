import tweepy
from sopel import *
import random

try:  # Check for key file
	from twitter_keys import keys
except ImportError:  # Else...well get one
	print 'Get your keys sorted....'

@module.commands('tweetstuff')
def tweetstuff(bot, trigger):

	# Storing keys in a separate file for security reasons
	# Check bottom of key file structure
	CONSUMER_KEY = keys['CONSUMER_KEY']
	CONSUMER_SECRET = keys['CONSUMER_SECRET']
	ACCESS_TOKEN = keys['ACCESS_TOKEN']
	ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']


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

# Version 2.0

'''
Key file name : twitter_keys.py
contains a dictionary called keys

keys = {
	'CONSUMER_KEY': 'put your key here',
	'CONSUMER_SECRET': 'put your key here',
	'ACCESS_TOKEN': 'put your key here',
	'ACCESS_TOKEN_SECRET': 'put your key hereL'
}


'''


