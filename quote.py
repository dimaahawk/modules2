from sopel import *
import random
import logging
import os

box_user = os.getlogin()


logging.basicConfig(
	filename='/home/%s/mylogs/adopsbot/quote.log' % box_user,
	level=logging.DEBUG
	)

qdb = '/home/%s/.sopel/quote.db' % box_user

@module.commands('addquote')
def addquote(bot, trigger):
        quote = trigger.group(2)
        f = open(qdb, 'a')
        f.write("\n%s" % quote)
        logging.info('%s added a quote --> %s' % (trigger.nick(), quote))
        f.close()
        bot.reply('Added it...')


@module.commands('quote')
def quote(bot, trigger):
        f = open(qdb, 'r')
        line = random.choice(list(open(qdb)))
        bot.say(line)