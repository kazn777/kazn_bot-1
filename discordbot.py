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
async def cmsg(ctx):
    embed = discord.Embed(title="choco stupid mountain",description="",url = "https://clips.twitch.tv/GoodReliableArmadilloDoggo-QAW30SL4Rrgfkdrl",color=0xff0000)
    embed.add_field(name="CSM longver",value="[link](https://clips.twitch.tv/DeadNaiveTurnipLeeroyJenkins-oe9egb9VAYg4jzGg)")
    embed.add_field(name="Choco nice Mountain",value="[link](https://clips.twitch.tv/BetterFastKuduM4xHeh-HhQM5C9nQVjs1QYe)")
    embed.add_field(name="CNM-> CSM",value="[link](https://clips.twitch.tv/BitterObeseFungusPanicBasket-yacmSW8J-Wsb20tr)")
    embed.add_field(name="mkdsabel ver",value="[link](https://clips.twitch.tv/ToughBenevolentRatBuddhaBar-AiWkoMrPsoSImLYy)",inline=False)
    embed.add_field(name="Ce_Mec ver",value="[link](https://clips.twitch.tv/GentleAltruisticCamelKappaWealth-zYGgXXazVl4hZyee)")
    embed.add_field(name="TMP ver",value="[link](https://clips.twitch.tv/FunGracefulSparrowRaccAttack-qeFSem4jpPlkoXzi)")
    embed.add_field(name="king_kelp CSM comment",value="[link](https://clips.twitch.tv/FitSpoopyTaroNerfBlueBlaster-Wkn_pDhjjTQ1P98p)")
    embed.add_field(name="MySong abney reaction",value="[link](https://clips.twitch.tv/StylishWittyPigANELE-XqeuXk2RjskQSS1f)")
    await ctx.send(embed=embed)

@bot.command()
async def tt(ctx):
    embed = discord.Embed(title="kazn's TimeTrials list",description="",url = "https://youtube.com/playlist?list=PLdGKAlqxxNI4oOn7v2LppK5j_oYJH7Lrf",color=0xff0000)
    await ctx.send(embed=embed)

bot.run(token)
