import discord, config, aiohttp, psutil
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


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix = get_prefix,
            case_insensitive = True,
            owner_id = 698080201158033409,
            reconnect = True,
            allowed_mentions = discord.AllowedMentions.none(),
            max_messages=10000)

        for extension in config.EXTENSIONS:
            try:
                self.load_extension(extension)
                print(f'[EXTENSION] {extension} was loaded successfully!')
            except Exception as e:
                tb = traceback.format_exception(type(e), e, e.__traceback__) 
                tbe = "".join(tb) + ""
                print(f'[WARNING] Could not load extension {extension}: {tbe}')
