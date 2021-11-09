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
@commands.has_permissions(administrator=True)
async def database(ctx):
    embed = discord.Embed(title="kazn's google spreadsheets",description="",color=0xff0000)
    embed.add_field(name="MK64 Past events list",value="[link](https://docs.google.com/spreadsheets/d/1OLVssG1cnNiaQas5shl44awqAdrW6ahQbfqpndac3BY/edit#gid=552396019)")
    embed.add_field(name="SGDQ2021マリオカート64解説用資料",value="[link](https://docs.google.com/spreadsheets/d/1GCy4gfZnVtDeUlMVFw1lt5kJ3rTEhjW3L4Ec0H9vPnI/edit#gid=1085278230)")
    embed.add_field(name="VAトーナメント参加マニュアル",value="[link](https://docs.google.com/spreadsheets/d/1npNm3upMzT4lSYMAUPWwOY4NbTKie9p2Ccfc33ViPqo/edit#gid=0)")

    await ctx.send(embed=embed)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def cmsg(ctx):
    embed = discord.Embed(title="choco stupid mountain",description="",url = "https://www.twitch.tv/videos/1099447026",color=0xff0000)
    embed.add_field(name="2nd half part",value="[link](https://clips.twitch.tv/SnappyWonderfulToothArgieB8-FwOP3THV_Nw2pTHX)")
    embed.add_field(name="Choco nice Mountain",value="[link](https://clips.twitch.tv/BetterFastKuduM4xHeh-HhQM5C9nQVjs1QYe)")
    embed.add_field(name="CNM-> CSM",value="[link](https://clips.twitch.tv/BigCovertGalagoOSsloth-b1TaEc6IhKubSK27)")
    embed.add_field(name="mkdsabel ver",value="[link](https://clips.twitch.tv/ToughBenevolentRatBuddhaBar-AiWkoMrPsoSImLYy)")
    embed.add_field(name="Ce_Mec ver",value="[link](https://clips.twitch.tv/TenaciousMiniatureGrasshopperItsBoshyTime-KYBQtJg_OGg2WD0E)")
    embed.add_field(name="TMP ver",value="[link](https://clips.twitch.tv/AdventurousFaithfulDogPMSTwin-bwqUX6KLpebt65ST)")
    embed.add_field(name="MySong listen abney",value="[link](https://clips.twitch.tv/StylishWittyPigANELE-XqeuXk2RjskQSS1f)")
    embed.add_field(name="Mysong listen MR",value="[link](https://clips.twitch.tv/HardEnticingGrouseCoolStoryBob-D-GF4BDJaNoBV-mT)")
    embed.add_field(name="AAG ver",value="[link](https://clips.twitch.tv/CrowdedObservantNostrilPJSugar-Ib0Ouxzr1oMY7WZg)")
    embed.add_field(name="Hattok ver",value="[link](https://clips.twitch.tv/HilariousEsteemedSrirachaPJSalt-nZ9p81tVAfbj0XRs)")
    embed.add_field(name="Vocaloid ver",value="[link](https://twitter.com/i/status/1428988200219942917)")
    await ctx.send(embed=embed)
   


bot.run(token)
