from sopel import module
import random


@module.commands('ping')
def ping(bot, trigger):
    bot.say('Pong!')


@module.commands('hi')
def hi(bot, trigger):
    bot.say('Hi ' + trigger.nick + ', ' + 'how are you this fine day')


@module.commands('goal')
def helloworld(bot, trigger):
    bot.say('GOOOOOOOOOOOOOOOOOOOOOOOOOAL!')


@module.commands('echo')
def echo(bot, trigger):
    bot.say(trigger.group(2))
#####
 
imagine_gun = ['a nerf gun','a super soaker','a potato gun','a rail gun','a plasma rifle','a sentry gun','the noisy cricket','a bolt rifle','a pulse rifle','a needler','a freeze gun','Judge Dredd\'s Law Giver','a disintegration ray','The Golden Gun','a sonic shotgun']
 
@module.commands('teach')
def teach(bot, trigger):
	if trigger.group(2) is None:
		bot.say('Who or what are you going to teach a lesson?')
	weapon = random.choice(imagine_gun)
	bot.say(trigger.nick + ' ' + 'taught' + ' ' + trigger.group(2) + ' ' + 'a lesson with' + ' ' + weapon)

# "dimaa" taught "atlas" a lesson with "a nerf gun"


@module.commands('gtb')
def gtb(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What are your gonna give that bitch?')
        return
    
    bot.say('I\'ll give that bitch'+' '+trigger.group(2)+', '+'bitches LOVE'+' '+trigger.group(2)+'.')



@module.commands('gtc')
def gtc(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What are you gonna give that client?')
        return
    
    bot.say('I\'ll give that client'+' '+trigger.group(2)+', '+'clients LOVE'+' '+trigger.group(2)+'.')
