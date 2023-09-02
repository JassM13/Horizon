import time
import platform

import discord
from discord.ext import commands


class InfoCommands(commands.Cog):
  @commands.command(alias=["info"])
  async def stats(self, ctx):
    embed = discord.Embed(title="Stats", color=0x00ff00)
    embed.add_field(name="Guilds", value=len(ctx.bot.guilds), inline=True)
    embed.add_field(name="Channels", value=sum(1 for _ in ctx.bot.get_all_channels()), inline=True)
    embed.add_field(name="Users", value=sum(1 for _ in ctx.bot.get_all_members()), inline=True)
    embed.add_field(name="Discord.py Version", value=discord.__version__, inline=True)
    embed.add_field(name="OS", value=f"{platform.system()} {platform.release()}", inline=True)
    await ctx.send(embed=embed)


  @commands.slash_command()
  async def ping(self, ctx):
    pre_typing = time.monotonic()
    await ctx.typing()
    latency = int(round(time.monotonic() - pre_typing) * 1000)

    embed = discord.Embed(title=":ping_pong: Pong!", description=f"{latency}ms", color=0x00ff00)
    await ctx.send(embed=embed)