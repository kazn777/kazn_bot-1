import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import traceback


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def sm(ctx):
    embed = discord.Embed(title="choco stupid mountain",description="choco stupid mountain",url = "https://clips.twitch.tv/GoodReliableArmadilloDoggo-QAW30SL4Rrgfkdrl",color=0xff0000)
    await ctx.send(embed=embed)

bot.run(token)
