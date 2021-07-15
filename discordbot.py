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
    embed = discord.Embed(title="kazn's database",description="",color=0xff0000)
    embed.add_field(name="Blog",value="[link](https://kazn-mk-games.com)")
    embed.add_field(name="TikTok",value="[link](https://www.tiktok.com/@kaznmk64)")
    embed.add_field(name="MK64 TimeTralslist(Blog)",value="[link](https://kazn-mk-games.com/gamedata)")
    embed.add_field(name="MK64 TimeTralslist(Youtube)",value="[link](https://youtube.com/playlist?list=PLdGKAlqxxNI4oOn7v2LppK5j_oYJH7Lrf)")
    embed.add_field(name="MK64 150cc Timelist",value="[link](https://youtube.com/playlist?list=PLdGKAlqxxNI7DiAjbzY8-GQJsxa2GwtVO)")
    embed.add_field(name="MK64 Speedrunlist(Blog)",value="[link](https://kazn-mk-games.com/gamedata/#RTASpeedrun)")
    await ctx.send(embed=embed)

bot.run(token)
