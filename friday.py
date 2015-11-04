import sopel
from sopel import module
import datetime
import random

@module.commands('friday')
def friday(bot, trigger):
	tday = datetime.datetime.today().weekday()
	if tday == 0:
		bot.say("It\'s only Monday!"+' '+random.choice(['Have another cup of coffee.','You poor bastard!']))

	elif tday == 1:
		bot.say('Only Tuesday, check back later for the hookers')

	elif tday == 2:
		bot.say('Hump day! Still no hookers though')

	elif tday == 3:
		bot.say("It's only Thursday,"+' '+random.choice(['close but no cigar!', 'soon...']))

	elif tday == 4:
		bot.say('It\'s Friday' + ' ' + random.choice(['It\'s Hooker and Blow time bitches!!','Prepare the hookers and blow!','The hookers and blow are plentiful']))

	else:
		bot.say('It\'s the weekend! Rest up for next week.')

@module.commands('fridayfun')
def fridayfun(bot, trigger):
	bot.say('  __|   _)      |              ')
	bot.say('  _|  _| |   _` |   _` |  |  | ')
	bot.say(' _| _|  _| \__,_| \__,_| \_, | ')
	boy.say('                         ___/  ')