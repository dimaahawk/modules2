from sopel import module
import random

@module.rule('.*programmatic.*')
def hi1(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('2.0?')

@module.rule('.*viewability.*')
def hi2(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('Industry saver')

@module.rule('.*dsp.*')
def hi3(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('Designated Slam Piece')

@module.rule('.*kool-aid.*')
def hi4(bot, trigger):
	bot.say('sip')

# @module.rule('.*pointroll.*')
# def hi5(bot, trigger):
# 	bot.say('discrepancy')

@module.rule('.*mobile.*')
def hi6(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say(random.choice(['mobile? lol', 'mobile OTP coming soon', 'mobile == $$$']))

@module.rule('.*bots.*')
def hi7(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say(random.choice(['Delivery', 'fakebotsite.com', '']))
		
@module.rule('.*adblock.*')
def hi8(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('amazing')


@module.rule('.*traffic.*')
def hi9(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('Like a BOSS!!')


@module.rule('.*pixels.*')
def hi10(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say(random.choice(['fire', 'so tracking']))
	

@module.rule('.*data.*')
def hi11(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('nom nom nom')
    
@module.rule('.*sales.*')
def hi12(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say(random.choice(['Get the spray bottle!','hiss!']))

@module.rule('.*fraud.*')
def hi13(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('Profit!')

@module.rule('.*shifty.*')
def hi14(bot, trigger):
	bot.say('>.>')
	bot.say('<.<')

@module.rule(r'\bpho\b')
def hi15(bot, trigger):
	bot.say('yummy')


@module.rule(r'\bebola\b')
def hi18(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 76:
		bot.say(random.choice(['Mattresses for all!', 'Did you get your mattress from ebolamattressclearance.com?', 'What happend to ebola anyway?']))

@module.rule(r'\bbro\b')
def hi19(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 26:
		bot.say('Do you even lift?!')

@module.rule(r'\bbruh\b')
def hi20(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 51:
		bot.say(random.choice(['Don\'t taze me bruh!', 'Don\'t you mean bro?', 'Don\'t bruh me bro!', 'I\'m not your bruh bro!']))

@module.rule(r'\bbitch\b')
def hi21(bot, trigger):
	rr = random.randrange(1,101)
	if rr < 11:
		bot.say('Hizzy?')

@module.rule(r'\bIsn\'t that right adopsbot?\b')
def hi22(bot, trigger):
	 bot.say('Sure is!')



@module.rule(r'\bbrb\b')
def hi23(bot, trigger):
	replies = [
		'See ya soon.',
		'Off to do work?',
		'Fine, we didn\'t want you here anyway.',
		'Bye for now.',
		'Peace!',
		'I shall eagerly await your return.',
		'Until next time...',
		'You will be missed :('
		]

	bot.say(random.choice(replies))



@module.rule('asdfghjkl')
def asdfghjkl(bot, trigger):
	bot.say(random.choice(['O__O', '^-^', '^_^', 'O.o', '^_______^', '-___-']))

#### Trial section ####

#  @module.rule('.*terster.*')

#####  

# bot.say(random.choice(['', '', '', '', '', '', '', '', '', '', '']))

