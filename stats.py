from sopel import *
import codecs, re
import os

boxuser = os.getlogin()
logfile = "/home/%s/.willie/adops.log" % (boxuser)  # Setting this to the original file first
epoch = "May 24 2014"

@module.commands('stats')
@module.example('.stats')
def stats(bot, trigger):
        word = trigger.group(2)
        bot.reply('Scouring the archives for your request, this may take a minute...')
	with codecs.open(logfile, 'r', 'utf-8') as f:
	    for line in f:
	        count = sum(len(re.findall( r'\b%s\b' % word, line)) for line in f if "times since" not in line)

	results = "The word %s has been mentioned %s times since %s." % (word, count, epoch)
	bot.reply(results)
