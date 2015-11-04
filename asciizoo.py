from sopel import *

# 3.0

@module.commands('llamasay')
def llamasay(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What does the llama say?')
    
    bot.say('  \/ '+trigger.group(2))
    bot.say('<-l  /')
    bot.say('  ll')
    bot.say('  llama~')
    bot.say('  || ||')


@module.commands('dinosay')
def dinosay(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What does the dino say?')
    
    bot.say('               __')
    bot.say('              / _)')
    bot.say('     _.----._/ /   \ ')
    bot.say('    /         /  '+trigger.group(2))
    bot.say(' __/ (  | (  |')
    bot.say('/__.- |_|--|_|')


@module.commands('catsay')
def catsay(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What does that kitty say?')
    
    bot.say('     /\/\  '+trigger.group(2))
    bot.say('    /o.o \  /')
    bot.say('    \_^__/\_ ')
    bot.say('     | ,    \ ')
    bot.say('    (_(_,____| ')


@module.commands('owlsay')
def owlsay(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What does the owl say?')
    
    bot.say('___/|'+trigger.group(2))
    bot.say('\o.O|  /')
    bot.say('(___)')
    bot.say('  U')
    
@module.commands('ducksay')
def ducksay(bot, trigger):
    if trigger.group(2) is None:
        bot.say('What does the duck say?')

    bot.say('   _' + '   ' + trigger.group(2))
    bot.say('__(.)<  /')
    bot.say('\___)')
    
    