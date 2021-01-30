import discord, config, aiohttp, psutil, traceback
from discord.ext import commands

def get_prefix(bot, message):
    prefixes = ["e!", "exo "]
    
    return commands.when_mentioned_or(*prefixes)(bot, message)


#  bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))

async def run():
    description = "A multifunctional bot"
    
    bot = Bot(description=description)
    bot.session = aiohttp.ClientSession(loop=bot.loop)
    await bot.run(config.token)


bot = commands.Bot(command_prefix=get_prefix, case_insensitive =True, allowed_mentions =discord.AllowedMentions.none(), max_messages=10000)

for extension in config.extensions:
    try:
        self.load_extension(extension)
        print(f'[extension] {extension} was loaded successfully!')
    except Exception as e:
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        tbe = "".join(tb) + ""
        print(f'[WARNING] Could not load extension {extension}: {tbe}')
