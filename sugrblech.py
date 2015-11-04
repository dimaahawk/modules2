from sopel.module import *
import random
welcomes = ['Hello Sugrblech', 'Welcome back Sugrblech', 'Good day Sugrblech!']
nicks = ['Sugrbelch', ]
@event('JOIN')
@rule(r'.*')
def welcome(bot, trigger):
	nickname = trigger.nick
	choice = random.choice(welcomes)
	if nickname == 'Sugrblech':
		bot.say(choice)
