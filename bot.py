import discord, config, aiohttp, psutil
from discord.ext import commands

def get_prefix(bot, message):
    prefixes = ["e!", "exo "]
    
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))

@bot.event
async def on_ready():
    print("exorium has started successfully")
    
extensions = ['jishaku',
              'cogs.info'
]

if __name__ == '__bot__':
  for extension in extensions:
    bot.load_extension(extension)

bot.session = aiohttp.ClientSession(loop=bot.loop)

bot.run(config.token)
