import urllib
import json
from sopel import *

@module.commands('subinfo')
def subinfo(bot, trigger):
	try:
		f = urllib.urlopen('http://www.reddit.com/r/adops/about.json')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		readers = parsed_json['data']['subscribers']
		active = parsed_json['data']['accounts_active']
		bot.say('%s AdOps Peeps Subscribed | %s Currently reading' % (readers, active))
		f.close()
	except KeyError:
		bot.say('Try again in a moment')

# Version 3_RC1
# Consider actually implementeing PRAW...