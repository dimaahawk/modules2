from sopel import *
import random
import os

boxuser = os.getlogin() 
qdb = "/home/%s/.sopel/playlist.db" % (boxuser)

@module.commands('addsong')
def addsong(bot, trigger):
        songurl = trigger.group(2).strip()
        f = open(qdb, 'a')
        f.write("\n%s" % songurl)
        f.close()
        bot.reply('Added the song.')

@module.commands('song')
@module.example('.song')
def song(bot, trigger):
        line = random.choice(list(open(qdb)))
        bot.say('Here '+trigger.nick+', traffic to this: '+line)

# Version 2