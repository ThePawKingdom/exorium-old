import discord, config, time, aiohttp
from discord.ext import commands

class info(commands.Cog, name="Info"):
    
  def __init__(self, bot):
    self.bot = bot

    #@commands.command(brief="Bot's latency to discord")
    #async def ping(self, ctx):
    #    """ See bot's latency to discord """
    #    discord_start = time.monotonic()
    #    bot.session = aiohttp.ClientSession(loop=bot.loop)
    #    async with self.bot.session.get("https://discord.com/") as resp:
    #        if resp.status == 200:
    #            discord_end = time.monotonic()
    #            discord_ms = f"{round((discord_end - discord_start) * 1000)}ms"
    #        else:
    #            discord_ms = "fucking dead"
    #    await ctx.send(f"\U0001f3d3 Pong   |   {discord_ms}")

    @commands.command(brief="test command")
    async def respond(self, ctx):
        await ctx.send("success")

def setup(bot):
  bot.add_cog(info(bot))
