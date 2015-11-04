from sopel import *
import random

qdb = "/home/dimaa/.sopel/sloth.db"

@module.commands('addsloth')
def addquote(bot, trigger):
        quote = trigger.group(2)
        f = open(qdb, 'a')
        f.write("\n%s" % quote)
        f.close()
        bot.reply('Added')

@module.commands('sloth')
@module.example('.sloth')
def quote(bot, trigger):
        f = open(qdb, 'r')
        line = random.choice(list(open(qdb)))
        bot.say(line)
