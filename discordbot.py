import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import traceback


bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def database(ctx):
    embed = discord.Embed(title="kazn's google spreadsheets",description="",color=0xff0000)
    embed.add_field(name="MK64 Past events list",value="[link](https://docs.google.com/spreadsheets/d/1OLVssG1cnNiaQas5shl44awqAdrW6ahQbfqpndac3BY/edit#gid=552396019)")
    embed.add_field(name="SGDQ2021マリオカート64解説用資料",value="[link](https://docs.google.com/spreadsheets/d/1GCy4gfZnVtDeUlMVFw1lt5kJ3rTEhjW3L4Ec0H9vPnI/edit#gid=1085278230)")
    embed.add_field(name="VAトーナメント参加マニュアル",value="[link](https://docs.google.com/spreadsheets/d/1npNm3upMzT4lSYMAUPWwOY4NbTKie9p2Ccfc33ViPqo/edit#gid=0)")

    await ctx.send(embed=embed)

bot.run(token)
